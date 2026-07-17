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
| `DEMAND_PHASE_SHIFT` | Re-phasing demand between weeks (pull-forward / push-out, e.g. deals): author a **positive + negative pair** — a positive row where the demand lands, a negative row where it is taken from | — |
| `SUPPLY_SHORTAGE_COMP` | Compensating item for a shortage | Shortage Planning SKU |
| `MARKETING` | Marketing overlay | `ALL_FORECAST_PARTNERS` allowed |
| `DEMAND_PLANNING` | Demand-planning overlay | `ALL_FORECAST_PARTNERS` allowed |

!!! note "Status values"
    `PROPOSED` = planned / working input · `CONFIRMED` = approved active input · `DECLINED` = preserved for visibility in the template and audit trail, but **excluded from calculated downstream outputs**. As of the **20 July 2026 release**, setting a row to `DECLINED` is the recommended way to remove its effect — see *Cancelling or removing an enrichment* below.

!!! tip "Re-phasing demand: use DEMAND_PHASE_SHIFT, not SET (ratified, 16 July 2026)"
    When the business decision is to **move existing demand between weeks** (deals, pull-forwards, ladder buys — and in general demand timing changes that do **not** originate from problems in history), use a `DEMAND_PHASE_SHIFT` **positive + negative pair** instead of `SET`. Reserve `SET` for a **true set build**; if a true set build also pulls existing demand forward, offset it with **negative `SET` rows** on the weeks the demand comes from — the same enrichment type for both legs, consistent with the ladder rule (DPS pair) and the NPI set/baseline case (simplification confirmed 16 July 2026).

!!! note "Boundary with reconciliation"
    If the phasing issue stems from the **baseline / history** — defects or one-off events in history whose adjustment was not made in time, or that cannot be explained by commercial actions — correct it through **reconciliation** (base trend adjustment), not an enrichment. `DEMAND_PHASE_SHIFT` is for known commercial timing events; reconciliation is for history-driven baseline corrections.

!!! warning "No single-row move; SUPPLY_SHORTAGE_COMP stays tracking-only"
    A single `DEMAND_PHASE_SHIFT` row does **not** automatically move demand — it takes **two rows** (positive where the demand lands, negative where it comes from). Do **not** confuse it with **Channel Shift** (a reconciliation control): Channel Shift moves demand between channels (`DOM` ↔ `DI`) and creates the offsetting negative **automatically**; `DEMAND_PHASE_SHIFT` moves demand between **weeks** and both legs are authored manually. `SUPPLY_SHORTAGE_COMP` remains **tracking metadata**: it does not move volume between SKUs.

!!! note "TMO comes from FAST"
    `TMO` rows are sourced from **FAST** and the template is seeded from FAST once a month. Do **not** author or edit TMO directly in the template — that would desynchronise FAST and Logility.

!!! tip "Confirmed vs Proposed horizon"
    Use `CONFIRMED` for near-term events inside the supply window; use `PROPOSED` for longer-horizon events that are not yet locked. `EXCESS_DEPLETION` and `PHASE_OUT` are separate types in the tool; "Phase-Out" is the business term for taking an item off normal carry-forward, and excess-inventory depletion is captured the same way.

## Working in the template (Excel, formulas, copying data)

The HERO templates are **ordinary Excel files** — while you prepare your entries you can use anything Excel offers: copy/paste from other files, `VLOOKUP` and other formulas, and so on. Before you **upload** the file to HERO, take these precautions (mostly good practice, not always hard rules):

- **Don't overwrite rows.**
- **Replace any formulas with their values** before uploading (copy → paste as values). The upload expects static values, not live formulas.
- **Avoid blank rows** — don't leave empty lines between enrichments. As of the **20 July 2026 release**, upload validation detects mid-sheet blank rows (and blanked headers) and rejects the upload with an explanation, instead of silently dropping the data below them.
- **Insert any new or copied row below the last row that has data.**

## Cancelling or removing an enrichment

!!! warning "Never delete rows"
    Do **not** delete enrichment rows. Every enrichment must stay traceable through its key (Enrichment ID) — deleting a row breaks that audit trail.

As of the **20 July 2026 release**, the recommended way to cancel an enrichment is to set its **Status** to `DECLINED`. A `DECLINED` row is preserved in the template and the audit trail for visibility, but is **excluded from calculated downstream outputs** — its effect is removed from the forecast while the record of the decision remains.

!!! note "Previous method: zeroing the quantity"
    Before the 20 July 2026 release, Status was a log-only field and the only way to remove an enrichment's effect was to **zero the quantity** (set *Expected Shipment Lift* to 0). Zeroing still removes the effect, but `DECLINED` is now the preferred method because it removes the effect *and* records the decision explicitly in the audit trail.

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)

!!! warning "Gaps & Open Questions"
    - The 16 July 2026 decision is **formally ratified**; taxonomy and training sources were corrected the same day (Taxonomy Playbook v2, Examples for Enrichment Training v2, Enrichment Training Examples Deck v2, Scenarios & Examples v2, MOD2 deck v4, EU Day1 deck v3). Superseded versions should be retired/archived so only the 2026-07-16 versions circulate.
