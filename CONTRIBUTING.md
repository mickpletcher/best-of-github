# Contributing

Thanks for helping improve Best of GitHub.

## Repository Suggestions

Use the repository-suggestion issue form before opening a pull request. Promising projects normally enter [Mick's Watchlist](micks-watchlist.md) before promotion to the main curated catalog.

A useful suggestion explains:

- the project's practical value beyond star count;
- how it fits the catalog's AI, automation, developer-tooling, document, web, media, infrastructure, finance, or security scope;
- whether it has been tested or reviewed;
- its maintenance status and license; and
- any affiliation, sponsorship, referral, or commercial interest.

Source-available software must be described accurately and must not be presented as OSI-approved open source unless its license qualifies.

## Pull Requests

Keep each pull request focused. Do not manually edit generated weekly reports or the automated GitHub of the Day block. Update `CHANGELOG.md` and `assessment.md` when behavior, automation, or project structure changes.

Before submitting:

```powershell
python -m compileall -q scripts
python scripts/validate_weekly_rankings.py
```

The automated quality workflow runs the same checks on pull requests.

## Security

Do not report vulnerabilities in a public issue. Follow [SECURITY.md](SECURITY.md) for private reporting.
