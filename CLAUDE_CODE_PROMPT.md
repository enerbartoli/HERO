# Prompt for Claude Code — continue the HERO User Manual site

Paste this into Claude Code when working inside the `HERO_Manual_Site` repository.

---

You are working in `HERO_Manual_Site`, an **MkDocs Material** documentation site for the
HERO (Hasbro Enrichment & Reconciliation Optimizer) user manual. The content is **complete**:
24 Markdown pages under `docs/`, wired into `mkdocs.yml` `nav`. Your job is to build, deploy,
and polish the site — **not** to write or change manual content.

## Current state (already done outside Code)
- `docs/` contains all 24 pages: home, role guides (3), getting-started (3), tools (5),
  workflows (4), examples (2), help (3), reference (3).
- `mkdocs.yml` has the full nav, Material theme, and admonition/superfences extensions.
- `docs/stylesheets/extra.css` carries the Hasbro palette (navy `#0B1F3A`, teal `#1FB6B6`,
  accent yellow `#FFC72C`).
- `.github/workflows/deploy.yml` runs `mkdocs gh-deploy` on push to `main`.
- Validated already: 0 broken internal links, every nav entry resolves to a file, no orphan pages.
- NOT yet done: an actual `mkdocs build` (the authoring environment had no PyPI access to
  install `mkdocs-material`).

## Hard constraints
- **Do not write, rewrite, or invent HERO manual content.** The Markdown was authored from
  controlled source documents. You may fix Markdown syntax, broken links, and formatting only.
- **Preserve every "Gaps & Open Questions" admonition exactly.** They are deliberate review flags.
- Anything that looks missing, wrong, or contradictory goes into `BUILD_NOTES.md` for Rene to
  resolve from source — never edit the content to "fix" it yourself.

## What to do
1. `pip install mkdocs-material`, then `mkdocs build --strict`. Report every warning/error.
2. Fix only **structural** issues to make the build pass: broken relative links, malformed
   admonitions (`!!! note` / `tip` / `warning` / `example` / `question` / `success`), bad table
   syntax. If a real content page is genuinely missing, comment its nav line (don't delete) and
   note it in `BUILD_NOTES.md`.
3. Confirm rendering: Material theme loads, the custom palette applies, admonitions render, and
   search works.
4. `mkdocs serve` and confirm the site loads locally; report the local URL.
5. Initialize git if needed, commit, push to `main` on GitHub (private repo).
6. Deploy via GitHub Pages: confirm the `deploy.yml` workflow runs (or run `mkdocs gh-deploy`).
   If Pages needs enabling, give me the exact Settings → Pages steps. Report the published URL.

## Optional polish (only if it does not touch content meaning)
- Add a site logo / favicon if Hasbro brand assets are provided.
- Enable `navigation.instant` and a dark/light palette toggle if desired.
- Add `mkdocs-material` social cards / metadata.

## Deliverables
- A passing `mkdocs build --strict` (or a precise list of what blocks it).
- The live GitHub Pages URL and the local `mkdocs serve` URL.
- `BUILD_NOTES.md` listing: any commented-out nav entries, unresolved links, and any content
  that looks incomplete — for Rene to fix from source, not you.
