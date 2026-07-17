# Prompt 3 for Claude Code — apply the Hasbro character-brand look & feel

Use after Prompts 1 and 2. Goal: make the HERO manual **feel like a Hasbro product** — an IP /
character company — while staying a clean, readable reference manual. The brand assets and exact
tokens are already extracted into the repo: see `BRAND_ASSETS.md` and `docs/assets/img/`.

## Hard constraints
- **Do not change manual content** or the "Gaps & Open Questions" blocks (same as Prompts 1–2).
- **Use the exact palette and assets in `BRAND_ASSETS.md`.** Do not invent colors or pull character
  images from the web — only the official files already in `docs/assets/img/`.
- **Follow the logo & IP rules in `BRAND_ASSETS.md`**: never recolor, rotate, stretch, or redraw the
  logo; keep its white border and 16° angle; do not alter character artwork.
- **Readability wins.** Characters and gradients are accents on headers and landing areas — never
  behind body text, tables, or code. This is a working reference, not a poster.

## 1. Replace the placeholder palette with the corporate one
The current `docs/stylesheets/extra.css` and `mkdocs.yml` use a placeholder navy/teal/yellow scheme.
Replace it with the Hasbro palette:
- Primary: Hasbro Blue `#005EB8`, Cyan `#00AEEF`, Navy `#003C77`.
- Accents (sparingly): Magenta `#C71882`, Violet `#625DA3`, Green `#8DC63F`.
- Map Material `--md-primary-fg-color` to `#005EB8` (or Navy `#003C77` for the top bar) and
  `--md-accent-fg-color` to Cyan `#00AEEF`. Links in Hasbro Blue.
- Keep a clean white/very-light content background for legibility.

## 2. Logo, favicon, typography
- Set `theme.logo: assets/img/hasbro-logo.png` and `theme.favicon: assets/img/favicon.png` in `mkdocs.yml`.
- Typography: prefer **Proxima Nova** only if a licensed Monotype web kit is available; otherwise set the
  font stack to Arial / system sans-serif (the brand guide's approved fallback). Do not load an
  unlicensed Proxima Nova webfont.

## 3. Signature gradient + pattern motif
- Style the page header / hero area with the diagonal **blue→violet gradient** (cyan→blue→navy with
  magenta/violet edges) — replicate with CSS `linear-gradient`, or use `bg-gradient-1.jpg` /
  `bg-gradient-2.jpg` as a background image.
- Add the subtle **concentric rounded-square** motif and **diagonal light streaks** as a light CSS
  texture on hero areas only (low opacity), echoing the deck templates.

## 4. Character hero per top-level section — lead with HEROES
The tool is **HERO**, so put **heroic characters first** on the most visible pages. Lead with
Transformers (Optimus Prime, Bumblebee) and the D&D adventure art; relegate the non-hero franchises
(Monopoly, Peppa, Play-Doh) to lighter back sections, and use plain gradients for dense pages.
Give each top-level section a hero banner with the title overlaid on the left open space.

| Section | Hero image | Why |
|---|---|---|
| Home | `hero-transformers.jpg` (Optimus Prime) | Flagship hero — sets the HERO identity |
| Role-based guides | `hero-bumblebee.jpg` | Hero |
| Getting started | `hero-dnd.jpg` | Heroic / adventure |
| Tools & templates | `bg-gradient-1.jpg` | Dense content — keep clean |
| Workflows | `bg-gradient-2.jpg` | Dense content — keep clean |
| Examples | `hero-playdoh.jpg` | Lighter back section |
| Help & troubleshooting | `hero-peppa.jpg` | Lighter back section |
| Reference | `hero-monopoly.jpg` | Lighter back section |

If more approved Hasbro hero art is added later (G.I. Joe, Power Rangers, more Transformers — see
`BRAND_ASSETS.md`), prefer it on the lead sections and push the non-hero franchises further back.

Implementation options (pick the lowest-maintenance that works):
- A small bit of CSS keyed off the section URL, or
- Material's `template` / `main.html` override that sets a hero based on the page's top-level nav, or
- A per-page front-matter / `attr_list` hook (e.g. an HTML hero block at the top of each section
  landing page) — but if you add HTML hero blocks to pages, add ONLY presentational markup, never new
  manual text.

## 5. Accessibility & polish
- Ensure WCAG-AA contrast: white text only over the darker part of gradients; add a subtle dark overlay
  behind overlaid titles if needed.
- Respect `prefers-reduced-motion` (no animated gradients for those users).
- Test light/dark palette toggle if enabled — keep the Hasbro blue identity in both.

## 6. Report back
- Screenshots (or a description) of: home hero, one section hero, a content page, and the nav/logo.
- Confirm `mkdocs build --strict` still passes and body-text readability is unaffected.
- Note any brand asset you wish you had (e.g. a transparent-PNG character cutout, the official branded
  pattern vector, or a licensed Proxima Nova web kit) in `BUILD_NOTES.md` for Rene to source.
