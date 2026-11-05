# Accessibility

## Goals and scope

Best of GitHub aims to make its curated catalog, generated rankings, documentation, and contribution process usable by people with different abilities and assistive technologies. Clear text, navigable structure, and practical ways to report barriers are part of that goal.

The repository is Markdown-first, with Python maintenance scripts rather than a hosted application. It can be read on GitHub or in a local editor or Markdown reader. GitHub's interface and each reader's rendering affect the experience. The [README](README.md#run-locally) documents Python requirements; these are not a claim of assistive-technology compatibility. Linked third-party projects have their own accessibility practices and support routes.

## Current status and known limitations

- Source files provide text versions of the curated catalog, watchlist, and weekly reports. Category headings and report summary links help readers navigate the content.
- Long ranking tables, horizontal scrolling, link-heavy entries, badges, and the growing daily archive may create barriers, especially on narrow screens or with assistive technology.
- Generated repository links include HTML attributes for opening new tabs in compatible renderers. GitHub may ignore those attributes, so link behavior differs between readers.
- No repository-wide assistive-technology audit or WCAG conformance assessment has been completed for this statement. A specific screen reader, browser, keyboard-only workflow, or zoom level has not been certified here.
- Catalog inclusion, popularity, and automated report validation do not establish the accessibility of a listed project.

## Contributor guidance

- Use descriptive headings in a logical order, clear language, meaningful link text, and short steps.
- Keep tables simple with meaningful column headers. Consider a list or prose alternative when a wide table makes information difficult to use.
- Give informative images useful alternative text. Include essential information as text, not only in a screenshot, badge, color, position, or emoji.
- Preserve category navigation and source text when changing report generators. Fix generated-output barriers in the generator rather than manually editing a report that the next run will overwrite.
- For a relevant change, check keyboard access, focus visibility, heading order, link purpose, reading order, text resizing, and narrow-screen behavior in the environment being used. Record what was checked and what remains untested. [W3C's accessibility introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/) is a useful starting point.
- Do not claim universal accessibility or legal compliance from a documentation update or an automated check.

## Report a barrier or request an alternative

Use the [accessibility issue form](https://github.com/mickpletcher/best-of-github/issues/new?template=accessibility.yml). If the form is a barrier, a [blank issue](https://github.com/mickpletcher/best-of-github/issues/new) with a short text description is enough. Screenshots and medical details are not required.

Useful information includes the affected page or file, what you were trying to do, what prevented it, the expected experience, and an alternative that would help. Browser, operating system, Markdown reader, and assistive-technology details are optional. Issues are public: omit personal health information, credentials, and other private data.

The repository owner, [@mickpletcher](https://github.com/mickpletcher), reviews reports alongside other project work. Fixes should describe the affected content and checks performed, and this statement should be updated when relevant behavior changes. No response deadline or audited conformance level is promised.
