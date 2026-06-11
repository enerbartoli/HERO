<!-- docs/tools/forecast-reconciliation-template.md -->

# Forecast Reconciliation Template (FRT)

## Who should read this page

Demand Planning (primary) and Sales when proposing final-number changes.

## Purpose

Explain when to use the **Forecast Reconciliation Template (FRT)** and what is editable on it.

## When to use it

Use reconciliation when the business needs to **directly change the final week-level number** after enrichments are already considered. If the ask is *"change the final number for these weeks,"* it belongs here rather than in enrichments.

## What you can edit

!!! note "Editable controls only"
    On the reconciliation tab, edit only these fields:

    - Weekly **Base Trend Adjustments**
    - **Adjusted Planning SKU** (Version Change)
    - **Version Adjustment Start Week** / **End Week**
    - **Channel Shift Proportion**
    - **Channel Shift Start Week** / **End Week**

    Treat item-dimension fields, Lifecycle Status, Blended A-Price, baseline totals, and the rendered baseline / sales-enrichment / marketing-and-demand-planning weekly columns as **read-only context**.

!!! warning "Two rules to remember"
    - **Deltas, not absolutes** — reconciliation does not support an absolute overwrite. Enter a plus/minus change.
    - **One structured control per row** — do not combine an Adjusted Planning SKU (version change) and a Channel Shift Proportion on the same row.

## Actualized vs forward weeks

Weeks in the actualized period use exact row-level shipment actuals where they exist, and 0 where no exact actual is available; values are zero-floored so negative net shipment weeks render as 0. **Shaded** cells mark the actualized shipment period (historical cutoff); **unshaded** cells are forward forecast weeks.

!!! note "Channel shift moves the enrichments too"
    A Channel Shift moves demand between `DOM` and `DI`. Make sure any enrichments associated with the moved volume are also moved to the correct channel. Capture a genuine change in total demand separately.

!!! tip "Forecasting range (start / end dates)"
    To stop forecasting a SKU for a customer, adjust the **forecast calculation range** (set an end date) — distinct from a phase-out enrichment. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md).

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU / Level 2.5 mode](bu-sku-level-25-mode.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
