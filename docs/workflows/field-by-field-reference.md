<!-- docs/workflows/field-by-field-reference.md -->

# Field-by-field reference

## Who should read this page

Anyone entering data in the enrichment or reconciliation tabs. Use it to look up what a field means and whether it is editable.

## Purpose

Define each field, whether it is required / editable, and its allowed values.

## Enrichment template fields

| Field | Required? | Allowed values / source | Notes |
|---|---|---|---|
| Business Unit | Required | Dropdown of enabled BUs | Defines which time series the enrichment applies to. |
| Forecast Partner | Required | Dynamic dropdown by BU + Brand | `ALL_FORECAST_PARTNERS` only for authorised users and only on MARKETING / DEMAND_PLANNING rows. |
| Forecast Partner Customer Number | Required | Auto-populated | From the selected Forecast Partner. |
| Planning SKU | Required | Dynamic dropdown in scope | The planning item code. |
| SKU Description | Read-only | Auto-populated | Confirm the item. |
| Shortage Planning SKU | Required for `SUPPLY_SHORTAGE_COMP` | Text | Tracking only; does not move demand. |
| Enrichment Type | Required | See [ECT types](../tools/enrichment-capture-template.md) | Determines bucket and downstream treatment. |
| Status | Required | `PROPOSED` / `CONFIRMED` / `DECLINED` | Controls audit/reporting treatment. |
| Shipment Impact Start Date | Required | `YYYY-MM-DD` | Defines which fiscal weeks receive the enrichment. |
| Shipment Impact End Date | Optional | `YYYY-MM-DD` | With the start date, sets weekly coverage. If left blank, the enrichment is treated as a **single-week** event (the start week only). |
| Shipment Channel | Required | `DOM` / `DI` | Defines the time series. The reconciliation model uses `DOM` (domestic) and `DI` (direct import). |
| Expected Shipment Lift, percent | Conditional | Excel percent (25% = 0.25) | Use percent **or** units, never both. Converted against baseline. |
| Expected Shipment Lift, units | Conditional | Number | Use units **or** percent, never both. Spread evenly across covered weeks. |
| Retail Promotion Mechanism | Required for `RETAIL_PROMOTION` | `DISCOUNT` / `BOGO` / `COUPON` / `OTHER` | Classification metadata. |
| Price Discount, percent | Optional | Excel percent | Commercial metadata for audit. |
| Pallet Tag | Required for `TMO` | Text | Unique within one upload; groups TMO pallet rows. |
| Special Planning Unit (SPU) SKU | Optional (`TMO` only) | Text | Tracking only; does not change math. |
| Store Count | Optional | Whole number | Supporting context. |
| Notes | Optional | Free text | Supporting context. |
| Brand / Lifecycle Status | Read-only | Auto-populated | Context lookups. |
| Pallet ID / Enrichment ID / Submitted By / Operation Type / Upload Batch ID | Read-only | Auto-populated | Audit and traceability. |

## Reconciliation fields (non-weekly, editable controls)

| Field | Required? | Notes |
|---|---|---|
| Adjusted Planning SKU | Optional | Version-change target. **Do not** use with Channel Shift Proportion on the same row. |
| Version Adjustment Start / End Week | Required with Adjusted Planning SKU | Fiscal week numbers. |
| Channel Shift Proportion | Optional | e.g. `0.25` = 25%. **Do not** use with Adjusted Planning SKU on the same row. |
| Channel Shift Start / End Week | Required with Channel Shift Proportion | Fiscal week numbers. |

!!! note "Read-only reconciliation context"
    Business Unit, Forecast Partner, Fiscal Year, Shipment Channel, Planning SKU, SKU/Brand/Parent fields, Lifecycle Status, Blended A-Price, all *Total …* columns, and all *Previous Cycle …* / *Cycle-on-Cycle Variation* columns are read-only context.

## Reconciliation weekly field families (Wk 1–Wk 52)

| Family | Editable? | Meaning |
|---|---|---|
| Baseline | Read-only | Current baseline or shipment actuals in the actualized period. |
| Sales Enrichment | Read-only | Weekly contribution from sales / event enrichments. |
| Marketing and Demand Planning | Read-only | Weekly contribution from marketing / DP enrichments. |
| **Baseline Trend Adjustments** | **Editable** | Numeric delta in units — the main editable weekly area in standard reconciliation. |

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [Tab-by-tab walkthrough](tab-by-tab-walkthrough.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
