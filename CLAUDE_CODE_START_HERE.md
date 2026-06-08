# START HERE — Claude Code instructions for the HERO Manual site

You are working inside the `HERO_Manual_Site` repository — an **MkDocs Material** documentation
site for the HERO (Hasbro Enrichment & Reconciliation Optimizer) user manual. Everything you need
is in this repo. Do not look outside it.

## Read these first (in the repo root), then execute in order
1. `CLAUDE_CODE_PROMPT.md` — build, fix structural issues, push to GitHub, deploy to Pages.
2. `CLAUDE_CODE_PROMPT_2.md` — verify all 24 pages, repo hygiene, consolidated open-questions view.
3. `CLAUDE_CODE_PROMPT_3.md` — apply the Hasbro character-brand look & feel.
4. `BRAND_ASSETS.md` — exact palette, fonts, and the asset inventory in `docs/assets/img/`.

## Hard constraints (apply to all steps)
- **Do not write, rewrite, or invent HERO manual content.** The 24 Markdown pages under `docs/`
  were authored from controlled source documents. You may fix Markdown syntax, broken links,
  formatting, and add presentational markup only.
- **Preserve every `!!! question "Gaps & Open Questions"` block exactly.**
- **Use only the colors and image files already in the repo** (`BRAND_ASSETS.md` / `docs/assets/img/`).
  Do not pull images from the web. Lead with the HERO-themed hero characters (Transformers, D&D).
- **Follow the logo & IP rules** in `BRAND_ASSETS.md`: never recolor/rotate/stretch/redraw the logo;
  keep its white border and 16° angle; never alter character artwork.
- **Readability wins** — characters and gradients are header/landing accents, never behind body text,
  tables, or code.
- Anything missing, contradictory, or that needs a real fact → record in `BUILD_NOTES.md` for Rene
  to resolve from source. Never invent it.

## Definition of done
- `mkdocs build --strict` passes (or a precise list of blockers).
- Site deployed to GitHub Pages — report the live URL and the local `mkdocs serve` URL.
- Hasbro palette + logo/favicon applied; hero banners per section per Prompt 3.
- `BUILD_NOTES.md` lists any unresolved links, commented nav entries, or assets still needed.
