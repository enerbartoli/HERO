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
| **Shipment Channel** | The shipment route — `DOM` (domestic), `DI` (direct import), `D2C`. |
| **Level 1 (L1)** | Forecast-partner-level reconciliation. |
| **Level 2.5 (L2.5)** | BU-SKU reconciliation mode used when all forecast partners are selected. |
| **Level 3** | Broader leadership / aggregate review layer referenced in training materials. `[DRAFT — confirm with SME]` |
| **Base Trend Adjustment** | A direct week-level delta against the displayed baseline forecast. |
| **Version Change** | A net-zero move of demand from one planning SKU to another over selected weeks. |
| **Channel Shift** | A move of some or all demand between `DOM` and `DI` over selected weeks. |
| **TMO** | Trade / pallet adjustment that travels through the UA5 / TMO path. |
| **SPU** | Special Planning Unit — optional tracking metadata on TMO rows. |
| **GPL** | Global Product Lead. `[DRAFT — confirm canonical expansion]` |
| **Phase-Out** | An enrichment used when an item should no longer behave like a normal carry-forward baseline. |
| **Actualized period** | The historical portion of the year where the workbook shows exact shipment actuals when they exist. |
| **RESULTANT_FORECAST** | The baseline consensus forecast before HERO adjustments. |
| **ADS2** | Positive HERO adjustments other than TMO in the consensus path. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT. |
| **PROMO_LIFT** | Negative HERO adjustments in the consensus path. |
| **UA1–UA8** | Logility sales-forecast arrays — see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md). |

!!! question "Gaps & Open Questions"
    - Confirm canonical expansions for **GPL** and the **Level 3** review layer.
