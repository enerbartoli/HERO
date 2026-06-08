# HERO User Manual (documentation site)

Markdown source for the HERO (Hasbro Enrichment & Reconciliation Optimizer) user manual,
built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Open **http://127.0.0.1:8000**

For a strict build (fails on any warning — use before pushing):

```bash
mkdocs build --strict
```

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which publishes to GitHub Pages
via `mkdocs gh-deploy`. First-time setup: **Settings → Pages → Source: Deploy from branch →
Branch: `gh-pages` / folder: `/ (root)` → Save**.

Published site: **https://enerbartoli.github.io/HERO/**

## Source of truth

Content is consolidated from the HERO User Manual (v0) and the BU-SKU Reconciliation
Behavior Explainer. Unresolved points are flagged on each page under
"Gaps & Open Questions" and aggregated in
[`docs/reference/open-questions.md`](docs/reference/open-questions.md) for SME review.

Do not edit content freehand — all changes must be grounded in the source documents.
See [`docs/reference/documentation-governance.md`](docs/reference/documentation-governance.md).

## Brand assets still needed

- **Logo** (`docs/assets/logo.svg` or `.png`) — add to `mkdocs.yml` under `theme.logo`
- **Favicon** (`docs/assets/favicon.png`) — add to `mkdocs.yml` under `theme.favicon`

See `BUILD_NOTES.md` for the full list of outstanding items.
