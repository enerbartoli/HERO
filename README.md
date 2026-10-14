# HERO User Manual — moved

This site has been retired. The HERO User Manual and its training resources
now live on the new HERO Enablement site:

https://hero-enablement.apps.ai-dev.tiamat.cloud

GitHub Pages (https://enerbartoli.github.io/HERO/) now serves only a "This site
has moved" notice on the home page and a matching `404.html`, so old deep links
(e.g. `/HERO/roles/demand-planner/`) show the same notice. There is
deliberately **no automatic redirect**: visitors click the button to continue,
so they notice the change and update their bookmarks.

The previous manual (all section pages, the Prioritization Matrix, and the
site configuration) is preserved in git history and on the
`archive/pre-redirect-2026-10-13` branch.

## What is still in this repo

- `docs/index.md` and `docs/overrides/` — the moved notice and 404 page.
- `docs/assets/`, `docs/stylesheets/` and the theme settings in `mkdocs.yml` —
  kept so the notice stays on-brand.
- `HERO_Manual_Full_v<N>_<date>.md` — kept **frozen** as the last full text of
  the manual (it was the knowledge file for the Brave assistant). Do not
  regenerate it with `tools/generate_manual_full.py`: `docs/` no longer holds
  the manual, so the output would only contain the notice.

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which publishes to
GitHub Pages via `mkdocs gh-deploy`. CI (`.github/workflows/ci.yml`) runs
`mkdocs build --strict` on every push and pull request.
