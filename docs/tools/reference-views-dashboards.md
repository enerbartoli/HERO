<!-- docs/tools/reference-views-dashboards.md -->

# Reference views & dashboards

## Who should read this page

All users who consume resolved outputs: Sales, Demand Planning (DP), Marketing / Global Product Lead (GPL), Finance, and Supply Chain.

## Purpose

Describe the Power BI views that present resolved HERO (Hasbro Enrichment & Reconciliation Optimizer) outputs, and how they refresh.

!!! warning "Timing"
    Resolved dashboards refresh **after the backend processing run completes** — they can lag a successful upload. The workbook shows authored intent immediately after download; dashboards match only after the resolved refresh.

## Forecast Enrichment Power BI dashboard

Provides visualisations of baseline forecasts, enrichments, consensus forecasts, and key performance indicators, with drill-down to SKU-level detail. Domestic (DOM) and Direct Import (DI) data are separated; DI forecasts are reflected as base trend adjustments while Domestic forecasts include captain adjustments.

## POS (Point of Sale) Glidepath

Four dashboard tabs, consumed in Power BI with input via a web enrichment template:

1. Monthly POS View
2. Global Overview — POS
3. POS Pace Chart (benchmark is the financial or consensus forecast depending on your role)
4. Global Overview — Shipment

## AIM Shipment Revenue Model

Pages: Cover Sheet, Full-Year Forecast, Cumulative Forecast Chart, Cumulative / Discrete Forecast Table, Brand Cumulative Forecast, plus appendices (Data Sources, Backtest). Source data: SAP HANA table `Z_CV_SUPPLY_CHAIN`. Owner: the AIM team.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Deferred in v0](../reference/deferred-in-v0.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
