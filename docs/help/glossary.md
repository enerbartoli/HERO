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
| **Cleansing** | Correction of the **Adjusted Demand array** so the statistical baseline learns real demand rather than what shipped. It runs in the opposite direction to the enrichment — when a period closes, cleansed history is actual shipments minus the `SET` — and never touches raw Actuals. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works). |
| **Frozen window** | The rolling lead-time horizon at the start of the UA1 authoring window, inside which HERO withholds UA1 authoring. It is stepping down cycle by cycle rather than staying fixed at months 0 to 4: September 2026 protects months 0 to 3, October protects 0 to 2, November protects 0 to 1, December protects month 0 only, and from the January 2027 cycle there is no protection and HERO writes UA1 from month 0. The window itself does not disappear; what ends is HERO holding UA1 back inside it. The step-down is agreed direction for both pilot markets (United States and United Kingdom); it does not extend to markets that are not yet live on HERO. Inside the frozen window, the published value currently carries the current live Logility **baseline**, not the live UA1 array; the intent is to carry the live UA1 array, and the difference is a known gap that narrows as the step-down proceeds and closes when it completes. HERO authors UA1 in design horizon months 5 to 21, though the current build stops publishing UA1 after month 12, a build gap rather than a horizon change (see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md)). |
| **Version Change** | A net-zero move of demand from one planning SKU to another over selected weeks. |
| **Channel Shift** | A move of some or all demand between `DOM` and `DI` over selected weeks. |
| **TMO** | Trade / pallet adjustment that travels through the UA5 / TMO path. Sourced from FAST. |
| **FAST** | The upstream system that is the source of truth for TMO; the ECT is seeded from it. |
| **SPU** | Special Planning Unit — optional tracking metadata on TMO rows. |
| **Phase-out** (`PHASE_OUT` in the tool) | An enrichment type captured in the enrichment capture template, used when an item should no longer behave like a normal carry-forward baseline (maps the depletion of available inventory). It is one of the UA1-mapped components (see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md) for the full UA1 composition) and also flows to consensus by sign — positive values to ADS2, negative values to PROMO_LIFT. **Phase-out is the canonical name** (confirmed by Rene Bartoli, 12 July 2026); `PHASE_OUT` is that same name as it appears in the tool/enrichment-type field. `MDP_ENRICHMENT` is a legacy synonym found in older architecture material (Transmission Design Topics V1) and should not be used as current terminology. |
| **Forecast Calculation Range** (also called "forecasting range") | A continuous period, one start date and one end date, not a year bucket: every period outside those two dates is out of range whatever calendar year it falls in. Defines **which customer and which periods receive part of the resultant**, the baseline; setting an end date stops future forecasting for that SKU/customer. Distinct from the **portfolio extension**, which defines which customers can hold forecast for a SKU at all, whether or not that forecast was generated statistically. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md). |
| **Management Indicator** | The per-item, per-level, per-week flag that tells Logility how to treat a period's forecast when it sits outside the Forecast Calculation Range. `M` (Manual) means the planner owns the number and an out-of-range value is preserved. `H` (Historical) means the statistical model owns it and an out-of-range value is removed. It is the same field Logility calls the Resultant Forecast Override Indicator; Hasbro uses two of its six user-settable values. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md). |
| **`NON_STATISTICAL_DEMAND`** | An enrichment type capturing the full forecast volume for a part of the portfolio a market has agreed not to forecast statistically. Maps to UA1 on the Field Forecast side, with a sign-based Consensus contribution. See [Enrichment Capture Template](../tools/enrichment-capture-template.md). |
| **Summing program** | The Logility pass that brings the sum of the children up to the parent record, operating only on Resultant Forecasts. It is **not** governed by the Forecast Calculation Range, which is why a value already sitting at a lower level survives the range and rolls up into a total that does not reconcile with the range supposedly governing it. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md). |
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
