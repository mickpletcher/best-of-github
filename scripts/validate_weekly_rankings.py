#!/usr/bin/env python3
"""Validate generated weekly GitHub ranking reports."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_REPORT_COUNTS = [100, 250]
ALLOWED_REPORT_COUNTS = [50, 100, 250, 500]
README_PATH = Path("README.md")
SUMMARY_HEADER = ["Category", "Count"]
REPOSITORY_HEADER = ["Rank", "Repository", "Stars", "Language", "Description"]
REQUIRED_SOURCE_FIELDS = [
    "Generated at",
    "GitHub API endpoint",
    "Search query",
    "Sort",
    "Order",
    "Requested repository count",
    "GitHub API version",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate generated weekly GitHub ranking reports.")
    parser.add_argument(
        "--counts",
        nargs="+",
        type=int,
        choices=ALLOWED_REPORT_COUNTS,
        default=DEFAULT_REPORT_COUNTS,
        metavar="COUNT",
        help="Report sizes to validate. Allowed values: 50, 100, 250, 500.",
    )
    return parser.parse_args()


def report_path_for_count(repository_count: int) -> Path:
    return Path(f"weekly-top-{repository_count}-github-repositories.md")


def split_markdown_row(line: str) -> list[str]:
    cells: list[str] = []
    current: list[str] = []
    escaped = False

    for char in line.strip()[1:-1]:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            current.append(char)
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)

    cells.append("".join(current).strip())
    return cells


def is_separator_row(line: str) -> bool:
    cells = split_markdown_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def extract_repository_name(cell: str) -> str | None:
    html_match = re.search(r"<a\s+[^>]*>([^<]+)</a>", cell)
    if html_match:
        return html_match.group(1).strip()

    markdown_match = re.search(r"\[([^\]]+)\]\(https://github\.com/[^)]+\)", cell)
    if markdown_match:
        return markdown_match.group(1).strip()

    return None


def extract_scan_date(text: str) -> str | None:
    match = re.search(r"^Scanned on (\d{4}-\d{2}-\d{2})\.$", text, flags=re.MULTILINE)
    if match:
        return match.group(1)
    return None


def collect_errors(text: str, expected_repository_count: int) -> list[str]:
    errors: list[str] = []
    lines = text.splitlines()
    repository_rows: list[list[str]] = []
    summary_rows: list[list[str]] = []
    repositories: list[str] = []
    ranks: list[int] = []
    saw_summary_header = False
    saw_repository_header = False

    for index, line in enumerate(lines, start=1):
        if not line.startswith("|"):
            continue
        if not line.endswith("|"):
            errors.append(f"Line {index}: table row does not end with '|'.")
            continue

        cells = split_markdown_row(line)
        if cells == SUMMARY_HEADER:
            saw_summary_header = True
            continue
        if cells == REPOSITORY_HEADER:
            saw_repository_header = True
            continue
        if is_separator_row(line):
            continue

        if len(cells) == len(SUMMARY_HEADER) and cells[1].replace(",", "").isdigit():
            summary_rows.append(cells)
            continue

        if len(cells) != len(REPOSITORY_HEADER):
            errors.append(
                f"Line {index}: expected {len(REPOSITORY_HEADER)} table columns, got {len(cells)}."
            )
            continue

        repository_rows.append(cells)
        try:
            ranks.append(int(cells[0]))
        except ValueError:
            errors.append(f"Line {index}: rank is not a number: {cells[0]!r}.")

        repository_name = extract_repository_name(cells[1])
        if repository_name is None:
            errors.append(f"Line {index}: repository cell is missing a GitHub link.")
        else:
            repositories.append(repository_name)

        for column, value in zip(REPOSITORY_HEADER, cells):
            if not value:
                errors.append(f"Line {index}: {column} column is empty.")

    if not saw_summary_header:
        errors.append("Missing category summary table header.")
    if not saw_repository_header:
        errors.append("Missing repository table header.")

    if len(repository_rows) != expected_repository_count:
        errors.append(
            f"Expected {expected_repository_count} repository rows, got {len(repository_rows)}."
        )

    duplicate_repositories = sorted(
        repository for repository in set(repositories) if repositories.count(repository) > 1
    )
    if duplicate_repositories:
        errors.append(f"Duplicate repositories found: {', '.join(duplicate_repositories)}.")

    expected_ranks = list(range(1, expected_repository_count + 1))
    if sorted(ranks) != expected_ranks:
        errors.append("Repository ranks are missing, duplicated, or outside the expected range.")

    summary_total = 0
    for category, count in summary_rows:
        if not re.search(r"\[.+\]\(#.+\)", category):
            errors.append(f"Category summary row is missing a section link: {category!r}.")
        summary_total += int(count.replace(",", ""))

    if summary_rows and summary_total != expected_repository_count:
        errors.append(
            f"Category summary total should be {expected_repository_count}, got {summary_total}."
        )

    for field in REQUIRED_SOURCE_FIELDS:
        if f"- {field}:" not in text:
            errors.append(f"Missing source detail field: {field}.")

    if f"- Requested repository count: `{expected_repository_count}`" not in text:
        errors.append(
            f"Requested repository count should be `{expected_repository_count}`."
        )

    return errors


def main() -> int:
    args = parse_args()
    has_errors = False
    scan_dates: set[str] = set()
    for expected_repository_count in sorted(set(args.counts)):
        report_path = report_path_for_count(expected_repository_count)
        if not report_path.exists():
            print(f"{report_path} does not exist.", file=sys.stderr)
            has_errors = True
            continue

        text = report_path.read_text(encoding="utf-8")
        report_scan_date = extract_scan_date(text)
        if report_scan_date is None:
            print(f"ERROR [{report_path}]: Missing scanned date.", file=sys.stderr)
            has_errors = True
        else:
            scan_dates.add(report_scan_date)

        errors = collect_errors(text, expected_repository_count)
        if errors:
            has_errors = True
            for error in errors:
                print(f"ERROR [{report_path}]: {error}", file=sys.stderr)
            continue

        print(f"{report_path} passed validation.")

    if len(scan_dates) > 1:
        print(f"ERROR: Report scan dates do not match: {', '.join(sorted(scan_dates))}.", file=sys.stderr)
        has_errors = True

    if scan_dates:
        expected_scan_date = max(scan_dates)
        readme = README_PATH.read_text(encoding="utf-8")
        expected_line = f"Latest weekly scan: {expected_scan_date}."
        if expected_line not in readme:
            print(f"ERROR [{README_PATH}]: Missing freshness line: {expected_line}", file=sys.stderr)
            has_errors = True

    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
