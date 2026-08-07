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

## Delivery drops (read-only snapshots — never a source)
The repository is the source; the process owner keeps a **read-only reading
copy** in OneDrive. It is delivered as a **one-way zip snapshot**, produced on
each merge to `main` and **copied in by hand**. That folder is never edited —
edits there are lost; all changes happen in the repo.

```bash
# after merging to main, produce a full snapshot drop
python3 tools/make_drop.py
```
This writes `HERO_Manual_Site_drop_<date>_<short-sha>.zip` containing a full,
coherent snapshot (`docs/`, `mkdocs.yml`, `README.md`, and the generated
`HERO_Manual_Full_v*.md`) — never a delta — plus a `_DROP_MANIFEST.md` (repo
URL, commit, what changed since the previous drop, file list). It prints the
destination folder to copy the drop into:
```
C:\Users\bartolr\OneDrive - Hasbro Inc\Demand Planning\HERO PROJECT\04_outputs\_repo_snapshots\manual-site\
```

The same tool drops the `mod1-knowledge-check` repo — generated/reference
artefacts only, question bank matched **by pattern** so a version bump never
desyncs the list:
```bash
python3 tools/make_drop.py \
  --repo-root /path/to/mod1-knowledge-check \
  --include APP_INVENTORY.md APP_MANIFEST.md 'KC_Canonical_QuestionBank_v*.json' audit \
  --prefix KnowledgeCheck_drop \
  --dest 'C:\Users\bartolr\OneDrive - Hasbro Inc\Demand Planning\HERO PROJECT\04_outputs\_repo_snapshots\knowledge-check\'
```
The older `_code_handoffs\` zips are from the retired repo-inbound direction;
they are not touched and not updated — new drops go to `_repo_snapshots`.

## Source of truth
The **repository is the single source of truth** for manual content. Changes
arrive as instructions and are committed here; there is no two-way archive
round-trip — deliveries out are the one-way read-only drops above. Content
originates from the HERO User Manual (v0) and the BU-SKU Reconciliation Behavior
Explainer. Unresolved points are flagged in each page under "Gaps & Open
Questions" for SME review before pencils-down.
