# Repository Assessment

Last updated: 2026-06-17

## Quick Reference

Best of GitHub is a documentation-first repository for highlighting Mick's curated open-source project picks and maintaining automated weekly rankings of highly starred GitHub repositories.

## Current State

- Primary catalog: [README.md](README.md), currently listing 16 personal curated picks across five topic sections.
- Watchlist: [micks-watchlist.md](micks-watchlist.md), used for promising repos that need more review before README promotion.
- Automated weekly top 100 ranking: [weekly-top-100-github-repositories.md](weekly-top-100-github-repositories.md)
- Automated weekly top 250 ranking: [weekly-top-250-github-repositories.md](weekly-top-250-github-repositories.md)
- Weekly ranking generator: [scripts/update_weekly_rankings.py](scripts/update_weekly_rankings.py)
- Weekly report validator: [scripts/validate_weekly_rankings.py](scripts/validate_weekly_rankings.py)
- README freshness note: `Latest weekly scan: 2026-06-17.`
- Scheduled workflow: [.github/workflows/weekly-github-rankings.yml](.github/workflows/weekly-github-rankings.yml)
- Upgrade backlog: [future-upgrades.md](future-upgrades.md)
- Completed upgrades: [completed-upgrades.md](completed-upgrades.md)
- Change history: [CHANGELOG.md](CHANGELOG.md)

## Strengths

- The repo is simple and easy to understand.
- The weekly rankings are automated and can also be run manually through GitHub Actions.
- The generator uses the GitHub API directly with Python standard library dependencies only.
- The generator and validator accept `--counts` for top 50, top 100, top 250, and top 500 reports.
- Upgrade planning, completed work, and repo assessment now have dedicated reference files.
- The weekly reports are grouped into practical technology categories while preserving each repository's overall star rank.
- The weekly report category summaries link directly to each generated category section.
- Future upgrade planning is tracked with the repo so backlog rules are visible in VSCode and Git.
- Generated weekly reports include source query details and are checked by a validation script.
- README shows the latest generated weekly scan date and the validator checks it against the reports.
- The README separates Mick's personal curated picks from automated star-count rankings.
- The watchlist gives promising repos a place to sit before they are promoted or removed.

## Risks and Gaps

- There are no fixture-based unit tests for the report generator or validator.
- The curated README catalog and generated weekly report use separate update paths.
- Historical weekly snapshots are not retained.
- GitHub Markdown may not honor `target="_blank"` link behavior even though the generated links include that attribute for compatible renderers.

## Maintenance Rules

- Update this assessment whenever the repository changes.
- Log every repository change in [CHANGELOG.md](CHANGELOG.md).
- When an item from [future-upgrades.md](future-upgrades.md) is implemented, move it to [completed-upgrades.md](completed-upgrades.md).
- Replace each implemented future-upgrades item with a new suggested upgrade in the appropriate tier.
- Keep README references current when new key files or workflows are added.
