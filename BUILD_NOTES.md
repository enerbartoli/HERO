# BUILD_NOTES — HERO User Manual

Last updated during **second-pass stand-up** (content complete, brand/UX polish, repo hygiene).

**Do not edit content files based on these notes** — all remediation requires the original
controlled source documents or SME confirmation.

---

## 1. Build status

`mkdocs build --strict` — **PASSING, 0 warnings** (25 pages including `open-questions.md`).

All 24 authored pages have verified nav entries and zero broken internal links.

---

## 2. Brand assets still needed

Neither a logo nor a favicon was provided in the source material.

| Asset | Expected path | `mkdocs.yml` key | Notes |
|---|---|---|---|
| Logo (SVG or PNG) | `docs/assets/logo.svg` | `theme.logo: assets/logo.svg` | Shown in navbar and tab. Recommend white/teal on navy. |
| Favicon | `docs/assets/favicon.png` | `theme.favicon: assets/favicon.png` | 32 × 32 px minimum. |

To add once assets are available:

```yaml
theme:
  logo: assets/logo.svg
  favicon: assets/favicon.png
```

---

## 3. Open-questions aggregation — maintenance note

`docs/reference/open-questions.md` was hand-generated from the 24 source pages.
It contains **24 items across 16 pages**.

To regenerate it when pages are updated, run:

```bash
grep -rn '!!! question' docs/ --include="*.md" -A 5
```

Or, for a semi-automated approach, add the
[`mkdocs-git-revision-date-localized`](https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/)
plugin and maintain this file alongside source pages. A fully automated solution would
require a small Python script (or a custom MkDocs hook) to scan `docs/` for
`!!! question` blocks and emit the table — note this in `requirements.txt` if implemented.

---

## 4. Structural changes made in second pass

| Change | File(s) | Reason |
|---|---|---|
| Light/dark palette toggle added | `mkdocs.yml`, `extra.css` | UX polish; dark mode uses teal `#1FB6B6` as primary on slate background |
| `navigation.instant` enabled | `mkdocs.yml` | SPA-like navigation |
| `content.tooltips` + `abbr` extension enabled | `mkdocs.yml` | Enables hover tooltips on abbreviations |
| `requirements.txt` added (pin `mkdocs-material==9.7.6`) | `requirements.txt` | Locks CI and local installs to same version |
| `deploy.yml` updated to `pip install -r requirements.txt` | `.github/workflows/deploy.yml` | Consistency with requirements.txt pin |
| `.gitignore` updated to add `.cache/`, `*.pyo`, `Thumbs.db` | `.gitignore` | Repo hygiene |
| `README.md` updated with pinned install command and Pages URL | `README.md` | Accurate local-preview and deploy instructions |
| `open-questions.md` added to nav under Reference | `mkdocs.yml`, `docs/reference/open-questions.md` | Consolidated view of all open items |

---

## 5. Pages with no open-questions block

These pages carry either `!!! success "No open questions identified"` or no block at all
(content considered complete at v0). No action needed unless new questions arise from
SME review.

| Page | Status |
|---|---|
| `getting-started/what-hero-is.md` | No block (complete) |
| `tools/hero-portal.md` | No block (complete) |
| `tools/forecast-reconciliation-template.md` | No block (complete) |
| `workflows/end-to-end-workflow.md` | No block (complete) |
| `workflows/tab-by-tab-walkthrough.md` | No block (complete) |
| `help/validation-error-catalogue.md` | `!!! success "No open questions identified"` |
| `reference/logility-array-mart-mapping.md` | `!!! success "No open questions identified"` |
| `reference/documentation-governance.md` | `!!! success "No open questions identified"` |

---

## 6. Items that require Rene's source-grounded input

These are the open questions from the 24 pages that are most likely to block the
pilot — grouped by theme for prioritisation:

### Write ownership (recurring across 3 pages)
- `roles/demand-planner.md`, `tools/bu-sku-level-25-mode.md`, `getting-started/roles-permissions.md`:
  Confirm whether **Level 2.5 write ownership** sits with Demand Planning or Brand Captains.

### Frozen-window exception process (recurring across 2 pages)
- `getting-started/hero-in-the-cycle.md`, `help/faq-common-gotchas.md`:
  Confirm the frozen-period / out-of-cycle exception routing for the UK pilot.

### Dashboard documentation (blocked on owner)
- `tools/reference-views-dashboards.md`: **Owner: Edgar** — Power BI documentation
  (AIM Shipment Revenue, POS Glidepath) and role-access matrix still needed.

### Scope (D2C channel)
- `workflows/field-by-field-reference.md`: Confirm whether `D2C` is in scope for the
  UK pilot — the reconciliation model currently references only `DOM` / `DI`.

### Logility cadence
- `workflows/timing-system-sync.md`: Confirm the Logility export cadence for the pilot
  (currently a draft default).
