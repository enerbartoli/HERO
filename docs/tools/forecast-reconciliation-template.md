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

    Treat item-dimension fields, Lifecycle Status, Blended A-Price, baseline totals, and the rendered baseline / enrichment / prior-cycle / preliminary-forecast / sales-enrichment / marketing-and-demand-planning weekly columns as **read-only context**.

!!! note "The Level 2.5 adjustment is visible here, as read-only context"
    The forecast-partner (Level 1) template carries a read-only **L2.5 adjustment** column alongside the read-only baseline, enrichment, prior-cycle and preliminary-forecast context. In the `_ALL_FORECAST_PARTNERS_` BU-SKU template the labels invert: the editable column there is Level 2.5, and the read-only cross-level context column is labelled **L1 base trend adjustment**.

    What still holds is the **timing**: a Level 2.5 change is not visible at Level 1 until post-processing has run, which is minutes after upload (see [Timing & system sync](../workflows/timing-system-sync.md)), not instantly on save. Treat visibility and timing as two separate questions. A Level 1 user is not blind to a Level 2.5 change in their template; they may just be looking a few minutes too early.

!!! warning "Two rules to remember"
    - **Deltas, not absolutes** — reconciliation does not support an absolute overwrite. Enter a plus/minus change.
    - **One structured control per row** — do not combine an Adjusted Planning SKU (version change) and a Channel Shift Proportion on the same row.

!!! tip "Which columns do Demand Planning / Marketing edit? (incl. Level 2.5)"
    Enter your weekly adjustments in the **Baseline Trend Adjustments** columns — the **orange** ones. That is the editable weekly area on both the standard and the BU-SKU / Level 2.5 reconciliation templates. After you upload, HERO **automatically classifies** the entry and it appears under the **Marketing and Demand Planning** weekly columns — the classification is based on **who entered it and when**. So: you edit in *Baseline Trend Adjustments*, and your change shows up under *Marketing and Demand Planning* after upload. The template's **Instructions** page also covers this.

## What changed in the 20 July 2026 release

- **Clearer template layout** — cleaner labels and formatting, and **rounded display values** so the template is easier to read. (Rounding on the weekly display does not change the underlying stored values.)
- **Clearer calculated forecast totals** — the template now shows calculated totals so you can **see the effect of your entries before you upload**.
- **Level 1 / Level 2.5 behaviour tightened** — adjustments are handled more consistently between the two levels, and the template better explains **what is coming from each level**.
- **Stale or invalid planning SKUs are removed** from reconciliation templates, so you no longer see rows you cannot act on.
- **Fresh templates only** — always download a fresh template before working; avoid stale saved templates, and report any template/dashboard mismatch immediately.

!!! warning "Gaps & Open Questions"
    - Exact new column labels and the placement/format of the calculated forecast totals are not yet documented — confirm against the released template and add screenshots.
    - Confirm the precise rounding rule used for display values (and that stored values remain unrounded).
    - Confirm what "tightened" Level 1 / Level 2.5 handling changes in practice for users, if anything beyond clearer labelling.

## Actualized vs forward weeks

Weeks in the actualized period use exact row-level shipment actuals where they exist, and 0 where no exact actual is available; values are zero-floored so negative net shipment weeks render as 0. **Shaded** cells mark the actualized shipment period (historical cutoff); **unshaded** cells are forward forecast weeks.

!!! note "Channel shift moves the enrichments too"
    A Channel Shift moves demand between `DOM` and `DI`. Make sure any enrichments associated with the moved volume are also moved to the correct channel. Capture a genuine change in total demand separately.

!!! tip "Forecasting range (start / end dates)"
    To stop forecasting a SKU for a customer, adjust the **forecast calculation range** (set an end date) — distinct from a phase-out enrichment. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md).

!!! warning "Zero the Version Change / Channel Shift pair once the Forecasting Range is fixed"
    A Version Change or Channel Shift creates an offsetting +/− base-trend-adjustment pair for its week range — it never touches the baseline or forecasting range itself. The durable fix is updating the **Forecasting Range**. Once that range is fixed, the offsetting pair must be **manually zeroed**, or it persists as a delta indefinitely (fixing the range without zeroing the pair leaves you wrong for exactly one cycle, then correct).

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU / Level 2.5 mode](bu-sku-level-25-mode.md)
