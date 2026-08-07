<!-- docs/help/glossary.md -->

# Glossary

## Who should read this page

All users. Every acronym used in HERO, expanded.

## Purpose

Single reference for HERO terms and acronyms.

| Term | Definition |
|---|---|
| **HERO** | Hasbro Enrichment & Reconciliation Optimizer — the business-user capture layer between Logility baselines and published forecast changes. |
| **ECT** | Enrichment Capture Template — the workbook path for event-driven enrichments. |
| **FRT** | Forecast Reconciliation Template — the workbook path for adjusting final week-level numbers. |
| **Business Unit (BU)** | The geography / organizational slice used throughout HERO. |
| **Forecast Partner** | The customer / retailer Hasbro forecasts shipments for. |
| **Planning SKU** | The planning item code HERO uses as the item identifier. |
| **Shipment Channel** | The shipment route — `DOM` (domestic) or `DI` (direct import). |
| **KAM** | Key Account Manager (Sales). |
| **GPL** | Global Product Lead (a commercial / marketing role). |
| **Level 1 (L1)** | Forecast-partner / customer-level reconciliation. |
| **Level 2.5 (L2.5)** | BU-SKU reconciliation mode used when all forecast partners are selected. |
| **SKU hierarchy levels** | Nodes in the item hierarchy: L5 Brand/BU · L4 Global SKU/BU · L3 Parent SKU/BU/Channel · L2 Planning SKU/Customer · L1 Planning SKU/Customer/Channel. "Level 3" is a hierarchy node (e.g. Parent SKU / BU / Channel), **not** a review stage; the later-stage review stage is Level 2.5 / BU-SKU. |
| **Base Trend Adjustment** | A direct week-level delta against the displayed baseline forecast. Persists across cycles until manually reversed — it is not a single-cycle entry. At Level 2.5 it disaggregates across **all** forecast partners by baseline proportion; it cannot be targeted at one account. |
| **Frozen window** | The rolling lead-time horizon — months 0–4 counted from the current date, every cycle, not a one-off period after go-live — inside which HERO withholds UA1 authoring and the published value carries the live Logility UA1 / baseline instead. HERO authors UA1 in horizon months 5–21. |
| **Version Change** | A net-zero move of demand from one planning SKU to another over selected weeks. |
| **Channel Shift** | A move of some or all demand between `DOM` and `DI` over selected weeks. |
| **TMO** | Trade / pallet adjustment that travels through the UA5 / TMO path. Sourced from FAST. |
| **FAST** | The upstream system that is the source of truth for TMO; the ECT is seeded from it. |
| **SPU** | Special Planning Unit — optional tracking metadata on TMO rows. |
| **Phase-out** (`PHASE_OUT` in the tool) | An enrichment type captured in the enrichment capture template, used when an item should no longer behave like a normal carry-forward baseline (maps the depletion of available inventory). It is one of the UA1-mapped components (see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md) for the full UA1 composition) and also flows to consensus by sign — positive values to ADS2, negative values to PROMO_LIFT. **Phase-out is the canonical name** (confirmed by Rene Bartoli, 12 July 2026); `PHASE_OUT` is that same name as it appears in the tool/enrichment-type field. `MDP_ENRICHMENT` is a legacy synonym found in older architecture material (Transmission Design Topics V1) and should not be used as current terminology. |
| **Forecasting range** | The start / end dates over which a SKU is forecast for a partner; setting an end date stops future forecasting for that SKU/customer. |
| **Actualized period** | The historical portion of the year where the workbook shows exact shipment actuals when they exist. |
| **RESULTANT_FORECAST** | The baseline consensus forecast before HERO adjustments. |
| **ADS2** | Positive HERO adjustments other than TMO in the consensus path. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT, calculated by Logility. HERO never reads it and never writes it. |
| **Zero floor** | Logility's rule that no Level 1 combination is published negative. It is applied on the Logility side, on the total, so a negative sitting under positive components never surfaces downstream. Inside HERO only UA1 restricts negatives. |
| **One-way flow** | HERO reads only `RESULTANT_FORECAST` from Logility. Every other array travels HERO to Logility only, which is why a change made directly in Logility never reaches HERO. |
| **PROMO_LIFT** | Negative HERO adjustments in the consensus path. |
| **UA1–UA8** | Logility sales-forecast arrays — see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md). |
| **P2M** | The source used to derive on-shelf dates / quantities that seed the forecasting range. |

!!! success "No open questions identified"
    No open questions were identified from the available source material.
