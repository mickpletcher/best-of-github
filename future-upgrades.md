# Future Upgrades

This file tracks planned improvements. When an upgrade is implemented, move it from this file to [completed-upgrades.md](completed-upgrades.md), add a matching entry to [CHANGELOG.md](CHANGELOG.md), and refresh [assessment.md](assessment.md).

## Tier 1: High-Value, Low-Complexity

- Add a small validation script that checks generated Markdown tables for row count, duplicate repositories, broken table formatting, and missing required columns.
- Add a generated timestamp and source query details to the weekly report footer for easier auditing.
- Add a README table of contents once the project documentation grows beyond the current quick-reference sections.

## Tier 2: Better Discovery and Filtering

- Add topic-based weekly lists for AI, developer tools, security, data, automation, and learning repositories.
- Track week-over-week rank changes so the weekly report can show movers, new entries, and dropped repositories.
- Add optional filters for minimum stars, primary language, repository topic, and organization allow/block lists.
- Create a compact summary section at the top of the weekly report with total repositories scanned, top languages, and notable new entries.

## Tier 3: Automation, Quality, and Publishing

- Publish the weekly report through GitHub Pages with searchable and sortable tables.
- Store historical weekly snapshots so trends can be reviewed over time instead of only keeping the latest generated list.
- Add tests for the GitHub API parsing and Markdown rendering logic with fixture data.
- Add issue templates for suggesting repositories, reporting stale metadata, and proposing future upgrade items.
