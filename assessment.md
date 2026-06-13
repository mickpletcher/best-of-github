# Repository Assessment

Last updated: 2026-06-12

## Quick Reference

Best of GitHub is a documentation-first repository for highlighting useful open-source projects and maintaining an automated weekly ranking of highly starred GitHub repositories.

## Current State

- Primary catalog: [README.md](README.md), currently listing 15 curated projects across five topic sections.
- Automated weekly ranking: [weeklytoplist.md](weeklytoplist.md)
- Weekly ranking generator: [scripts/update_weekly_top50.py](scripts/update_weekly_top50.py)
- Weekly report validator: [scripts/validate_weekly_toplist.py](scripts/validate_weekly_toplist.py)
- Scheduled workflow: [.github/workflows/weekly-top50.yml](.github/workflows/weekly-top50.yml)
- Local upgrade backlog: `future-upgrades.md` is ignored by Git and kept only on this laptop.
- Completed upgrades: [completed-upgrades.md](completed-upgrades.md)
- Change history: [CHANGELOG.md](CHANGELOG.md)

## Strengths

- The repo is simple and easy to understand.
- The weekly ranking is automated and can also be run manually through GitHub Actions.
- The generator uses the GitHub API directly with Python standard library dependencies only.
- Upgrade planning, completed work, and repo assessment now have dedicated reference files.
- The weekly report is grouped into practical technology categories while preserving each repository's overall star rank.
- The weekly report category summary links directly to each generated category section.
- Future upgrade planning remains available locally without publishing the backlog to GitHub.
- Generated weekly reports now include source query details and are checked by a validation script.

## Risks and Gaps

- The weekly workflow and script names still include `top50`, even though the generated report now contains the top 100 repositories.
- There are no fixture-based unit tests for the report generator or validator.
- The curated README catalog and generated weekly report use separate update paths.
- Historical weekly snapshots are not retained.
- GitHub Markdown may not honor `target="_blank"` link behavior even though the generated links include that attribute for compatible renderers.

## Maintenance Rules

- Update this assessment whenever the repository changes.
- Log every repository change in [CHANGELOG.md](CHANGELOG.md).
- When an item from local-only `future-upgrades.md` is implemented, move it to [completed-upgrades.md](completed-upgrades.md).
- Replace each implemented future-upgrades item with a new suggested upgrade in the appropriate tier.
- Keep README references current when new key files or workflows are added.
