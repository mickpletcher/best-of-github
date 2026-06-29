#!/usr/bin/env python3
"""Update the README GitHub of the Day block."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import random
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python 3.8 fallback.
    ZoneInfo = None


GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
GITHUB_API_VERSION = "2022-11-28"
README_PATH = Path("README.md")
ARCHIVE_PATH = Path("github-of-the-day-archive.md")
BLOCK_START = "<!-- github-of-the-day:start -->"
BLOCK_END = "<!-- github-of-the-day:end -->"
DEFAULT_STAR_RANGES = ["3..50", "51..250", "251..1000", "1001..5000"]
DEFAULT_LANGUAGES = [
    "Python",
    "PowerShell",
    "TypeScript",
    "JavaScript",
    "Go",
    "Rust",
    "C#",
    "Shell",
]
BLOCKED_TERMS = [
    "fuck",
    "shit",
    "porn",
    "nsfw",
    "malware",
    "crack",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update README.md with a random GitHub of the Day.")
    parser.add_argument(
        "--date",
        help="Selection date in YYYY-MM-DD format. Defaults to today in SCAN_TIMEZONE.",
    )
    parser.add_argument(
        "--seed",
        help="Optional seed override for repeatable local testing.",
    )
    return parser.parse_args()


def get_selection_date() -> dt.date:
    timezone_name = os.environ.get("SCAN_TIMEZONE", "America/Chicago")
    if ZoneInfo is None:
        return dt.datetime.now(dt.timezone.utc).date()
    return dt.datetime.now(ZoneInfo(timezone_name)).date()


def build_search_query(selection_date: dt.date, rng: random.Random) -> str:
    pushed_since = selection_date - dt.timedelta(days=365)
    star_range = rng.choice(DEFAULT_STAR_RANGES)
    language = rng.choice(DEFAULT_LANGUAGES)
    return (
        f"stars:{star_range} fork:false archived:false is:public "
        f"pushed:>={pushed_since.isoformat()} language:{language}"
    )


def build_search_url(query: str, page: int) -> str:
    query_params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": "100",
        "page": str(page),
    }
    return f"{GITHUB_SEARCH_URL}?{urllib.parse.urlencode(query_params)}"


def fetch_repositories(query: str, page: int) -> list[dict]:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "best-of-github-github-of-the-day",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(build_search_url(query, page), headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {error.code} {body}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub API request failed: {error.reason}") from error

    return payload.get("items", [])


def select_repository(selection_date: dt.date, seed: str | None) -> tuple[dict, str]:
    rng = random.Random(seed or selection_date.isoformat())
    errors: list[str] = []

    for _ in range(12):
        query = build_search_query(selection_date, rng)
        page = rng.randint(1, 10)
        try:
            repositories = fetch_repositories(query, page)
        except RuntimeError as error:
            errors.append(str(error))
            continue
        safe_ascii_repositories = [
            repository
            for repository in repositories
            if repository["full_name"].isascii()
            and (not repository.get("description") or repository["description"].isascii())
            and is_readme_safe(repository)
        ]
        ascii_repositories_with_descriptions = [
            repository
            for repository in safe_ascii_repositories
            if repository.get("description")
        ]
        if ascii_repositories_with_descriptions:
            return rng.choice(ascii_repositories_with_descriptions), query
        if safe_ascii_repositories:
            return rng.choice(safe_ascii_repositories), query

    if errors:
        raise RuntimeError(errors[-1])
    raise RuntimeError("No repositories matched the GitHub of the Day search.")


def is_readme_safe(repository: dict) -> bool:
    searchable = " ".join(
        [
            repository.get("full_name", ""),
            repository.get("description") or "",
        ]
    ).lower()
    return not any(term in searchable for term in BLOCKED_TERMS)


def markdown_escape(value: str | None) -> str:
    if not value:
        return "-"
    return (
        value.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r", " ")
        .replace("\n", " ")
        .strip()
    )


def render_block(repository: dict, query: str, selection_date: dt.date) -> str:
    full_name = html.escape(repository["full_name"], quote=True)
    html_url = html.escape(repository["html_url"], quote=True)
    stars = f"{repository.get('stargazers_count', 0):,}"
    language = markdown_escape(repository.get("language"))
    description = markdown_escape(repository.get("description"))
    repository_link = f"[{full_name}]({html_url})"

    lines = [
        BLOCK_START,
        f"Selected for {selection_date.isoformat()} from public, non-fork, non-archived repositories with recent activity. This is random and is not based on popularity.",
        "",
        "| Repository | Stars | Language | Notes |",
        "| --- | ---: | --- | --- |",
        f"| {repository_link} | {stars} | {language} | {description} |",
        "",
        f"Selection query: `{query}`",
        BLOCK_END,
    ]
    return "\n".join(lines)


def archive_row(repository: dict, query: str, selection_date: dt.date) -> str:
    full_name = html.escape(repository["full_name"], quote=True)
    html_url = html.escape(repository["html_url"], quote=True)
    stars = f"{repository.get('stargazers_count', 0):,}"
    language = markdown_escape(repository.get("language"))
    description = markdown_escape(repository.get("description"))
    repository_link = f"[{full_name}]({html_url})"
    return (
        f"| {selection_date.isoformat()} | {repository_link} | {stars} | "
        f"{language} | {description} | `{query}` |"
    )


def update_readme(block: str) -> None:
    readme = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{re.escape(BLOCK_START)}.*?{re.escape(BLOCK_END)}",
        flags=re.DOTALL,
    )
    if pattern.search(readme):
        updated = pattern.sub(block, readme, count=1)
    else:
        anchor = "## Project References"
        section = f"## GitHub of the Day\n\n{block}\n\n"
        if anchor not in readme:
            raise RuntimeError(f"Could not find README anchor: {anchor}")
        updated = readme.replace(anchor, f"{section}{anchor}", 1)
    README_PATH.write_text(updated, encoding="utf-8")


def update_archive(row: str, selection_date: dt.date) -> None:
    existing_rows: list[str] = []
    if ARCHIVE_PATH.exists():
        existing_rows = [
            line
            for line in ARCHIVE_PATH.read_text(encoding="utf-8").splitlines()
            if re.match(r"^\| \d{4}-\d{2}-\d{2} \|", line)
            and not line.startswith(f"| {selection_date.isoformat()} |")
        ]

    rows = sorted([row, *existing_rows], reverse=True)
    lines = [
        "# GitHub of the Day Archive",
        "",
        "Daily random picks from the README GitHub of the Day section.",
        "",
        "Each row keeps the repository link, star count, primary language, site description, and selection query used for retrieval.",
        "",
        "| Date | Repository | Stars | Language | Site Description | Selection Query |",
        "| --- | --- | ---: | --- | --- | --- |",
        *rows,
        "",
    ]
    ARCHIVE_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    selection_date = (
        dt.date.fromisoformat(args.date)
        if args.date
        else get_selection_date()
    )
    repository, query = select_repository(selection_date, args.seed)
    update_readme(render_block(repository, query, selection_date))
    update_archive(archive_row(repository, query, selection_date), selection_date)
    print(f"Updated {README_PATH} GitHub of the Day: {repository['full_name']}")
    print(f"Updated {ARCHIVE_PATH}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
