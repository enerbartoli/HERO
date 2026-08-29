<!-- docs/tools/reference-views-dashboards.md -->

# Reference views & dashboards

## Who should read this page

All users who consume resolved outputs: Sales, Demand Planning (DP), Marketing / Global Product Lead (GPL), Finance, and Supply Chain.

## Purpose

Describe the Power BI views that present resolved HERO (Hasbro Enrichment & Reconciliation Optimizer) outputs, and how they refresh.

!!! warning "Timing"
    Resolved dashboards refresh **after the backend processing run completes** — they can lag a successful upload. The workbook shows authored intent immediately after download; dashboards match only after the resolved refresh.

## Forecast Enrichment Power BI dashboard

[Open in Power BI](https://app.powerbi.com/groups/ffc77157-ca2d-4b70-9f14-2a1c3842f973/reports/1d7dcc05-0d12-40f8-bd0c-184b82bdd406/e26a15167349ce5185cc?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&bookmarkGuid=92641236-1c4a-4f93-be93-803e0577ab14)

Provides visualisations of baseline forecasts, enrichments, consensus forecasts, and key performance indicators, with drill-down to SKU-level detail. Domestic (DOM) and Direct Import (DI) data are separated; DI forecasts are reflected as base trend adjustments while Domestic forecasts include captain adjustments.

!!! note "One consolidated dashboard, scoped to what you are authorised for"
    The separate per-market reports have been replaced by this single consolidated dashboard. Opening it shows you the market you are authorised for, and nothing else. Members of a regional team see every market in their region that is already live on HERO, in one view, rather than switching between per-market reports.

## POS (Point of Sale) Glidepath

[Open in Power BI](https://app.powerbi.com/links/9YKCWlN-jc?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&pbi_source=linkShare)

Four dashboard tabs, consumed in Power BI with input via a web enrichment template:

1. Monthly POS View
2. Global Overview — POS
3. POS Pace Chart (benchmark is the financial or consensus forecast depending on your role)
4. Global Overview — Shipment

## AIM Shipment Revenue Model

[Open in Power BI](https://app.powerbi.com/links/F5YrmkBmfH?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&pbi_source=linkShare)

Pages: Cover Sheet, Full-Year Forecast, Cumulative Forecast Chart, Cumulative / Discrete Forecast Table, Brand Cumulative Forecast, plus appendices (Data Sources, Backtest). Source data: SAP HANA table `Z_CV_SUPPLY_CHAIN`. Owner: the AIM team.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Deferred in v0](../reference/deferred-in-v0.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
