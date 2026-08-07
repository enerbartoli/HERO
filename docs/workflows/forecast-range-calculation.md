<!-- docs/workflows/forecast-range-calculation.md -->

# Forecast Calculation Range & Disaggregation

## Who should read this page

Sales / Key Account Managers (KAMs), Demand Planning (DP), and Brand Captains — anyone whose item should be forecast for some customers and periods but not others.

## Purpose

Explain what the **Forecast Calculation Range (FCR)** is, how it is generated and adjusted, and why it matters for **disaggregation** — how the baseline is split down to customers.

!!! note "Name"
    The canonical term is **Forecast Calculation Range**. An underlying pipeline guide informally calls it "Forecast Calendar Range"; treat *Calculation* as canonical.

## What the forecast range is

The FCR is a **per-product window of Start and End weeks** that tells Logility when a product should be planned: *"this product should be available from week X to week Y."* It is the gate that decides which weeks — and, at customer level, which customers — receive a forecast.

## How the range is generated

The range is built bottom-up in four steps, starting from launch data:

1. **Planning SKU dates** — extract on-shelf dates and quantities from **P2M**, then apply region- and channel-specific **lead-time** logic to work out when items must ship to be available. End dates are extrapolated from the last year with P2M quantities.
2. **Level 1 (partner)** — the dates are replicated and adjusted per forecast partner.
3. **Level 2 (Parent SKU)** — aggregated using the **earliest Start and latest End** across items sharing the parent SKU, partner, and channel.
4. **Level 3** — extended to Parent SKU + Business Unit; this is the file loaded into Logility.

After initial load, **Logility is the source of truth** for the range.

## How you control / adjust it

Commercial teams receive **Excel files with the proposed Start/End dates** for each SKU and forecast partner and **adjust them manually** using customer knowledge — delayed launches, exclusivity, and so on. The Level 1 files carry blank "New Start / End Date" override columns and a **status flag** showing whether the range matches Logility or differs. The adjusted dates are then updated in Logility.

## Why it matters for disaggregation

!!! warning "Default spread causes bad forecasts"
    By default a SKU can extend to **all** forecast partners, which spreads demand to customers that will never take it. The range is how you include **only the relevant customers**.

- **Exclusives** — for a single-customer SKU (e.g. an Amazon exclusive), **set/adjust the end date** so other partners are excluded and the forecast does not spread to them.
- **Stopping a SKU for a customer** — set an end date to stop forecasting that SKU/customer. This is distinct from a phase-out enrichment (which takes the item off normal carry-forward more broadly).
- **Missing or inactive items lose forecast** — if a SKU is inactive or missing at any hierarchy level during disaggregation, the system can assign **zeros**, losing the forecast. Complete, accurate data at every level is required for correct allocation.

## Scope, validation, and data quality

- Both **8-digit and 9-digit (wave) SKUs** are processed by the range pipeline.
- SKUs **without supporting P2M data** are **deactivated**, and files are generated to classify the reason for the missing dates.
- If a computed **End Date falls before the Start Date**, the row is flagged as a data issue for review.
- Regional teams run **periodic P2M audits** to remove invalid or outdated entries.

## How it relates to the baseline

The statistical model output is generated **first** (forecast before range), and the **range layer is then applied** on top.

## How history cleansing works

Cleansing is how the model is told what really happened, as opposed to what shipped. It is applied in the **Adjusted Demand array**, the editable layer the statistical baseline learns from, and never in raw Actuals.

**The mechanic.** Cleansing runs in the **opposite direction to the enrichment**. When a period closes, cleansed history is actual shipments minus the `SET`. Base trend adjustments are **not** cleansed: they adjust the forward baseline and never enter the cleansing calculation.

That is why a `SET` does two jobs at once. It holds volume in the forecast now, and it is the instruction that removes that same volume from history later. It is also why a pair of offsetting `SET` rows nets to zero in cleansing, which is correct when demand only moved between weeks and nothing new was created, and wrong when the point is to strip a volume out of what the model learns.

**Supply shortage compensation.** When a shortage pushes demand onto a substitute item, `SUPPLY_SHORTAGE_COMP` records the relationship between the item that was unavailable and the item that absorbed the demand. At cleansing, that relationship raises the adjusted demand of the item that was unavailable by the compensating quantity, and reduces the same quantity from the substitute. The model then learns the demand the absent item would have had, and does not carry forward an inflated projection for a substitute that only sold because of the shortage.

Capturing that relationship correctly matters even though nothing moves in the forward forecast: the intent is to use it to **automate** the historical cleansing, so the correction happens without a planner having to reconstruct it by hand.

!!! note "This is the initial logic, and it is expected to change"
    The rules on this page are the starting point, not a finished design. They will evolve as the programme accumulates enough cycles to evaluate which cleansing treatment actually improves forecast accuracy. Two objectives guide that evolution: cleansing should measurably improve accuracy, and it should be automated far enough that it does not consume planner time. Treat the current rules as the working method and expect them to be refined.

## Related pages

- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — the in-template "set an end date to stop forecasting" usage.
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md) — note the difference: the **range** decides *which customers* receive a forecast; **Level 2.5** decides *how an aggregate adjustment is split* across them.
- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
