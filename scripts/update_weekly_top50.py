#!/usr/bin/env python3
"""Generate weeklytoplist.md from GitHub's most-starred public repositories."""

from __future__ import annotations

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
OUTPUT_PATH = Path("weeklytoplist.md")
TOP_N = 100

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
    timezone_name = os.environ.get("SCAN_TIMEZONE", "America/Chicago")
    if ZoneInfo is None:
        now = dt.datetime.now(dt.timezone.utc)
    else:
        now = dt.datetime.now(ZoneInfo(timezone_name))
    return now.date().isoformat()


def fetch_top_repositories() -> list[dict]:
    query = {
        "q": "stars:>1 fork:false archived:false",
        "sort": "stars",
        "order": "desc",
        "per_page": str(TOP_N),
    }
    url = f"{GITHUB_SEARCH_URL}?{urllib.parse.urlencode(query)}"
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "best-of-github-weekly-top50",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {error.code} {body}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub API request failed: {error.reason}") from error

    repositories = payload.get("items", [])
    if len(repositories) < TOP_N:
        raise RuntimeError(f"Expected {TOP_N} repositories, got {len(repositories)}")
    return repositories[:TOP_N]


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


def render_markdown(repositories: list[dict]) -> str:
    grouped = group_repositories(repositories)
    lines = [
        "# Weekly Top 100 GitHub Repositories",
        "",
        f"Scanned on {get_scan_date()}.",
        "",
        "This weekly report lists the top 100 public, non-fork, non-archived GitHub repositories sorted by star count and grouped into practical technology categories. The list is generated from the GitHub Search API.",
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
            "<!-- This file is generated by scripts/update_weekly_top50.py. -->",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    repositories = fetch_top_repositories()
    OUTPUT_PATH.write_text(render_markdown(repositories), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {len(repositories)} repositories.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
