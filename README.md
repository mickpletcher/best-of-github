# Best of GitHub

[![Quality](https://github.com/mickpletcher/best-of-github/actions/workflows/quality.yml/badge.svg)](https://github.com/mickpletcher/best-of-github/actions/workflows/quality.yml)
[![GitHub of the Day](https://github.com/mickpletcher/best-of-github/actions/workflows/github-of-the-day.yml/badge.svg)](https://github.com/mickpletcher/best-of-github/actions/workflows/github-of-the-day.yml)
[![Weekly Rankings](https://github.com/mickpletcher/best-of-github/actions/workflows/weekly-github-rankings.yml/badge.svg)](https://github.com/mickpletcher/best-of-github/actions/workflows/weekly-github-rankings.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Best of GitHub is Mick's curated catalog of standout public repositories for AI engineering, coding agents, document processing, web automation, media tooling, and security. It highlights practical repositories worth exploring, with current star counts and short notes explaining why each project is useful or interesting.

Star counts were refreshed on 2026-08-20.

For the current automated rankings, see the weekly top 100 and weekly top 250 reports below.

Latest weekly scan: 2026-08-17.

## GitHub of the Day

<!-- github-of-the-day:start -->
Selected for 2026-08-22 from public, non-fork, non-archived repositories with recent activity. This is random and is not based on popularity.

| Repository | Stars | Language | Notes |
| --- | ---: | --- | --- |
| [solana-program/token](https://github.com/solana-program/token) | 187 | Rust | The SPL Token program and its clients |

Selection query: `stars:51..250 fork:false archived:false is:public pushed:>=2025-08-22 language:Rust`
<!-- github-of-the-day:end -->

Past picks are saved in the [GitHub of the Day Archive](github-of-the-day-archive.md). Repositories need at least 3 stars to be eligible.

## Project References

- [Future upgrades](future-upgrades.md): planned improvements that should be moved to completed upgrades when implemented.
- [GitHub of the Day Archive](github-of-the-day-archive.md): daily random picks with links, descriptions, and selection queries.
- [Mick's Watchlist](micks-watchlist.md): repos worth monitoring before they belong in the main curated README list.
- [Completed upgrades](completed-upgrades.md): implemented improvements moved out of the future-upgrades backlog.
- [Repository assessment](assessment.md): a quick-reference assessment that is updated whenever the repo changes.
- [Changelog](CHANGELOG.md): every repository change should be logged here.
- [Contributing](CONTRIBUTING.md): suggestion criteria, validation steps, and disclosure expectations.
- [Security policy](SECURITY.md): private vulnerability-reporting guidance.

## Weekly Rankings

The automated weekly scan writes two ranking files:

| Report | Repository Count | File |
| --- | ---: | --- |
| Weekly Top 100 GitHub Repositories | 100 | [weekly-top-100-github-repositories.md](weekly-top-100-github-repositories.md) |
| Weekly Top 250 GitHub Repositories | 250 | [weekly-top-250-github-repositories.md](weekly-top-250-github-repositories.md) |

Both files list public, non-fork, non-archived GitHub repositories sorted by star count and grouped by technology category. The scheduled GitHub Actions workflow refreshes both reports every Monday. The generated reports include source query details and are validated by [scripts/validate_weekly_rankings.py](scripts/validate_weekly_rankings.py).

The separate GitHub of the Day workflow refreshes the README pick daily.

The generator and validator also support custom report counts:

```powershell
python scripts/update_weekly_rankings.py --counts 50 100 250 500
python scripts/validate_weekly_rankings.py --counts 50 100 250 500
```

Refresh the GitHub of the Day block:

```powershell
python scripts/update_github_of_the_day.py
```

## Run Locally

Python 3.10 or newer is required. The scripts use only the Python standard library.

Validate the current repository state:

```powershell
python -m compileall -q scripts
python scripts/validate_weekly_rankings.py
```

Regenerate the weekly reports and daily pick:

```powershell
python scripts/update_weekly_rankings.py --counts 100 250
python scripts/update_github_of_the_day.py
python scripts/validate_weekly_rankings.py
```

Unauthenticated GitHub API requests are rate-limited. For local authenticated runs, provide a token through `GH_TOKEN` or `GITHUB_TOKEN` in the environment and never commit it.

## Mick's Curated GitHub Picks

These are the 41 public repositories starred by [mickpletcher](https://github.com/mickpletcher) as of 2026-08-20. They are selected for practical value, not just star count.

Repos that look promising but still need testing or review live in [Mick's Watchlist](micks-watchlist.md).

### AI Coding Agents, Skills, and Developer Tools

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 88,798 | Provides production-grade engineering skills for AI coding agents. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 241,400 | Covers agent harness optimization through skills, memory, security, and research-first workflows. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 24,403 | Implements the Compound Engineering workflow for Claude Code, Codex, Cursor, and other coding agents. |
| [cursor/plugins](https://github.com/cursor/plugins) | 3,999 | Defines Cursor's plugin specification and provides its official plugins. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 58,802 | Researches recent discussion across social, video, prediction-market, and web sources. |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | 67,002 | Compresses agent tool output, logs, files, and RAG content to reduce token use while preserving answers. |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 67,362 | Builds a local code knowledge graph that stays synchronized for coding agents. |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 79,924 | Turns codebases into interactive knowledge graphs that can be explored, searched, and queried. |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | 16,006 | Provides a compact agent skill for removing obvious AI tells from prose. |
| [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) | 74,281 | Converts screenshots into HTML, Tailwind, React, or Vue implementations. |
| [elvisun/newsjack](https://github.com/elvisun/newsjack) | 630 | Supplies agent skills that model a full pull request team. |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | 75,396 | Provides practical examples and guides for building with the OpenAI API. |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 57,393 | Orchestrates role-based autonomous agents for collaborative workflows. |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 142,123 | Runs an agentic coding workflow from the terminal with codebase and Git support. |
| [openai/codex](https://github.com/openai/codex) | 107,096 | Provides a lightweight open-source coding agent for terminal workflows. |

### AI Engineering, Local Models, and Research

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 47,345 | Provides a hands-on path for learning, building, and shipping AI systems. |
| [alexziskind1/llm-inference-calculator](https://github.com/alexziskind1/llm-inference-calculator) | 316 | Helps estimate hardware and resource requirements for local LLM inference. |
| [paperswithcode/paperswithcode-data](https://github.com/paperswithcode/paperswithcode-data) | 934 | Publishes the dataset behind Papers with Code for local analysis and research. |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 64,979 | Provides a local-first AI workspace with agents, document chat, and model integrations. |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 149,374 | Offers a self-hosted interface for Ollama, OpenAI-compatible APIs, and other models. |
| [ollama/ollama](https://github.com/ollama/ollama) | 179,049 | Simplifies running and managing language models locally. |
| [lmstudio-ai/lmstudio-bug-tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker) | 149 | Tracks bugs and product issues for the LM Studio desktop application. |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 74,066 | Supports local model training and inference through an integrated UI. |

### Document Processing, Web Automation, and Media

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 174,905 | Converts files and Office documents into Markdown for AI and automation workflows. |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | 12,140 | Provides fast open-source document parsing and text extraction. |
| [microsoft/Webwright](https://github.com/microsoft/Webwright) | 5,931 | Implements a software-engineering-style browser agent for long-running web tasks. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 75,517 | Scales adaptive web scraping from single requests to complete crawls. |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 94,818 | Automates Chromium, Firefox, and WebKit for testing and browser workflows. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 185,851 | Provides a feature-rich command-line audio and video downloader. |
| [shanselman/TinyToolTown](https://github.com/shanselman/TinyToolTown) | 255 | Collects small, focused, open-source utilities built for specific needs. |
| [bradautomates/claude-video](https://github.com/bradautomates/claude-video) | 15,899 | Downloads, samples, and transcribes videos so Claude can analyze them. |

### Automation, Infrastructure, and Home Lab

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [smart-underworld/seestar_alp](https://github.com/smart-underworld/seestar_alp) | 285 | Adds complete control and automation for the Seestar S50 telescope. |
| [espressif/arduino-esp32](https://github.com/espressif/arduino-esp32) | 17,260 | Brings the Arduino platform to the ESP32 family of microcontrollers. |
| [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole) | 60,504 | Provides network-wide DNS filtering for ads and unwanted domains. |
| [tailscale/tailscale](https://github.com/tailscale/tailscale) | 35,397 | Builds secure private networks on WireGuard with simple identity-based access. |
| [home-assistant/core](https://github.com/home-assistant/core) | 90,011 | Provides privacy-focused home automation with local control. |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 201,361 | Combines visual workflow automation, code, AI features, and self-hosting. |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | 55,018 | Provides the cross-platform PowerShell automation runtime and shell. |

### Finance and Market Data

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [trendsmcp-ai/news-sentiment-mcp](https://github.com/trendsmcp-ai/news-sentiment-mcp) | 1 | Exposes live news sentiment and coverage volume through MCP. |
| [risabhmishra/algotrading-sentimentanalysis-genai](https://github.com/risabhmishra/algotrading-sentimentanalysis-genai) | 24 | Explores algorithmic trading with news sentiment analysis and generative AI. |

### Cybersecurity and Agent Security

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 30,313 | Provides structured cybersecurity skills mapped to major defensive, offensive, fraud, and AI security frameworks. |
