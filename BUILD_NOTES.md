# BUILD_NOTES — HERO User Manual

Last updated: **fourth pass** — navigation UX fix, brand logos, texture overlays (Prompt 4).

**Do not edit content files based on these notes** — all remediation
requires the original controlled source documents or SME confirmation.

---

## 1. Build status

`mkdocs build --strict` — **PASSING, 0 warnings** (25 pages including `open-questions.md`).

All 24 authored pages have verified nav entries and zero broken internal links.

---

## 1b. Prompt 4 changes (navigation + brand logos + textures)

| # | Change | File(s) |
|---|---|---|
| 1 | Removed `navigation.sections` → top-level chapters are now **collapsible groups with a chevron** (collapsed until expanded; `navigation.expand` deliberately NOT added) | `mkdocs.yml` |
| 1 | Chapter toggles enlarged + high-contrast (Hasbro navy/blue, `font-weight:700`), chevron scaled 1.2×; slate-mode override (`#5cc6f5`) for sidebar readability | `extra.css` |
| 2 | **Brand-logo badge** per section hero — transparent `.webp`, top-left over the dark gradient zone, `object-fit:contain` (never stretched/recolored) | `hooks.py`, `main.html`, `extra.css` |
| 4 | **Texture overlays** `pattern-frames.svg` + `light-streaks.svg` layered inside `.hero-banner` at 8% opacity, above gradient / below title | `hooks.py`, `main.html`, `extra.css` |

### Section → hero image → brand-logo pairing

| Section | Hero image | Brand logo (accent) |
|---|---|---|
| Home | `hero-transformers.jpg` | `transformers-logo.webp` |
| Role-based guides | `hero-bumblebee.jpg` | `transformers-logo.webp` (Bumblebee = Transformers) |
| Getting started | `hero-dnd.jpg` | `dnd-logo.webp` |
| Tools & templates | `bg-gradient-1.jpg` | `nerf-logo.webp` |
| Workflows | `bg-gradient-2.jpg` | `magic-the-gathering-logo.webp` |
| Examples | `hero-playdoh.jpg` | `playdoh-logo.webp` |
| Help & troubleshooting | `hero-peppa.jpg` | `my-little-pony-logo.webp` (no Peppa logo supplied — reused a light Hasbro-owned mark) |
| Reference | `hero-monopoly.jpg` | `monopoly-logo.webp` |

**Partner brands not used:** `marvel-logo.webp` and `star-wars-logo.webp` are Disney/Lucasfilm IP
(per `BRAND_ASSETS.md`) and are intentionally left out of primary branding. Also currently unused:
`gijoe-logo.webp`, `beyblade-x-logo.webp`, `furby-logo.webp`, and the wide G.I. Joe banners
(`gijoe-banner-mobile.webp`, `gijoe-vehicle-banner.webp`) — available to swap in if Rene wants a
different section pairing. No new art was requested or sourced; per Prompt 4 the existing set is reused.

---

## 2. Brand implementation — what was applied

| Component | Implementation | File(s) |
|---|---|---|
| Hasbro palette (Navy/Blue/Cyan) | CSS variables on `:root` and `[data-md-color-scheme]` | `extra.css` |
| Signature diagonal gradient header | `background-image: linear-gradient(135deg, #003C77 → #005EB8 → #625DA3)` on `.md-header` | `extra.css` |
| Logo (16° angle badge) | `theme.logo: assets/img/hasbro-logo.png` | `mkdocs.yml` |
| Favicon | `theme.favicon: assets/img/favicon.png` | `mkdocs.yml` |
| Typography | `font: false` — Arial / system sans; no Proxima Nova license | `mkdocs.yml`, `extra.css` |
| Light/dark toggle | Two palette entries (`default` / `slate`) with toggle icons | `mkdocs.yml` |
| Hero banners per section | Python hook (`hooks.py`) + Jinja2 override (`docs/overrides/main.html`) | `hooks.py`, `main.html`, `extra.css` |
| `navigation.instant`, `content.tooltips`, `abbr` | Enabled in features + extensions | `mkdocs.yml` |
| Open questions aggregation | 24 items across 16 pages verbatim | `docs/reference/open-questions.md` |

