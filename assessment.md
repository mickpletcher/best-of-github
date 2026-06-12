# Repository Assessment

Last updated: 2026-06-12

## Quick Reference

Best of GitHub is a documentation-first repository for highlighting useful open-source projects and maintaining an automated weekly ranking of highly starred GitHub repositories.

## Current State

- Primary catalog: [README.md](README.md)
- Automated weekly ranking: [WeeklyTop50.md](WeeklyTop50.md)
- Weekly ranking generator: [scripts/update_weekly_top50.py](scripts/update_weekly_top50.py)
- Scheduled workflow: [.github/workflows/weekly-top50.yml](.github/workflows/weekly-top50.yml)
- Upgrade backlog: [future-upgrades.md](future-upgrades.md)
- Completed upgrades: [completed-upgrades.md](completed-upgrades.md)
- Change history: [CHANGELOG.md](CHANGELOG.md)

## Strengths

- The repo is simple and easy to understand.
- The weekly ranking is automated and can also be run manually through GitHub Actions.
- The generator uses the GitHub API directly with Python standard library dependencies only.
- Upgrade planning, completed work, and repo assessment now have dedicated reference files.

## Risks and Gaps

- `WeeklyTop50.md` now contains a top 100 list, so the filename no longer matches the report size.
- There are no automated tests for the report generator.
- The curated README catalog and generated weekly report use separate update paths.
- Historical weekly snapshots are not retained.

## Maintenance Rules

- Update this assessment whenever the repository changes.
- Log every repository change in [CHANGELOG.md](CHANGELOG.md).
- When an item from [future-upgrades.md](future-upgrades.md) is implemented, move it to [completed-upgrades.md](completed-upgrades.md).
- Keep README references current when new key files or workflows are added.
