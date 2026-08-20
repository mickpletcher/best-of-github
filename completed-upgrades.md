# Completed Upgrades

Completed upgrades are moved here from the tracked `future-upgrades.md` backlog. Each completed item should also be represented in [CHANGELOG.md](CHANGELOG.md), and [assessment.md](assessment.md) should be refreshed in the same change.

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
- Made `future-upgrades.md` local-only by removing it from Git tracking and keeping it ignored.
- Added `scripts/validate_weekly_toplist.py` to validate generated Markdown tables, required columns, duplicate repositories, row counts, and source details.
- Added generated timestamp and source query details to the `weeklytoplist.md` footer for easier auditing.

## 2026-06-17

- Renamed the generated weekly top 100 report to `weekly-top-100-github-repositories.md`.
- Added `weekly-top-250-github-repositories.md` for the top 250 public, non-fork, non-archived GitHub repositories.
- Updated the weekly generator, validator, and GitHub Actions workflow to produce and validate both ranking reports.
- Renamed the weekly ranking script, validator, and workflow paths to remove stale `top50` naming.
- Added a dedicated `Mick's Curated GitHub Picks` title in `README.md` for the personal repo list.
- Added `--counts` flags to the weekly ranking generator and validator so top 50, top 100, top 250, and top 500 reports can be generated without code edits.
- Added `micks-watchlist.md` for repos worth monitoring before they belong in the main curated README list.
- Added a README freshness note showing the latest generated weekly scan date.

## 2026-06-29

- Added a README GitHub of the Day section backed by `scripts/update_github_of_the_day.py`.
- Updated the weekly GitHub Actions workflow so the GitHub of the Day block is refreshed automatically.
- Added a daily GitHub of the Day workflow so the README pick changes each day without rerunning weekly rankings.
- Added `github-of-the-day-archive.md` so past daily picks are retained with links, descriptions, and selection queries.
- Added a minimum 3-star eligibility rule for GitHub of the Day picks.

## 2026-08-20

- Added a read-only quality workflow for pull requests and pushes to `main`.
- Added Python compilation and generated-report validation as automated checks.
- Pinned third-party GitHub Actions to immutable release commit SHAs.
- Added Dependabot updates for pinned GitHub Actions dependencies.
- Added shared concurrency control and timeouts to scheduled write workflows.
- Added `SECURITY.md`, `CONTRIBUTING.md`, `CODEOWNERS`, and a pull request template.
- Added structured issue forms for repository suggestions and stale metadata reports.
- Added workflow-status and license badges plus local run instructions to README.
