# BUILD_NOTES — HERO User Manual

Generated during initial site stand-up. **Do not edit content files based on these
notes** — all remediation requires the original controlled source documents.

---

## 1. Commented-out nav entries (12 pages not yet authored)

The following pages are referenced in `mkdocs.yml` but no Markdown file exists.
Each entry is commented out in the nav; uncomment once the source document is converted.

### Workflows section (entire section hidden)

| Nav title | Expected file |
|---|---|
| End-to-end workflow | `docs/workflows/end-to-end-workflow.md` |
| Tab-by-tab walkthrough | `docs/workflows/tab-by-tab-walkthrough.md` |
| Timing & system sync | `docs/workflows/timing-system-sync.md` |
| Field-by-field reference | `docs/workflows/field-by-field-reference.md` |

### Examples section (entire section hidden)

| Nav title | Expected file |
|---|---|
| Calculation reference | `docs/examples/calculation-reference.md` |
| BU-SKU worked examples | `docs/examples/bu-sku-worked-examples.md` |

### Help & troubleshooting section (entire section hidden)

| Nav title | Expected file |
|---|---|
| Validation & error catalogue | `docs/help/validation-error-catalogue.md` |
| FAQ & common gotchas | `docs/help/faq-common-gotchas.md` |
| Glossary | `docs/help/glossary.md` |

### Reference section (entire section hidden)

| Nav title | Expected file |
|---|---|
| Logility array & mart mapping | `docs/reference/logility-array-mart-mapping.md` |
| Deferred in v0 | `docs/reference/deferred-in-v0.md` |
| Documentation governance | `docs/reference/documentation-governance.md` |

---

## 2. Broken internal links in existing pages

These links appear in authored pages and point to the missing files above.
They will resolve automatically once the target pages are created.
**Do not remove them from the source Markdown** — they are intentional forward references.

`mkdocs.yml` has `validation.links.not_found: ignore` to suppress build warnings
until the target pages exist.

| Source file | Link text | Target (missing) |
|---|---|---|
| `docs/index.md` | Field-by-field reference | `workflows/field-by-field-reference.md` |
| `docs/index.md` | Validation & error catalogue | `help/validation-error-catalogue.md` |
| `docs/getting-started/hero-in-the-cycle.md` | End-to-end workflow | `workflows/end-to-end-workflow.md` |
| `docs/getting-started/hero-in-the-cycle.md` | Timing & system sync | `workflows/timing-system-sync.md` |
| `docs/roles/demand-planner.md` | Field-by-field reference | `workflows/field-by-field-reference.md` |
| `docs/roles/demand-planner.md` | Calculation reference | `examples/calculation-reference.md` |
| `docs/roles/demand-planner.md` | BU-SKU worked examples | `examples/bu-sku-worked-examples.md` |
| `docs/roles/demand-planner.md` | Validation & error catalogue | `help/validation-error-catalogue.md` |
| `docs/roles/sales.md` | Tab-by-tab walkthrough | `workflows/tab-by-tab-walkthrough.md` |
| `docs/roles/sales.md` | Validation & error catalogue | `help/validation-error-catalogue.md` |
| `docs/roles/sales.md` | Calculation reference | `examples/calculation-reference.md` |
| `docs/tools/bu-sku-level-25-mode.md` | BU-SKU worked examples | `examples/bu-sku-worked-examples.md` |
| `docs/tools/enrichment-capture-template.md` | Field-by-field reference | `workflows/field-by-field-reference.md` |
| `docs/tools/enrichment-capture-template.md` | Tab-by-tab walkthrough | `workflows/tab-by-tab-walkthrough.md` |
| `docs/tools/forecast-reconciliation-template.md` | Field-by-field reference | `workflows/field-by-field-reference.md` |
| `docs/tools/forecast-reconciliation-template.md` | Calculation reference | `examples/calculation-reference.md` |
| `docs/tools/hero-portal.md` | End-to-end workflow | `workflows/end-to-end-workflow.md` |
| `docs/tools/hero-portal.md` | Timing & system sync | `workflows/timing-system-sync.md` |
| `docs/tools/reference-views-dashboards.md` | Timing & system sync | `workflows/timing-system-sync.md` |
| `docs/tools/reference-views-dashboards.md` | Deferred in v0 | `reference/deferred-in-v0.md` |

---

## 3. Structural notes

- `scheme: hero` in `mkdocs.yml` palette is a custom value (Material supports
  `default` / `slate` natively). It works because `docs/stylesheets/extra.css`
  defines `[data-md-color-scheme="hero"]` — no action needed.
- The `site/` output directory is excluded via `.gitignore` and is not committed.
- The GitHub Actions workflow (`deploy.yml`) uses `mkdocs gh-deploy --force`
  (no `--strict`). Once the missing pages are authored, re-enable strict mode
  in the workflow for ongoing CI protection.

---

## 4. To restore a section

1. Create the Markdown file in the appropriate `docs/` sub-directory.
2. In `mkdocs.yml`, uncomment the corresponding nav line(s).
3. If this is the first page in a section, also uncomment the section header line.
4. Run `mkdocs build --strict` locally to verify.
