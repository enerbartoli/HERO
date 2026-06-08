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
| `EXCESS_DEPLETION` | Depletion-style adjustment (excess inventory) | — |
| `DEMAND_PHASE_SHIFT` | Timing-issue tracking badge (tracking only) | — |
| `SUPPLY_SHORTAGE_COMP` | Compensating item for a shortage | Shortage Planning SKU |
| `MARKETING` | Marketing overlay | `ALL_FORECAST_PARTNERS` allowed |
| `DEMAND_PLANNING` | Demand-planning overlay | `ALL_FORECAST_PARTNERS` allowed |

!!! note "Status values"
    `PROPOSED` = planned / working input · `CONFIRMED` = approved active input · `DECLINED` = retained for traceability but not active.

!!! warning "Tracking-only types"
    `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP` are **tracking metadata**. They do **not** automatically move demand between weeks or between SKUs. Use reconciliation for an actual week move.

!!! note "TMO comes from FAST"
    `TMO` rows are sourced from **FAST** and the template is seeded from FAST once a month. Do **not** author or edit TMO directly in the template — that would desynchronise FAST and Logility.

!!! tip "Confirmed vs Proposed horizon"
    Use `CONFIRMED` for near-term events inside the supply window; use `PROPOSED` for longer-horizon events that are not yet locked. `EXCESS_DEPLETION` and `PHASE_OUT` are separate types in the tool; "Phase-Out" is the business term for taking an item off normal carry-forward, and excess-inventory depletion is captured the same way.

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
