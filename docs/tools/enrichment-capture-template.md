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
| `NON_STATISTICAL_DEMAND` | Full forecast volume for a part of the portfolio a market has agreed **not** to forecast statistically | — |
| `MARKETING` | Marketing overlay | `ALL_FORECAST_PARTNERS` allowed |
| `DEMAND_PLANNING` | Demand-planning overlay | `ALL_FORECAST_PARTNERS` allowed |

!!! note "Status values"
    `PROPOSED` = planned / working input · `CONFIRMED` = approved active input · `DECLINED` = preserved for visibility in the template and audit trail, but **excluded from calculated downstream outputs**. As of the **20 July 2026 release**, setting a row to `DECLINED` is the recommended way to remove its effect — see *Cancelling or removing an enrichment* below.

!!! tip "Re-phasing demand: use DEMAND_PHASE_SHIFT, not SET (ratified, 16 July 2026)"
    When the business decision is to **move existing demand between weeks** (deals, pull-forwards, ladder buys — and in general demand timing changes that do **not** originate from problems in history), use a `DEMAND_PHASE_SHIFT` **positive + negative pair** instead of `SET`. Reserve `SET` for a **true set build**; if a true set build also pulls existing demand forward, offset it with **negative `SET` rows** on the weeks the demand comes from — the same enrichment type for both legs, consistent with the ladder rule (DPS pair). That `SET` pair does **not** cover the case where the baseline already carries the fill — see *NPI channel fill* below.

!!! tip "NPI channel fill: negative base trend plus positive SET (corrected, 7 August 2026)"
    When the Daybreak New Product Introduction (NPI) launch baseline **already embeds the channel fill** in its curve, this is not a `SET` pair. Enter a **negative base trend adjustment in F1** for the excess the baseline encoded, plus a **positive `SET` of equal magnitude in F1** to make the fill visible as a discrete commitment for allocation and supply sizing. Both legs sit on exactly the same weeks — the launch window — so neither carries into the next cycle and neither needs manual retirement.

    The leg types differ on purpose. Base trend adjustments are not cleansed from history; they adjust the forward baseline. History cleansing runs in the **opposite direction** to the enrichment, so cleansed history is actual shipments minus the `SET`, which leaves replenishment demand only and stops the model relearning the fill next year. Two offsetting `SET` rows would hold the F1 total just as well, but they net to zero in the cleansing calculation and the fill would be relearned.

    The two magnitudes do not have to match: the negative base trend is the excess the baseline assumed, the positive `SET` is the fill actually agreed, and where they differ the total moves, which is correct. True up the `SET` against the fill actually shipped before the period closes, or the residual enters next year's baseline.

    Where the baseline does **not** carry the fill — new distribution, new stores, a partner the baseline has never served — there is no excess to correct, so no negative base trend. Enter a positive `SET` for the one-time fill, and if the new distribution also lifts the ongoing run rate, capture that lift as a separate positive base trend adjustment. The question that separates the two cases is simply: does the baseline already carry this volume?

!!! note "Boundary with reconciliation"
    If the phasing issue stems from the **baseline / history** — defects or one-off events in history whose adjustment was not made in time, or that cannot be explained by commercial actions — correct it through **reconciliation** (base trend adjustment), not an enrichment. `DEMAND_PHASE_SHIFT` is for known commercial timing events; reconciliation is for history-driven baseline corrections.

!!! warning "No single-row move; SUPPLY_SHORTAGE_COMP stays tracking-only"
    A single `DEMAND_PHASE_SHIFT` row does **not** automatically move demand — it takes **two rows** (positive where the demand lands, negative where it comes from). Do **not** confuse it with **Channel Shift** (a reconciliation control): Channel Shift moves demand between channels (`DOM` ↔ `DI`) and creates the offsetting negative **automatically**; `DEMAND_PHASE_SHIFT` moves demand between **weeks** and both legs are authored manually. `SUPPLY_SHORTAGE_COMP` remains **tracking metadata**: it does not move volume between SKUs. Tracking-only refers to the forward forecast. The relationship it records is used at history cleansing, where it raises the adjusted demand of the item that was unavailable and reduces the same quantity from the substitute. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works).

!!! tip "NON_STATISTICAL_DEMAND: a label of its own for volume with no baseline to sit on"
    Use `NON_STATISTICAL_DEMAND` for a part of the portfolio a market has agreed **not** to forecast statistically. It captures the **full forecast volume** for that segment, so it carries a label of its own instead of being indistinguishable from an adjustment layered on top of a baseline. What decides scope is the market-level agreement, not the channel and not the item class; today that means Direct Import and FAN in the UK pilot, and FAN in the United States.

    <!-- TODO: confirm with Rene --> The literal value as it appears in the template's Enrichment Type field. `NON_STATISTICAL_DEMAND` follows the convention of every other type on this page, but the exact string has not been confirmed against the live template.

    **It does not retire the base-trend route.** A market whose non-statistical demand is recurring at SKU and customer level may reasonably prefer to keep using a Level 1 base trend adjustment for it instead, and choosing that is not an error. Both routes are supported, and which one to use is the market's call, not a rule this manual sets. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md) and [Logility array & mart mapping](../reference/logility-array-mart-mapping.md) for how the type behaves once captured, including that it is not separately labelled in the export change-review report.

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
