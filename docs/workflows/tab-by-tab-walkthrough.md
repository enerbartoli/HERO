<!-- docs/workflows/tab-by-tab-walkthrough.md -->

# Tab-by-tab walkthrough

## Who should read this page

All users authoring in the workbook. Use it as a map of what each tab is for.

## Purpose

Describe every tab in the standard workbook and the BU-SKU workbook mode.

## Standard workbook tabs

| Tab | Type | Use it for |
|---|---|---|
| **information** | Read-only | Quick reference for how HERO behaves; the split between Enrichments, Reconciliation, and BU-SKU mode. Open first if unsure where a change belongs. |
| **instructions** | Read-only | Scenario-based decision aid. Use when you know the business situation but not the HERO path. |
| **summary** | Read-only | Workbook rollup (when reconciliation data is included in the download). |
| **enrichments** | Editable | Event capture: promotions, sets, pre-orders, TMO, marketing overlays. Creates or updates enrichment rows. |
| **reconciliation** | Editable | Forecast-partner reconciliation: review baseline + overlays, then enter final deltas. |
| **enrichment_validation_errors** | Read-only | Row-level enrichment error detail. Only appears when an upload is rejected. |
| **reconciliation_val_errors** | Read-only | Row-level reconciliation error detail. Only appears when an upload is rejected. |
| **data_validation_ranges** | Hidden helper | Dropdowns and lookups. **Never edit.** |
| **_hero_template_scope** | Hidden helper | Carries the workbook scope so HERO can verify the upload matches the download. **Never edit.** |

## BU-SKU workbook mode

!!! note "Triggered by All Forecast Partners"
    Selecting *All Forecast Partners* at download produces a later-stage reconciliation workbook, **not** the normal forecast-partner workbook.

- **Visible scope:** aggregated to Business Unit + Planning SKU + Shipment Channel + Fiscal Year. Forecast Partner fields stay blank / hidden.
- **Editable weekly behavior:** edit signed BU-SKU weekly reconciliation-adjustment totals in units. Blank keeps the current rendered total; `0` sets it to zero; positive and negative values are allowed.
- **Upload treatment:** HERO keeps only changed weeks and range controls, then redistributes the net effect to forecast-partner rows by baseline share (even split if the baseline total is zero).

!!! warning "Do not mix modes"
    Do not upload both standard reconciliation and BU-SKU reconciliation from the same workbook. Once teams move into BU-SKU review, older Level 1 workbooks are stale. Author BU-SKU rows only on the `reconciliation_bu_sku` tab and leave partner fields blank.

## Editable reconciliation fields (pilot)

Edit only: weekly **Base Trend Adjustments**, **Adjusted Planning SKU**, **Version Adjustment Start/End Week**, **Channel Shift Proportion**, **Channel Shift Start/End Week**. Everything else (item dimensions, Lifecycle Status, Blended A-Price, baseline totals, rendered weekly columns) is read-only context.

## Related pages

- [Field-by-field reference](field-by-field-reference.md)
- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
