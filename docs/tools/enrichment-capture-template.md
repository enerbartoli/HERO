<!-- docs/tools/enrichment-capture-template.md -->

# Enrichment Capture Template (ECT)

## Who should read this page

Sales / KAM and Marketing / GPL users who author event-driven enrichments; Demand Planning when reviewing.

## Purpose

Explain when to use the **Enrichment Capture Template (ECT)** and which enrichment types it supports.

## When to use it

Use the enrichments workflow when you have a **real-world event or overlay** tied to an item, channel, and time period — promotions, sets, pre-orders, Trade / pallet adjustments (TMO), marketing inputs, and demand-planning overlays.

!!! tip "Enrichments vs reconciliation"
    Use **enrichments** for dated business events. Use **reconciliation** when the ask is effectively *"change the final number for these weeks."* See [Forecast Reconciliation Template (FRT)](forecast-reconciliation-template.md).

## Supported enrichment types

| Type | Use for | Required extra field |
|---|---|---|
| `RETAIL_PROMOTION` | Promo / retail event | Retail Promotion Mechanism; Price Discount % when relevant |
| `SET` | Set build / one-time pipeline fill | — |
| `SAMPLE` | Free sample volume | — |
| `PRE_ORDER` | Committed launch volume | — |
| `TMO` | Trade / pallet adjustment | Pallet Tag; SPU SKU optional |
| `PHASE_OUT` | Item should no longer carry a normal baseline | — |
| `EXCESS_DEPLETION` | Legacy depletion-style adjustment `[DRAFT — confirm with SME]` | — |
| `DEMAND_PHASE_SHIFT` | Timing-issue tracking badge (pilot only) | — |
| `SUPPLY_SHORTAGE_COMP` | Compensating item for a shortage | Shortage Planning SKU |
| `MARKETING` | Marketing overlay | `ALL_FORECAST_PARTNERS` allowed |
| `DEMAND_PLANNING` | Demand-planning overlay | `ALL_FORECAST_PARTNERS` allowed |

!!! note "Status values"
    `PROPOSED` = planned / working input · `CONFIRMED` = approved active input · `DECLINED` = retained for traceability but not active.

!!! warning "Tracking-only types"
    `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP` are **tracking metadata** in the pilot. They do **not** automatically move demand between weeks or between SKUs. Use reconciliation for an actual week move.

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)

!!! question "Gaps & Open Questions"
    - Clarify whether `EXCESS_DEPLETION` is retained or folded into `PHASE_OUT` before pencils-down.
