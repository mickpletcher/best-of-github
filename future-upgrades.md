# Future Upgrades

Tracked repo backlog for planned improvements.

This file tracks planned improvements. When an upgrade is implemented, move it from this file to [completed-upgrades.md](completed-upgrades.md), add a new suggested upgrade to replace it in the appropriate tier, add a matching entry to [CHANGELOG.md](CHANGELOG.md), and refresh [assessment.md](assessment.md).

## Backlog Maintenance

- Keep each tier replenished by adding a new suggested upgrade whenever an item is implemented and moved out of this file.
- Add replacement suggestions to the tier that best matches their value, complexity, and timing.
- Keep replacement suggestions specific enough that they can be implemented without rediscovering the original intent.

## Tier 1: High-Value, Low-Complexity

- Add a README table of contents once the project documentation grows beyond the current quick-reference sections.
- Add a short "how to run locally" section to README.md for regenerating and validating both weekly ranking reports.
- Add a workflow_dispatch input for report counts so GitHub Actions can generate top 50, top 100, top 250, or top 500 reports from the Actions UI.
- Add a README note explaining that the latest weekly scan date is refreshed automatically by the ranking generator.

## Tier 2: Better Discovery and Filtering

- Track week-over-week rank changes so the weekly reports can show movers, new entries, and dropped repositories.
- Add optional filters for minimum stars, primary language, repository topic, and organization allow/block lists.
- Create a compact summary section at the top of each weekly report with total repositories scanned, top languages, and notable new entries.
- Add a watchlist review cadence section so candidates have clear keep, promote, or remove decisions after each monthly review.

## Tier 3: Automation, Quality, and Publishing

- Publish the weekly reports through GitHub Pages with searchable and sortable tables.
- Store historical weekly snapshots so trends can be reviewed over time instead of only keeping the latest generated list.
- Add tests for the GitHub API parsing and Markdown rendering logic with fixture data.
- Add issue templates for suggesting repositories, reporting stale metadata, and proposing future upgrade items.
- Add a scheduled stale-link audit that checks README links and generated report links for deleted, archived, or renamed repositories.
