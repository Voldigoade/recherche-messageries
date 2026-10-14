# Verification

Run the Python checks with the dependencies in `requirements.txt`, then install browser tools with `npm ci` and `npx playwright install chromium` (`--with-deps` on Linux CI).

- `npm test`: decision constraints, phone visibility, incompatible platforms, explicit global-observer limits, Session's downgrade and comparator URL validation.
- `python scripts/check_catalog.py`: source ranges and hashes, required fields, translations and canonical-report integrity.
- `python scripts/check_generated.py`: generator consistency in an isolated temporary copy, without replacing working-tree files.
- `python -m mkdocs build --strict` and `python scripts/check_site.py`: every internal destination, fragment, title, description, canonical, reciprocal hreflang, sitemap, robots, search index and original download checksum.
- `npm run test:browser`: Chromium at 320/375/768/1024/1440 px in FR/EN/ES; ordinary tables, large matrices, long strings, keyboard navigation, comparator history and limits, chooser validation/results/reset, search, mobile and desktop WCAG axe audits, forced colours, reduced motion and no-JavaScript reading. It writes an ignored `.qa/browser-report.json` and screenshots.

The browser suite starts and stops its own localhost static preview. Set `STUDY_PYTHON` if Python is installed elsewhere, or `STUDY_TEST_PORT` if port 8773 is occupied. Browser automation uses Playwright because no browser-testing skill is available in this environment.

Automated Chromium and axe checks do not replace manual testing with NVDA, VoiceOver, Safari or physical devices. The research also retains its documented laboratory, forensic and binary-reproduction limits.

`python scripts/check_external.py` is a separate read-only availability diagnostic for cited URLs. HTTP errors, rate limits and blocks are recorded in `.qa/external-links.json`; they do not change claims or fail CI. Do not use `--publish` unless intentionally updating the dated availability snapshot.
