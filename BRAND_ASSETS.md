# HERO Manual — Brand assets & tokens

Extracted from the Hasbro Global Brand Guidelines (v1) and the Hasbro Deck Templates.
These are the authoritative values; do not substitute approximations.

## Color palette (exact)

### Primary (should dominate)
| Name | HEX | RGB | Pantone / CMYK |
|---|---|---|---|
| Hasbro Blue (PMS 300) | `#005EB8` | 0, 94, 184 | PMS 300 · C100 M50 Y0 K0 |
| Cyan | `#00AEEF` | 0, 174, 239 | C100 M0 Y0 K0 |
| Navy | `#003C77` | 0, 60, 119 | C100 M55 Y10 K48 |

### Secondary (accents only — never overpower primary)
| Name | HEX | RGB | CMYK |
|---|---|---|---|
| Magenta | `#C71882` | 199, 24, 130 | C20 M100 Y10 K0 |
| Violet | `#625DA3` | 98, 93, 163 | C70 M70 Y0 K0 |
| Green | `#8DC63F` | 141, 198, 63 | C50 M0 Y100 K0 |

The signature look is a **diagonal blue→violet gradient** (cyan → blue → navy with magenta/violet
edges) overlaid with a **concentric rounded-square pattern** and **diagonal light streaks**.

## Typography
- **Primary:** Proxima Nova (Regular / Semibold / Bold) — licensed via Monotype.
- **Fallback (and when Proxima Nova is unavailable, e.g. web without a license):** Arial / system sans-serif.

## Assets in `docs/assets/img/`
The tool is called **HERO**, so prioritise **heroic characters** (Transformers, D&D) on the most
visible pages; use the non-hero franchises (Monopoly, Peppa, Play-Doh) for lighter back sections.

| File | What it is | Hero? | Suggested use |
|---|---|---|---|
| `hasbro-logo.png` | Hasbro blue badge logo (16° angle, white border) | — | Site logo (top-left) |
| `favicon.png` | 64×64 logo | — | Browser favicon |
| `banner.jpg` | Franchise diamond banner strip | — | Footer / accent strip |
| `hero-transformers.jpg` | **Optimus Prime** (Transformers) | ★ Hero | Flagship — Home / lead sections |
| `hero-bumblebee.jpg` | **Bumblebee** (Transformers) | ★ Hero | Lead sections |
| `hero-dnd.jpg` | Dungeons & Dragons dragon | ★ Heroic | Lead sections |
| `hero-monopoly.jpg` | Mr. Monopoly | non-hero | Back sections |
| `hero-peppa.jpg` | Peppa Pig | non-hero | Back sections |
| `hero-playdoh.jpg` | Play-Doh | non-hero | Back sections |
| `bg-gradient-1.jpg`, `bg-gradient-2.jpg` | Character-free gradients | — | Dense pages / overlays |
| `pattern-frames.svg` | Concentric rounded-square texture (generic, white stroke) | — | Hero overlay ~6% opacity |
| `light-streaks.svg` | Diagonal light-streak texture (generic, white) | — | Hero overlay, low opacity |

!!! note
    `pattern-frames.svg` and `light-streaks.svg` are **generic recreations** that evoke the deck look —
    NOT the official branded pattern artwork (which the brand guide says must not be redrawn without
    Corporate Brand Team approval). Swap in the official vector if/when provided.

All hero images have **open space on the left** for overlaying a title.

## Brand logos in `docs/assets/img/brands/`
Transparent (`.webp`) brand marks supplied by Rene — use as small badges / accents (e.g. on section
heroes or cards), never altered. Hasbro-owned: `transformers-logo`, `gijoe-logo`, `dnd-logo`,
`magic-the-gathering-logo`, `monopoly-logo`, `playdoh-logo`, `nerf-logo`, `beyblade-x-logo`,
`furby-logo`, `my-little-pony-logo`. Also `gijoe-banner-mobile.webp` and `gijoe-vehicle-banner.webp`
(wide G.I. Joe banners).

!!! warning "Partner brands"
    `marvel-logo.webp` and `star-wars-logo.webp` are **partner brands** (Disney / Lucasfilm IP), not
    Hasbro-owned. Use only with partner approval; prefer Hasbro-owned marks for primary branding.

## No more art is coming — reuse what exists
Rene will not supply additional images beyond what is already in `docs/assets/img/` and
`docs/assets/img/brands/`. **If a page needs an image that isn't here, reuse one of the existing
heroes/logos** (rotate the hero set) rather than requesting or sourcing new art.

### Adding more hero art
Web image **downloads are not available** from this environment (the web tools return page text, not
image files), and open-web character art carries IP/quality risk versus approved files. To add more
Hasbro heroes (e.g. **G.I. Joe, Power Rangers, more Transformers**), drop approved 16:9 art into
`docs/assets/img/` using the `hero-*.jpg` naming and the theme will pick it up.

## Logo & IP rules (from the brand guide — must follow)
- Use approved logo files only. **Do not** recreate, recolor, rotate, stretch, or alter the logo or its transparency.
- Keep the **white border**; maintain clearspace ≈ the size of the “o” in the logo.
- The logo is shown at its required **16-degree angle** (the provided file already includes it).
- Character artwork is official Hasbro IP for **internal first-party use**. Do not alter character art,
  and do not source additional character images from the web. Confirm with the Corporate Brand Team
  before any external publication.
