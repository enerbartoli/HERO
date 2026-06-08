<!-- docs/reference/logility-array-mart-mapping.md -->

# Logility array & mart mapping

## Who should read this page

Demand Planning, Supply-Chain COE, and anyone tracing a HERO change through to Logility.

## Purpose

Map HERO outputs to the Logility sales-forecast arrays and consensus path.

## Sales forecast arrays

| Array | Holds | Notes |
|---|---|---|
| **UA1** | Baseline sales forecast after reconciliation adjustments | Reconciliation deltas, version changes, and channel shifts land here. |
| **UA2** | Promotional activity | Promo-type sales adjustments. |
| **UA3** | Sets / initial stocking | Set-type sales adjustments. |
| **UA4** | Samples | Sample-type sales adjustments. |
| **UA5** | TMO / pallets | TMO rows. |
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

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [Glossary](../help/glossary.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
