# Completed Upgrades

Completed upgrades are moved here from [future-upgrades.md](future-upgrades.md). Each completed item should also be represented in [CHANGELOG.md](CHANGELOG.md), and [assessment.md](assessment.md) should be refreshed in the same change.

## 2026-06-12

- Added a weekly GitHub Actions scan that generates `weeklytoplist.md` from the GitHub Search API.
- Expanded the automated weekly report from the top 50 to the top 100 most-starred public, non-fork, non-archived GitHub repositories.
- Added a direct README reference to the generated weekly top 100 list.
- Added upgrade-tracking documentation with future, completed, and assessment files.
- Renamed the generated weekly ranking file from `WeeklyTop50.md` to `weeklytoplist.md`.
- Added category grouping to `weeklytoplist.md` so the top 100 repositories can be scanned by technology area.
- Changed generated repository links in `weeklytoplist.md` to HTML anchors with `target="_blank"` and `rel="noopener noreferrer"` for renderers that support new-tab link attributes.
- Added category summary links in `weeklytoplist.md` so each summary row jumps to its matching category section.
- Added the backlog replenishment rule requiring a new suggested future upgrade whenever an implemented item is moved to completed upgrades.
