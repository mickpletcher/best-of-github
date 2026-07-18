# Best of GitHub

Best of GitHub is Mick's curated catalog of standout open-source projects for AI engineering, coding agents, document processing, web automation, media tooling, and security. It highlights practical repositories worth exploring, with current star counts and short notes explaining why each project is useful or interesting.

Star counts were refreshed on 2026-06-10.

For the current automated rankings, see the weekly top 100 and weekly top 250 reports below.

Latest weekly scan: 2026-07-13.

## GitHub of the Day

<!-- github-of-the-day:start -->
Selected for 2026-07-18 from public, non-fork, non-archived repositories with recent activity. This is random and is not based on popularity.

| Repository | Stars | Language | Notes |
| --- | ---: | --- | --- |
| [eXtremeProgramming-cn/pomasa](https://github.com/eXtremeProgramming-cn/pomasa) | 47 | Shell | Patterns of Multi-Agent System Architecture |

Selection query: `stars:3..50 fork:false archived:false is:public pushed:>=2025-07-18 language:Shell`
<!-- github-of-the-day:end -->

Past picks are saved in the [GitHub of the Day Archive](github-of-the-day-archive.md). Repositories need at least 3 stars to be eligible.

## Project References

- [Future upgrades](future-upgrades.md): planned improvements that should be moved to completed upgrades when implemented.
- [GitHub of the Day Archive](github-of-the-day-archive.md): daily random picks with links, descriptions, and selection queries.
- [Mick's Watchlist](micks-watchlist.md): repos worth monitoring before they belong in the main curated README list.
- [Completed upgrades](completed-upgrades.md): implemented improvements moved out of the future-upgrades backlog.
- [Repository assessment](assessment.md): a quick-reference assessment that is updated whenever the repo changes.
- [Changelog](CHANGELOG.md): every repository change should be logged here.

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

## Mick's Curated GitHub Picks

These are repositories I personally like enough to keep on the main README. They are selected for practical value, not just star count.

Repos that look promising but still need testing or review live in [Mick's Watchlist](micks-watchlist.md).

### AI Coding Agents, Skills, and Plugins

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 56,259 | Turns codebases into interactive knowledge graphs that can be explored, searched, and queried with AI coding tools. |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 46,419 | Builds local, pre-indexed code knowledge graphs for AI coding agents to reduce context and tool-call overhead. |
| [chopratejas/headroom](https://github.com/chopratejas/headroom) | 24,950 | Compresses tool outputs, logs, files, and RAG chunks before they reach the LLM to reduce token usage. |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | 9,795 | A compact skill file for removing obvious AI tells from generated prose. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 40,495 | AI agent skill for researching recent discussion across Reddit, X, YouTube, HN, Polymarket, and the web. |
| [cursor/plugins](https://github.com/cursor/plugins) | 1,916 | Cursor's plugin specification and official plugin examples. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 20,833 | Official Compound Engineering plugin for Claude Code, Codex, Cursor, and similar agentic coding environments. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 212,236 | Agent harness optimization system covering skills, instincts, memory, security, and research-first development. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 50,086 | Production-grade engineering skills for AI coding agents. |

### AI Engineering and Learning

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) | 30,891 | A hands-on AI engineering learning path that emphasizes building and shipping systems from scratch. |

### Document and Content Processing

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 149,768 | Converts files and Office documents into Markdown for downstream AI and automation workflows. |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | 9,777 | Fast open-source document parser for OCR, PDF parsing, and text extraction. |

### Web Automation, Scraping, and Media

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [microsoft/Webwright](https://github.com/microsoft/Webwright) | 5,282 | Browser-agent framework for long-horizon web tasks. |
| [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) | 62,613 | Adaptive web scraping framework that scales from single requests to full crawls. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 169,586 | Feature-rich command-line audio and video downloader. |

### Cybersecurity and Agent Security

| Project | Stars | Why It Is Interesting |
| --- | ---: | --- |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 15,104 | Large collection of structured cybersecurity skills for AI agents, mapped to major security frameworks. |
