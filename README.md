# HERO User Manual (documentation site)

Markdown source for the HERO (Hasbro Enrichment & Reconciliation Optimizer) user manual,
built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local preview
```bash
pip install mkdocs-material
mkdocs serve
```
Open http://127.0.0.1:8000

## Deploy
Pushing to `main` runs `.github/workflows/deploy.yml`, which publishes to GitHub Pages
via `mkdocs gh-deploy`. Enable Pages (Settings → Pages → Deploy from branch: `gh-pages`).

## Source of truth
Content is consolidated from the HERO User Manual (v0) and the BU-SKU Reconciliation
Behavior Explainer. Unresolved points are flagged in each page under
"Gaps & Open Questions" for SME review before pencils-down.
