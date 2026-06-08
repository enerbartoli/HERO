# Prompt 2 for Claude Code — complete the HERO Manual site (complements Prompt 1)

Use this AFTER the first prompt (install, `mkdocs build --strict`, structural fixes, git push,
GitHub Pages deploy). The content is now **complete and validated** — all 24 pages are present,
every nav entry resolves to a file, and there are **0 broken internal links**. This second pass
is about completeness verification, brand/UX polish, and repo hygiene.

## Same hard constraints as before
- **Do not write, rewrite, or invent HERO (Hasbro Enrichment & Reconciliation Optimizer) content.**
- **Preserve every `!!! question "Gaps & Open Questions"` admonition exactly.**
- Anything missing/contradictory → record in `BUILD_NOTES.md`, do not "fix" by inventing.

## 1. Verify the full content set
Confirm these 24 pages build and render without warnings:
- `index.md`
- `roles/`: demand-planner, sales, marketing-gpl
- `getting-started/`: what-hero-is, hero-in-the-cycle, roles-permissions
- `tools/`: hero-portal, enrichment-capture-template, forecast-reconciliation-template,
  bu-sku-level-25-mode, reference-views-dashboards
- `workflows/`: end-to-end-workflow, tab-by-tab-walkthrough, timing-system-sync, field-by-field-reference
- `examples/`: calculation-reference, bu-sku-worked-examples
- `help/`: validation-error-catalogue, faq-common-gotchas, glossary
- `reference/`: logility-array-mart-mapping, deferred-in-v0, documentation-governance

Spot-check that the markdown tables (field-by-field reference, error catalogue, Logility arrays)
and the worked-example admonitions in `examples/` render correctly under Material.

## 2. Repo hygiene
- Add a `requirements.txt` pinning `mkdocs-material` (so the GitHub Action and local installs match).
- Add a `.gitignore` for `site/`, `.cache/`, `__pycache__/`, and OS cruft.
- Confirm `README.md` local-preview and deploy instructions are accurate.

## 3. Brand & UX polish (only if it does not change content meaning)
- Apply Hasbro branding: add a logo and favicon to `mkdocs.yml` if assets are provided;
  keep the existing palette (navy `#0B1F3A`, teal `#1FB6B6`, accent yellow `#FFC72C`).
- Enable useful Material features if not already on: `navigation.instant`, `navigation.tracking`,
  `toc.integrate` or `toc.follow`, `content.tooltips`, and a light/dark `palette` toggle.
- Confirm site search returns results for key terms (e.g. "BU-SKU", "base trend", "validation").

## 4. Build a consolidated "Open Questions" view (structure only, no new facts)
Generate `docs/reference/open-questions.md` by **collecting the existing** "Gaps & Open Questions"
bullets already present across the 24 pages into one table (Page | Open item). Do not author new
questions — only aggregate what is already written. Add it to the `nav` under Reference, and link
back to each source page. If you prefer not to maintain it by hand, add a short note in
`BUILD_NOTES.md` recommending the `mkdocs-material` tags or a simple script to regenerate it.

## 5. Final report
- `mkdocs build --strict` result (clean, or the exact blockers).
- Live GitHub Pages URL + local `mkdocs serve` URL.
- A short list of brand assets still needed (logo, favicon) if any.
- `BUILD_NOTES.md` updated with anything that needs Rene's source-grounded input.
