# Prompt 4 for Claude Code — navigation UX fix + brand logos + image reuse

Use after Prompts 1–3. Same hard constraints apply (no content changes, preserve Gaps blocks,
follow logo/IP rules, readability wins). New brand assets are already in the repo.

## 1. Fix the left-nav section titles (currently light-gray and confusing)
Make each top-level chapter a **collapsible group with an expand/collapse arrow (chevron)** and a
**larger, higher-contrast title**, so a user expands a chapter and then sees its subchapters.

- In `mkdocs.yml`, **remove `navigation.sections`** (it renders the flat gray section labels). Keep
  `navigation.top`, `navigation.tracking`, `toc.follow`. Do **not** add `navigation.expand` (we want
  them collapsed until expanded). This gives the built-in collapsible chevron behavior.
- In `docs/stylesheets/extra.css`, increase the prominence of the section toggles, e.g.:
  ```css
  .md-nav__item--nested > .md-nav__link {
    font-size: .82rem;          /* larger than the default group label */
    font-weight: 700;
    color: var(--md-primary-fg-color);  /* Hasbro navy/blue, not light gray */
    text-transform: none;
  }
  .md-nav__icon { transform: scale(1.2); }  /* make the expand/collapse arrow clearer */
  ```
- Verify the chevron toggles open/close each chapter and that subchapters are reachable.

## 2. Brand logos — use them
`docs/assets/img/brands/` now holds transparent `.webp` brand marks (see `BRAND_ASSETS.md`):
transformers, gijoe, dnd, magic-the-gathering, monopoly, playdoh, nerf, beyblade-x, furby,
my-little-pony, plus two wide G.I. Joe banners.

- Use a brand logo as a small badge / accent on the matching section hero or on cards — never
  altered, never stretched.
- Pair logos with the section that fits (e.g. `transformers-logo` on a Transformers hero,
  `dnd-logo` on the D&D hero). Keep them subtle; they are accents, not the page focus.
- **Partner brands** `marvel-logo` and `star-wars-logo` are Disney/Lucasfilm IP — use only with
  partner approval; prefer Hasbro-owned marks for primary branding.

## 3. No new art is coming — reuse existing images
Rene will **not** provide additional images. If any page or section needs an image that is not
already in `docs/assets/img/` or `docs/assets/img/brands/`, **reuse one of the existing heroes or
logos** (rotate the hero set). Do not request new art and do not pull anything from the web.

## 4. Wire the texture overlays (from Prompt 3)
Use `pattern-frames.svg` and `light-streaks.svg` as overlay layers inside `.hero-banner` at low
opacity (~6–10%), above the gradient and below the title text.

## 5. Report
Confirm `mkdocs build --strict` still passes, the nav chevrons work, and include a screenshot/notes
of the updated sidebar and a section hero with its brand logo.
