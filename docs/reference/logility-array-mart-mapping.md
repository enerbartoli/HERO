<!-- docs/reference/logility-array-mart-mapping.md -->

# Logility array & mart mapping

## Who should read this page

Demand Planning, Supply-Chain COE, and anyone tracing a HERO change through to Logility.

## Purpose

Map HERO outputs to the Logility sales-forecast arrays and consensus path.

## Which direction each array travels

HERO **reads** exactly one array from Logility: `RESULTANT_FORECAST`. Everything else on this page travels one way, **HERO to Logility**. HERO never reads UA1–UA6, ADS2, PROMO_LIFT or ADS3, so a change made directly in Logility on any of them is invisible to HERO. See [Direction of travel](batch-orchestration-updates.md) for the full mechanics.

!!! note "Users author deltas; what goes out is a replacement value"
    A HERO entry is a plus or minus delta against what was there before. The export sends **complete replacement values** for the affected array and week cells, not the delta itself. HERO also rounds output to whole units at partner, SKU and week grain, which is why a BU-SKU total can differ slightly from the sum of its own partner rows once many fractional Level 2.5 fan-out cells are each rounded on their own.

| | Horizon HERO manages |
|---|---|
| UA1 | design horizon months 5–21, suppressed inside the frozen window; the current build stops publishing UA1 after month 12 (see the note below the table) |
| UA2–UA6, ADS2, PROMO_LIFT | months 0–21 |
| RESULTANT_FORECAST | not written by HERO; changed in Logility by the baseline owner |
| ADS3 | not written by HERO; calculated by Logility from its components |

!!! warning "UA1 horizon: design is 21, the build currently stops at 12"
    Month 21 is the design of record, matching UA2 to UA6, ADS2 and Promo Lift so that the Sales Forecast does not have a shorter reach than the Consensus arrays it is held equal to. Six current product-repository documents describe the built export window as stopping at month 12. **This is a known build gap, not a design change**, and Rene Bartoli is raising it with Jarred Bultema for correction. Do not teach month 12 as the target: if you observe UA1 not publishing beyond month 12 today, that is the known gap, not a defect in your own work. `[GAP: Jarred Bultema]` Confirmation that the export window has been extended to month 21.

    Separately, UA1 authoring is currently withheld inside a **frozen window** at the start of the horizon. That window is stepping down cycle by cycle and ends with the January 2027 cycle; see the [frozen window](../help/glossary.md) entry for the schedule. The frozen window and the month-12 build gap are two different limits and should not be merged into one statement.

## Sales forecast arrays

| Array | Holds | Notes |
|---|---|---|
| **UA1** | Adjusted statistical baseline, and also the Sales (Fill) Forecast | Carries the baseline, the Level 1 base-trend adjustment, the Level 2.5 base-trend adjustment (after fan-out), version adjustments, channel shift, and five UA1-mapped enrichment types: `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT`, `SUPPLY_SHORTAGE_COMP` and `NON_STATISTICAL_DEMAND`. Level 1 `MARKETING` and `DEMAND_PLANNING` enrichments from the enrichment capture template do **not** land here; adjustments from the forecast reconciliation template **do**, whoever makes them (see [what routes an entry](batch-orchestration-updates.md)). Authored by HERO in design horizon months 5–21 (see the build-gap warning above); see the [frozen window](../help/glossary.md). |
| **UA2** | Promotional activity | Promo-type sales adjustments. |
| **UA3** | Sets / initial stocking | Set-type sales adjustments. |
| **UA4** | Samples | Sample-type sales adjustments. |
| **UA5** | TMO / pallets | TMO rows. TMO passes through exactly as stored and never sums into ADS3 the way the other arrays do — it stays an independent adjustment, as it is treated in Logility today. A TMO change made in HERO still updates UA5 through the field-forecast export. |
| **UA6** | Pre-orders | Pre-order rows. |
| **UA7** | Previous-cycle sales forecast snapshot | Cycle comparison context. |
| **UA8** | Total sales forecast | Sum of UA1 through UA6. |

!!! tip "The rule behind the UA1 list, so it doesn't need re-learning when it grows again"
    If an entry is an enrichment, is not `MARKETING`, is not `DEMAND_PLANNING`, and is not explicitly mapped to UA2 through UA6, it influences **UA1**. For completeness, the explicit mappings elsewhere are `RETAIL_PROMOTION` to UA2, `SET` to UA3, `SAMPLE` to UA4, `TMO` to UA5, `PRE_ORDER` to UA6. `MARKETING` and `DEMAND_PLANNING` have no Field Forecast array of their own and contribute to Consensus only.

!!! note "`NON_STATISTICAL_DEMAND` on the Field Forecast side"
    `NON_STATISTICAL_DEMAND` maps to UA1 with a sign-based Consensus contribution, and carries three riders worth knowing on top of the mapping itself:

    - **No percentage input.** There is no baseline to resolve a percentage against, so entries are quantities only.
    - **It inherits the UA1 window.** Its Field Forecast publication follows whatever UA1's window is at the time, so it is subject to the same frozen-window step-down and the same build gap as the rest of UA1. Its Consensus contribution, by contrast, stays eligible across the full 0–21 horizon regardless.
    - **It is not separately labelled in the export change-review report.** That report classifies every UA1 change as reconciliation or base-trend-adjustment activity, so this type cannot be told apart there even though it carries its own label inside HERO.

    See [Enrichment Capture Template](../tools/enrichment-capture-template.md) for what the type captures and when to choose it over a Level 1 base trend adjustment.

## Consensus path

| Element | Definition |
|---|---|
| **RESULTANT_FORECAST** | Baseline consensus forecast before HERO changes. |
| **ADS2** | Positive HERO adjustments except TMO → mapped to enrichment quantity. |
| **PROMO_LIFT** | Negative HERO adjustments → mapped into the promoted resultant line. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT. |
| **TMO** | Consensus TMO bucket → mapped to TMO quantity. |
| **consensus_forecast_quantity** | Final consensus forecast (Logility mart column) — consensus total after HERO adjustments. |

!!! warning "The zero floor is applied on the Logility side"
    Logility prevents any Level 1 combination from being **published** negative, applying the floor on both sides (RESULTANT_FORECAST + ADS2 + PROMO_LIFT, and the UA arrays). Inside HERO the only negative restriction is on UA1; every other array carries a negative straight out. Because the floor sits on the total, a negative hidden under positive components never surfaces here — which is why you review the total preliminary forecast in HERO rather than trusting a clean-looking published number.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [Glossary](../help/glossary.md)

!!! warning "Gaps & Open Questions"
    - **UA1 export window.** `[GAP: Jarred Bultema]` Confirmation that the build has been extended from month 12 to the design horizon of month 21.
    - **The literal `NON_STATISTICAL_DEMAND` value** as it appears in the template's Enrichment Type field is unconfirmed; it follows the naming convention of every other type in this table, but has not been verified against the live template. `[GAP: Rene Bartoli]`
    - Four Logility configuration questions raised by the vendor documentation behind this page and not yet answered: the Resultant Forecast default indicator, which Sum Option is run, whether Summing Resultant runs after the Calculate Forecasts program, and whether the Adjusted Demand indicator set (`M`, `P`, `Z`) is used in history cleansing. `[GAP: Jarred Bultema / Genpact]`
