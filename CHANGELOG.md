# Changelog

All notable changes to this repository are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning where practical.

## [Unreleased]

### Added
- Created this changelog to track repository changes.
- Added a weekly GitHub Actions scan that writes the top 100 most-starred public repositories to weeklytoplist.md.
- Added future-upgrades.md with a three-tier backlog of possible repository improvements.
- Added completed-upgrades.md to track implemented upgrades moved out of the future-upgrades backlog.
- Added assessment.md as a quick-reference repository assessment that should be refreshed with every repo change.
- Added README.md references to future-upgrades.md, completed-upgrades.md, assessment.md, and CHANGELOG.md.

### Changed
- Added a .gitignore rule for best-of-github.code-workspace so the workspace file is not committed or pushed.
- Categorized the private initial list and expanded README.md into a public project catalog with links, descriptions, and GitHub star counts.
- Documented the maintenance rule that every repository change should be logged in CHANGELOG.md and reflected in assessment.md.
- Renamed the generated weekly ranking file from WeeklyTop50.md to weeklytoplist.md and updated repository references.

## [2026-06-10]

### Added
- Added .gitignore with an ignore rule for initial-list.md so it is not committed or pushed.

### Changed
- Moved ignore behavior for initial-list.md from local .git/info/exclude to shared .gitignore.
