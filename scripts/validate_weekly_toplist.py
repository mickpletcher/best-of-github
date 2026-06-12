#!/usr/bin/env python3
"""Validate the generated weeklytoplist.md report."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPORT_PATH = Path("weeklytoplist.md")
EXPECTED_REPOSITORY_COUNT = 100
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


def collect_errors(text: str) -> list[str]:
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

    if len(repository_rows) != EXPECTED_REPOSITORY_COUNT:
        errors.append(
            f"Expected {EXPECTED_REPOSITORY_COUNT} repository rows, got {len(repository_rows)}."
        )

    duplicate_repositories = sorted(
        repository for repository in set(repositories) if repositories.count(repository) > 1
    )
    if duplicate_repositories:
        errors.append(f"Duplicate repositories found: {', '.join(duplicate_repositories)}.")

    expected_ranks = list(range(1, EXPECTED_REPOSITORY_COUNT + 1))
    if sorted(ranks) != expected_ranks:
        errors.append("Repository ranks are missing, duplicated, or outside the expected range.")

    summary_total = 0
    for category, count in summary_rows:
        if not re.search(r"\[.+\]\(#.+\)", category):
            errors.append(f"Category summary row is missing a section link: {category!r}.")
        summary_total += int(count.replace(",", ""))

    if summary_rows and summary_total != EXPECTED_REPOSITORY_COUNT:
        errors.append(
            f"Category summary total should be {EXPECTED_REPOSITORY_COUNT}, got {summary_total}."
        )

    for field in REQUIRED_SOURCE_FIELDS:
        if f"- {field}:" not in text:
            errors.append(f"Missing source detail field: {field}.")

    return errors


def main() -> int:
    if not REPORT_PATH.exists():
        print(f"{REPORT_PATH} does not exist.", file=sys.stderr)
        return 1

    errors = collect_errors(REPORT_PATH.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"{REPORT_PATH} passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
