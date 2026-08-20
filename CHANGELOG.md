# Changelog

All notable changes to this repository are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning where practical.

## [Unreleased]

### Added
- Created this changelog to track repository changes.
- Added chopratejas/headroom to the README.md AI coding agents, skills, and plugins catalog.
- Added mvanhorn/last30days-skill to the README.md AI coding agents, skills, and plugins catalog.
- Added a weekly GitHub Actions scan that writes the top 100 most-starred public repositories to weeklytoplist.md.
- Added weekly-top-250-github-repositories.md for the top 250 most-starred public repositories.
- Added future-upgrades.md with a three-tier backlog of possible repository improvements.
- Added completed-upgrades.md to track implemented upgrades moved out of the future-upgrades backlog.
- Added assessment.md as a quick-reference repository assessment that should be refreshed with every repo change.
- Added README.md references to future-upgrades.md, completed-upgrades.md, assessment.md, and CHANGELOG.md.
- Added category grouping to weeklytoplist.md so the top 100 repositories are easier to scan by technology area.
- Added category summary links in weeklytoplist.md so each summary row jumps to its matching category section.
- Added a backlog replenishment rule to future-upgrades.md so implemented items are replaced with new suggested upgrades.
- Added scripts/validate_weekly_toplist.py to validate generated report row counts, duplicate repositories, table structure, required columns, and source details.
- Added source query details and a generated timestamp to the weeklytoplist.md report footer.
- Added a dedicated Mick's Curated GitHub Picks section title to README.md for the personal repo list.
- Added `--counts` flags to `scripts/update_weekly_rankings.py` and `scripts/validate_weekly_rankings.py` for top 50, top 100, top 250, and top 500 report sizes.
- Added `micks-watchlist.md` for repos worth monitoring before they are promoted to the main curated README list.
- Added a README freshness note showing the latest generated weekly scan date.
- Added a README GitHub of the Day section and `scripts/update_github_of_the_day.py` to select a random public repository.
- Added a daily GitHub of the Day workflow to refresh the README pick without rerunning weekly rankings.
- Added `github-of-the-day-archive.md` to retain daily picks with links, descriptions, and selection queries.

### Changed
- Replaced Mick's curated README catalog with all 41 public repositories starred by `mickpletcher` as of 2026-08-20 and refreshed their star counts.
- Added a .gitignore rule for best-of-github.code-workspace so the workspace file is not committed or pushed.
- Categorized the private initial list and expanded README.md into a public project catalog with links, descriptions, and GitHub star counts.
- Documented the maintenance rule that every repository change should be logged in CHANGELOG.md and reflected in assessment.md.
- Renamed the generated weekly ranking file from WeeklyTop50.md to weeklytoplist.md and updated repository references.
- Renamed the generated weekly top 100 report from weeklytoplist.md to weekly-top-100-github-repositories.md.
- Renamed the weekly ranking generator, validator, and workflow paths to remove stale top50 naming.
- Changed generated repository links in weeklytoplist.md to HTML anchors with target="_blank" and rel="noopener noreferrer" for renderers that support new-tab link attributes.
- Updated README.md, completed-upgrades.md, and assessment.md to reflect the future-upgrades replenishment process.
- Removed future-upgrades.md from Git tracking so the future backlog remains local to the laptop.
- Updated README.md, completed-upgrades.md, and assessment.md to describe future-upgrades.md as a local-only file.
- Updated the weekly GitHub Actions workflow to validate weeklytoplist.md after generation.
- Updated the weekly GitHub Actions workflow to generate, validate, and commit both weekly ranking reports.
- Updated repository docs to describe `future-upgrades.md` as a tracked backlog.
- Updated README.md, completed-upgrades.md, future-upgrades.md, and assessment.md to reflect the new watchlist workflow.
- Updated the weekly ranking generator, validator, and workflow so the README freshness note stays aligned with generated report dates.
- Updated the weekly GitHub Actions workflow to refresh the GitHub of the Day block.
- Updated the GitHub of the Day updater and workflows to maintain the archive file.
- Changed the GitHub of the Day selector to require at least 3 stars.

## [2026-06-10]

### Added
- Added .gitignore with an ignore rule for initial-list.md so it is not committed or pushed.

### Changed
- Moved ignore behavior for initial-list.md from local .git/info/exclude to shared .gitignore.
