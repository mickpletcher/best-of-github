# Contributing

Thanks for helping improve Best of GitHub. Follow the [code of conduct](CODE_OF_CONDUCT.md) in project spaces. See [SUPPORT.md](SUPPORT.md) for reporting routes and questions.

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

## Accessibility

Follow [ACCESSIBILITY.md](ACCESSIBILITY.md) when changing documentation or generated reports. Use clear headings, descriptive links, meaningful table headers, and text alternatives for images. Preserve category navigation and fix generated-content barriers in the generator. Record relevant checks and known limitations in the pull request; do not claim conformance based only on automated validation.

The [accessibility issue form](https://github.com/mickpletcher/best-of-github/issues/new?template=accessibility.yml) and blank issues are available for reporting barriers. Do not include medical or other private information.

## Security

Do not report vulnerabilities in a public issue. Follow [SECURITY.md](SECURITY.md) for private reporting.