### Section → hero image mapping

| Section | Image used | Rationale |
|---|---|---|
| Home | `hero-transformers.jpg` (Optimus Prime) | Flagship hero — sets HERO identity |
| Role-based guides | `hero-bumblebee.jpg` (Bumblebee) | Hero / Transformers |
| Getting started | `hero-dnd.jpg` (D&D dragon) | Heroic / adventure |
| Tools & templates | `bg-gradient-1.jpg` | Dense content — clean gradient |
| Workflows | `bg-gradient-2.jpg` | Dense content — clean gradient |
| Examples | `hero-playdoh.jpg` | Lighter back section |
| Help & troubleshooting | `hero-peppa.jpg` | Lighter back section |
| Reference | `hero-monopoly.jpg` | Lighter back section |

---

## 3. Brand assets still wanted (note for Rene)

These would improve the site but are not available in the current asset set.
All are sourced from official Hasbro brand material — do not pull from the web.

| Asset | Where to use | Notes |
|---|---|---|
| **Proxima Nova web font kit** (Monotype license) | `mkdocs.yml` `theme.font` | Current fallback: Arial/system. Kit URL from Corporate Brand Team. |
| **Transparent-background character cutouts** (PNG, no bg) | Hero banner foreground layer | Current JPEGs have full backgrounds; cutouts allow more flexible layout. |
| **Concentric rounded-square SVG pattern** | `.hero-banner` texture overlay at ~5–8% opacity | Echoes the deck template motif. Currently omitted (vector not in repo). |
| **Diagonal light-streak SVG** | `.hero-banner` texture overlay | Same source as above — deck template assets. |
| **`banner.jpg` footer strip** (`docs/assets/img/banner.jpg` — 1600×300 franchise diamonds) | Page footer | Template override extension needed; noted for a future pass. |
| **More Transformers / G.I. Joe / Power Rangers hero art** | Home and lead sections | Drop approved 16:9 images as `docs/assets/img/hero-*.jpg` and the hook picks them up automatically. |

---

## 4. Open questions that need Rene's input (priority order)

| Priority | Pages | Item |
|---|---|---|
| 1 | demand-planner, bu-sku-level-25-mode, roles-permissions | Confirm **Level 2.5 write ownership** (Brand Captain vs Demand Planning) |
| 2 | hero-in-the-cycle, faq-common-gotchas | Confirm **frozen-window exception routing** for the UK pilot |
| 3 | reference-views-dashboards | **Owner: Edgar** — Power BI docs (AIM Shipment Revenue, POS Glidepath) |
| 4 | field-by-field-reference | Is `D2C` in scope? Reconciliation model references only `DOM`/`DI` |
| 5 | timing-system-sync | Confirm Logility export cadence (currently a draft default) |

Full list of 24 items: `docs/reference/open-questions.md`

---

## 5. Open-questions page maintenance

`docs/reference/open-questions.md` was hand-generated from the 24 source pages.
To regenerate after page edits:

```bash
grep -rn '!!! question' docs/ --include="*.md" -A 5
```

---

## 6. Repo hygiene notes

| File | Purpose |
|---|---|
| `hooks.py` | MkDocs hook — injects `hero_bg_url` / `hero_label` into page context |
| `docs/overrides/main.html` | Material template override — renders hero banner before page content |
| `requirements.txt` | Pins `mkdocs-material==9.7.6` for local + CI install parity |
| `.github/workflows/deploy.yml` | Uses `pip install -r requirements.txt` |
| `.gitignore` | Excludes `site/`, `.cache/`, `__pycache__/`, OS cruft |
