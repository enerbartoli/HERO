<!-- docs/examples/calculation-reference.md -->

# Calculation reference (worked examples)

## Who should read this page

Anyone who needs to predict what a number will do after an enrichment or reconciliation entry — Sales, Demand Planning, Marketing / GPL.

## Purpose

Show, with worked numbers, how HERO resolves enrichments and reconciliation into the final forecast.

## Foundational concept: baseline + enrichment = consensus

!!! note "Two layers, one number"
    **Baseline** is what the statistical model produces from history alone — pattern, trend, seasonality (owned by Demand Planning). **Enrichment** is the business knowledge layered on top — promos, sets, base trend, channel shifts — that the model cannot infer from history (owned by Sales + Brand Captain). The **consensus forecast** is the agreed number, with every adjustment traceable to its driver and owner. Neither layer is a place to reconcile to a target number; both are evidence-based.

## Key principle: Set vs Base Trend

The single most important modelling choice in enrichment is whether an adjustment should **cleanse out of history** or **enter the baseline permanently**.

| | Commercial building block (e.g. Set) | Base Trend Adjustment |
|---|---|---|
| **Effect** | One-time; removed from history after the period | Structural; becomes part of the baseline going forward |
| **Next year's model** | Will **not** learn it | **Will** learn it as normal |
| **Use for** | Pipeline fills, out-of-aisle, ladders / timing shifts, pre-orders, one-off substitutions, fan spikes | POD expansion / reduction, customer discontinued, recurring year-over-year temporality, ongoing run-rate corrections |

!!! warning "Common mistake"
    Using a Base Trend Adjustment to handle a **timing** move (a ladder or a lumpy buy). It cleanses correctly the first cycle, but the negative leg permanently distorts the baseline. **When in doubt — if the change is one-time, use a Set.**

## 1. Units lift vs percent lift

Baseline = 100 units/week; event covers weeks 5–15 inclusive (**11 covered weeks**).

- **Percent (+10%):** resolved against baseline first → each week gets 100 × 10% = **10 units**; total lift = **110 units**.
- **Units (+1,200):** spread evenly → each week gets 1,200 / 11 = **109.09 units** (before display/export rounding).

!!! tip "Coverage is by fiscal week, not daily proration"
    HERO expands enrichments by fiscal-week coverage. A mid-week start/end date still allocates by the fiscal weeks whose start dates fall inside the range.

## 2. Current-cycle enriched forecast

For one week: Baseline 100 + Base Trend Adjustment 15 + Sales Enrichment 20 + Marketing & DP 5 = **140 units**.

## 3. Version change (net-zero SKU move)

Source SKU = 200 units/week for weeks 10–12; Adjusted Planning SKU = target; Start Wk 10, End Wk 12. HERO derives a **negative delta** on the source and a matching **positive delta** on the target for those weeks. Use the structured Version Adjustment controls — do not zero rows manually, and do not combine with a channel shift.

## 4. Channel shift

Weekly resolved demand = 100 units/week; Channel Shift Proportion = 0.25; weeks 12–20. HERO moves **25 units/week** from the source channel to the opposite channel. If total demand is also changing, capture that separately.

## 5. BU-SKU (Level 2.5) disaggregation back to Level 1

Current BU-SKU week-10 adjustment total = 150; user edits it to 100 → required net change = **−50**. Baseline shares: FP A 50%, FP B 30%, FP C 20%. HERO redistributes: FP A −25, FP B −15, FP C −10. (If all eligible baselines are zero, HERO splits evenly.) See [BU-SKU worked examples](bu-sku-worked-examples.md) for what moves afterward.

## 6. Enrichment-to-consensus aggregation

One series-week: RESULTANT_FORECAST 100, Promo +20, Marketing +10, TMO +5 → positive non-TMO enrichments contribute +30 to the positive HERO adjustment path; TMO stays in the TMO path → final consensus = 100 + 30 + 5 = **135**.

## Worked scenario examples (Module 2)

!!! example "Historical promo spike that is not repeating"
    Last year's spike is baked into the trend, so the stat model overstates F1–F4. **Use a negative Base Trend Adjustment** for the contaminated period only; the corrected baseline returns to the true run-rate. Owner: Brand Captain / DP.

!!! example "Recurring year-over-year temporality missing"
    A seasonal pattern is not reflected because prior history did not capture it cleanly. **Use a Base Trend Adjustment** (not a one-off set) so the model learns it permanently and the correction is not re-entered each cycle. Owner: Sales.

!!! note "Rounding on export"
    Internally a unit spread can be fractional (e.g. 109.09 units/week). On export, published values are **rounded to the nearest whole integer**, with halves rounding **away from zero**. Published outputs are fully populated (no blank cells).

## Related pages

- [BU-SKU worked examples](bu-sku-worked-examples.md)
- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
