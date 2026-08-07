<!-- docs/reference/logility-array-mart-mapping.md -->

# Logility array & mart mapping

## Who should read this page

Demand Planning, Supply-Chain COE, and anyone tracing a HERO change through to Logility.

## Purpose

Map HERO outputs to the Logility sales-forecast arrays and consensus path.

## Which direction each array travels

HERO **reads** exactly one array from Logility: `RESULTANT_FORECAST`. Everything else on this page travels one way, **HERO to Logility**. HERO never reads UA1–UA6, ADS2, PROMO_LIFT or ADS3, so a change made directly in Logility on any of them is invisible to HERO. See [Direction of travel](batch-orchestration-updates.md) for the full mechanics.

| | Horizon HERO manages |
|---|---|
| UA1 | months 5–21 (suppressed inside the 0–4 frozen window) |
| UA2–UA6, ADS2, PROMO_LIFT | months 0–21 |
| RESULTANT_FORECAST | not written by HERO; changed in Logility by the baseline owner |
| ADS3 | not written by HERO; calculated by Logility from its components |

## Sales forecast arrays

| Array | Holds | Notes |
|---|---|---|
| **UA1** | Adjusted statistical baseline, and also the Sales (Fill) Forecast | Carries the baseline, the Level 1 base-trend adjustment, the Level 2.5 base-trend adjustment (after fan-out), version adjustments, channel shift, and the UA1-mapped enrichment types `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. Level 1 `MARKETING` and `DEMAND_PLANNING` enrichments from the enrichment capture template do **not** land here; adjustments from the forecast reconciliation template **do**, whoever makes them (see [what routes an entry](batch-orchestration-updates.md)). Authored by HERO in horizon months 5–21; see the [frozen window](../help/glossary.md). |
| **UA2** | Promotional activity | Promo-type sales adjustments. |
| **UA3** | Sets / initial stocking | Set-type sales adjustments. |
| **UA4** | Samples | Sample-type sales adjustments. |
| **UA5** | TMO / pallets | TMO rows. TMO passes through exactly as stored and never sums into ADS3 the way the other arrays do — it stays an independent adjustment, as it is treated in Logility today. A TMO change made in HERO still updates UA5 through the field-forecast export. |
| **UA6** | Pre-orders | Pre-order rows. |
| **UA7** | Previous-cycle sales forecast snapshot | Cycle comparison context. |
| **UA8** | Total sales forecast | Sum of UA1 through UA6. |

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

!!! success "No open questions identified"
    No open questions were identified from the available source material.
