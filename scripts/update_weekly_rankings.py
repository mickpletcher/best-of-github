#!/usr/bin/env python3
"""Generate weekly GitHub ranking reports."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
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
DEFAULT_REPORT_COUNTS = [100, 250]
ALLOWED_REPORT_COUNTS = [50, 100, 250, 500]
MAX_PER_PAGE = 100
SEARCH_QUERY = "stars:>1 fork:false archived:false"
SEARCH_SORT = "stars"
SEARCH_ORDER = "desc"
GITHUB_API_VERSION = "2022-11-28"

CATEGORY_ORDER = [
    "AI and Machine Learning",
    "Developer Tools and Frameworks",
    "Learning and Reference",
    "Web and Application Development",
    "Infrastructure and DevOps",
    "Security and Privacy",
    "Media and Content Tools",
    "Systems, Languages, and Runtimes",
    "Productivity and Utilities",
    "Other",
]

CATEGORY_RULES = {
    "AI and Machine Learning": [
        "ai",
        "artificial intelligence",
        "agent",
        "chatgpt",
        "claude",
        "comfyui",
        "diffusion",
        "generative",
        "llama",
        "llm",
        "machine learning",
        "ml",
        "neural",
        "ollama",
        "prompt",
        "rag",
        "stable diffusion",
        "tensorflow",
        "transformer",
    ],
    "Developer Tools and Frameworks": [
        "api",
        "automation",
        "bootstrap",
        "coding",
        "component",
        "developer",
        "framework",
        "gitignore",
        "interview",
        "library",
        "n8n",
        "opencode",
        "react",
        "sdk",
        "tool",
        "ui",
        "visual studio code",
        "vscode",
        "workflow",
    ],
    "Learning and Reference": [
        "algorithm",
        "awesome",
        "book",
        "computer science",
        "course",
        "curriculum",
        "education",
        "free programming books",
        "guide",
        "handbook",
        "interview",
        "learning",
        "notes",
        "primer",
        "project based",
        "roadmap",
        "tutorial",
    ],
    "Web and Application Development": [
        "android",
        "angular",
        "app",
        "css",
        "electron",
        "flutter",
        "html",
        "javascript",
        "mobile",
        "node",
        "react native",
        "tauri",
        "typescript",
        "vue",
        "web",
    ],
    "Infrastructure and DevOps": [
        "cloud",
        "container",
        "devops",
        "docker",
        "free for dev",
        "infrastructure",
        "kubernetes",
        "proxy",
        "selfhosted",
        "server",
        "workflow automation",
    ],
    "Security and Privacy": [
        "activation",
        "hacking",
        "infosec",
        "privacy",
        "proxy",
        "security",
        "vpn",
    ],
    "Media and Content Tools": [
        "audio",
        "content",
        "document",
        "download",
        "markdown",
        "media",
        "office",
        "pdf",
        "video",
        "youtube",
    ],
    "Systems, Languages, and Runtimes": [
        "c++",
        "compiler",
        "deno",
        "go",
        "kernel",
        "language",
        "linux",
        "node.js",
        "runtime",
        "rust",
        "swift",
        "vim",
    ],
    "Productivity and Utilities": [
        "command line",
        "desktop",
        "mac",
        "powertoys",
        "productivity",
        "remote desktop",
        "shell",
        "terminal",
        "utility",
        "windows",
        "zsh",
    ],
}


def get_scan_date() -> str:
    return get_scan_datetime().date().isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate weekly GitHub ranking reports.")
    parser.add_argument(
        "--counts",
        nargs="+",
        type=int,
        choices=ALLOWED_REPORT_COUNTS,
        default=DEFAULT_REPORT_COUNTS,
        metavar="COUNT",
        help="Report sizes to generate. Allowed values: 50, 100, 250, 500.",
    )
    return parser.parse_args()


def output_path_for_count(repository_count: int) -> Path:
    return Path(f"weekly-top-{repository_count}-github-repositories.md")


def get_scan_datetime() -> dt.datetime:
    timezone_name = os.environ.get("SCAN_TIMEZONE", "America/Chicago")
    if ZoneInfo is None:
        return dt.datetime.now(dt.timezone.utc)
    return dt.datetime.now(ZoneInfo(timezone_name))


def build_query_params(repository_count: int, page: int = 1) -> dict[str, str]:
    return {
        "q": SEARCH_QUERY,
        "sort": SEARCH_SORT,
        "order": SEARCH_ORDER,
        "per_page": str(min(repository_count, MAX_PER_PAGE)),
        "page": str(page),
    }


def build_search_url(repository_count: int, page: int = 1) -> str:
    return f"{GITHUB_SEARCH_URL}?{urllib.parse.urlencode(build_query_params(repository_count, page))}"


def fetch_top_repositories(repository_count: int) -> list[dict]:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"best-of-github-weekly-top{repository_count}",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repositories: list[dict] = []
    seen_repository_names: set[str] = set()
    page = 1
    per_page = min(repository_count, MAX_PER_PAGE)
    while len(repositories) < repository_count:
        url = build_search_url(per_page, page)
        request = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitHub API request failed: {error.code} {body}") from error
        except urllib.error.URLError as error:
            raise RuntimeError(f"GitHub API request failed: {error.reason}") from error

        items = payload.get("items", [])
        if not items:
            break

        for repository in items:
            full_name = repository.get("full_name")
            if full_name in seen_repository_names:
                continue
            seen_repository_names.add(full_name)
            repositories.append(repository)
            if len(repositories) == repository_count:
                break

        page += 1

    if len(repositories) < repository_count:
        raise RuntimeError(f"Expected {repository_count} repositories, got {len(repositories)}")
    return repositories[:repository_count]


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


def repository_link(repository: dict) -> str:
    full_name = html.escape(repository["full_name"], quote=True)
    html_url = html.escape(repository["html_url"], quote=True)
    return (
        f'<a href="{html_url}" target="_blank" rel="noopener noreferrer">'
        f"{full_name}</a>"
    )


def classify_repository(repository: dict) -> str:
    topics = " ".join(repository.get("topics") or [])
    searchable = " ".join(
        [
            repository.get("full_name", ""),
            repository.get("name", ""),
            repository.get("description") or "",
            repository.get("language") or "",
            topics,
        ]
    ).lower()

    for category in CATEGORY_ORDER:
        if category == "Other":
            continue
        if any(keyword_matches(searchable, keyword) for keyword in CATEGORY_RULES[category]):
            return category
    return "Other"


def keyword_matches(searchable: str, keyword: str) -> bool:
    if len(keyword) <= 3 and keyword.isalnum():
        return re.search(rf"(?<![a-z0-9]){re.escape(keyword)}(?![a-z0-9])", searchable) is not None
    return keyword in searchable


def heading_anchor(value: str) -> str:
    anchor = re.sub(r"[^a-z0-9 -]", "", value.lower())
    return re.sub(r"\s+", "-", anchor.strip())


def group_repositories(repositories: list[dict]) -> dict[str, list[tuple[int, dict]]]:
    grouped = {category: [] for category in CATEGORY_ORDER}
    for rank, repository in enumerate(repositories, start=1):
        grouped[classify_repository(repository)].append((rank, repository))
    return grouped


def render_markdown(repositories: list[dict], repository_count: int) -> str:
    grouped = group_repositories(repositories)
    scan_datetime = get_scan_datetime()
    query_params = build_query_params(repository_count)
    lines = [
        f"# Weekly Top {repository_count} GitHub Repositories",
        "",
        f"Scanned on {scan_datetime.date().isoformat()}.",
        "",
        f"This weekly report lists the top {repository_count} public, non-fork, non-archived GitHub repositories sorted by star count and grouped into practical technology categories. The list is generated from the GitHub Search API.",
        "",
        "Repository links are emitted as HTML anchors with `target=\"_blank\"` for Markdown renderers that honor new-tab link attributes.",
        "",
        "## Category Summary",
        "",
        "| Category | Count |",
        "| --- | ---: |",
    ]

    for category in CATEGORY_ORDER:
        count = len(grouped[category])
        if count:
            lines.append(f"| [{category}](#{heading_anchor(category)}) | {count} |")

    for category in CATEGORY_ORDER:
        repositories_in_category = grouped[category]
        if not repositories_in_category:
            continue

        lines.extend(
            [
                "",
                f"## {category}",
                "",
                "| Rank | Repository | Stars | Language | Description |",
                "| ---: | --- | ---: | --- | --- |",
            ]
        )

        for rank, repository in repositories_in_category:
            stars = f"{repository['stargazers_count']:,}"
            language = markdown_escape(repository.get("language"))
            description = markdown_escape(repository.get("description"))
            lines.append(
                f"| {rank} | {repository_link(repository)} | {stars} | {language} | {description} |"
            )

    lines.extend(
        [
            "",
            "## Source Details",
            "",
            f"- Generated at: {scan_datetime.isoformat(timespec='seconds')}",
            f"- GitHub API endpoint: `{GITHUB_SEARCH_URL}`",
            f"- Search query: `{query_params['q']}`",
            f"- Sort: `{query_params['sort']}`",
            f"- Order: `{query_params['order']}`",
            f"- Requested repository count: `{repository_count}`",
            f"- GitHub API version: `{GITHUB_API_VERSION}`",
            "",
            "<!-- This file is generated by scripts/update_weekly_rankings.py. -->",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    report_counts = sorted(set(args.counts))
    max_repository_count = max(report_counts)
    repositories = fetch_top_repositories(max_repository_count)
    for repository_count in report_counts:
        report_repositories = repositories[:repository_count]
        output_path = output_path_for_count(repository_count)
        output_path.write_text(
            render_markdown(report_repositories, repository_count),
            encoding="utf-8",
        )
        print(f"Wrote {output_path} with {len(report_repositories)} repositories.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
