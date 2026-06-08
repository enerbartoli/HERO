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
| **Base Trend Adjustment** | A direct week-level delta against the displayed baseline forecast. |
| **Version Change** | A net-zero move of demand from one planning SKU to another over selected weeks. |
| **Channel Shift** | A move of some or all demand between `DOM` and `DI` over selected weeks. |
| **TMO** | Trade / pallet adjustment that travels through the UA5 / TMO path. Sourced from FAST. |
| **FAST** | The upstream system that is the source of truth for TMO; the ECT is seeded from it. |
| **SPU** | Special Planning Unit — optional tracking metadata on TMO rows. |
| **Phase-Out** | An enrichment used when an item should no longer behave like a normal carry-forward baseline (also used to deplete excess inventory). |
| **Forecasting range** | The start / end dates over which a SKU is forecast for a partner; setting an end date stops future forecasting for that SKU/customer. |
| **Actualized period** | The historical portion of the year where the workbook shows exact shipment actuals when they exist. |
| **RESULTANT_FORECAST** | The baseline consensus forecast before HERO adjustments. |
| **ADS2** | Positive HERO adjustments other than TMO in the consensus path. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT. |
| **PROMO_LIFT** | Negative HERO adjustments in the consensus path. |
| **UA1–UA8** | Logility sales-forecast arrays — see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md). |
| **P2M** | The source used to derive on-shelf dates / quantities that seed the forecasting range. |

!!! success "No open questions identified"
    No open questions were identified from the available source material.
