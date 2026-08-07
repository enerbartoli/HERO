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

## Consolidated single-file manual (generated — never edit by hand)
`HERO_Manual_Full_v<N>_<date>.md` at the repo root is a single concatenated
Markdown copy of the whole manual, used as the knowledge file for the Brave
assistant. **It is generated, not hand-maintained** — it used to be edited by
hand and fell a month behind the site, which is exactly the drift we are
removing.

Regenerate it after any content change and commit the result:
```bash
python3 tools/generate_manual_full.py
```
The generator reads `mkdocs.yml`'s nav order, concatenates every
`docs/**/*.md` page in that order, flattens the MkDocs `!!! type "label"`
admonitions into plain Markdown, and fails loudly if a page under `docs/` is
missing from the nav or a nav entry points at a missing file. Bump `VERSION`
and `DATE` at the top of the script when the manual is republished.

**Do not edit the generated file by hand.** CI enforces this:
`.github/workflows/ci.yml` runs `mkdocs build --strict` and
`python3 tools/generate_manual_full.py --check` on every push and pull request,
and the check fails the build if the committed file is out of date with `docs/`.

## Source of truth
The **repository is the single source of truth** for manual content. Changes
arrive as instructions and are committed here; there is no packaged-archive
round-trip. Content originates from the HERO User Manual (v0) and the BU-SKU
Reconciliation Behavior Explainer. Unresolved points are flagged in each page
under "Gaps & Open Questions" for SME review before pencils-down.
