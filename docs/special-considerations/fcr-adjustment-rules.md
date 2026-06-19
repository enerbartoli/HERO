<!-- docs/special-considerations/fcr-adjustment-rules.md -->

# Rules for FCR adjustment within cycle

## Who should read this page

Key Account Managers (KAMs), Brand Captains, and Demand Planning (DP) — anyone handling a forecast adjustment opportunity identified **inside the planning cycle (W-1 to W3)** during the UK pilot.

## Purpose

Give clear guidance on how to handle forecast adjustment opportunities found within the cycle, depending on whether the impact can be absorbed within the same customer, requires a direct customer-level change, or needs broader compensation across products, accounts, or forecasting partners. It also defines who owns each type of adjustment so impact stays visible across customer, product, and brand hierarchies. (FCR = Forecast Calculation Range.)

## Decision summary

| Scenario | Business situation | Primary owner | Expected Level 3 impact |
|---|---|---|---|
| **Case 1** | Volume reallocation within the same customer, from one reference to another | KAM | Level 3 stays stable |
| **Case 2** | Absolute increase or reduction at customer level, not compensated within the customer | KAM, aligned with Brand Captain | Level 3 changes; variation accepted |
| **Case 3A** | Customer-level impact compensated through another product across all accounts | Brand Captain | Level 3 protected via product-level compensation |
| **Case 3B** | Customer-level impact compensated through a specific account | Brand Captain + compensating KAM | Level 3 protected via account-level compensation |
| **Case 3C** | One customer will not take a SKU, but total SKU volume should be preserved and redistributed | Brand Captain + Demand Planner | Level 3 stays stable; Level 1 reallocated |

## Case 1 — Volume reallocation within the same customer

Applies when the opportunity is for a specific reference and customer, but the volume will be **compensated by another product within that same customer** (e.g. a different colorway, 5-digit code, or parent material).

**Use the Version Change functionality.** At Reconciliation Level 1, the KAM indicates which product should absorb the forecast and the period the adjustment applies to, and the system moves the volume. **Level 3 stays stable** even though volume moves between products / 5-digit codes within the customer.

## Case 2 — Absolute increase or reduction at customer level

Applies when the adjustment is an absolute increase or reduction to a customer's total volume that **will not be compensated within that customer**.

The KAM should **align with the Brand Captain first**, since it changes total customer volume. The Brand Captain decides whether it is significant enough to require compensation from other accounts, or is normal demand variation to be absorbed at customer level. If it is normal variation, the KAM enters the Reconciliation template and applies the increase / reduction to the relevant brand, product, or SKU. The impact is **transmitted automatically to Level 3** and accepted as part of the customer-level update.

## Case 3 — Customer-level adjustment requiring brand-level compensation

A variation of Case 2: the change is not compensated within the customer and, after validating with the Brand Captain, is significant enough to put the **brand budget / total brand forecast** at risk. The Brand Captain defines how compensation is managed:

### Option 3A — Compensate through another product across all accounts

The adjustment is made at **Level 2.5**: the Brand Captain applies it to the compensating product, and it is distributed across accounts using the current baseline as the allocation reference. Simplest broad-reallocation scenario.

### Option 3B — Compensate through a specific account

Coordinated directly with the KAM of the **compensating account**, who applies the adjustment through the Reconciliation template for that account. Ensures the compensation is explicitly agreed with the account owner.

### Option 3C — Compensate in the same SKU across the remaining accounts

The most complex case: the Brand Captain wants to **preserve the total SKU forecast at Level 3**, but one customer / forecasting partner will no longer take the reference, so the volume must be **redistributed across the remaining eligible customers**.

Because this changes the underlying **forecasting range**, it cannot be done through the Reconciliation template — it requires **Demand Planner** intervention. In Logility, the Demand Planner:

1. Adjusts the forecasting range to avoid duplicating effort in future cycles.
2. Tags the record with the indicator **(M)** so the Genpact team does not overwrite it later.
3. Sets the **Level 2** forecast for the relevant forecasting partner to **zero** for all applicable weeks.

The team then waits for the **end-of-day disaggregation batch**, which recalculates Level 3 → Level 2 → Level 1. Finding no Level 2 forecast for that partner, it sets the corresponding Level 1 to zero, so the volume redistributes only across the remaining customers.

!!! note "When the change becomes visible"
    After the disaggregation batch, the updated data is transmitted to the EDW tables at **12:30 PM Eastern Time**. The changes become visible in HERO the **following day**, once the EDW tables are updated and HERO refreshes its data.

Result: **Level 3 stays stable**; **Level 1 is redistributed** only across the correct customers. Use this only when the business decision is to preserve the total SKU forecast and redistribute, rather than reduce the SKU or compensate through another product.

## Guiding principle

Preserve the right level of accountability while keeping the process practical:

- **Customer-specific corrections** → KAM, through the Reconciliation template.
- **Brand-level decisions** affecting total volume or requiring cross-account compensation → validated and coordinated by the Brand Captain.
- **Preserving a total SKU forecast by redistributing across remaining customers** → Demand Planner, through the traditional Logility forecasting-range process so the disaggregation logic recalculates correctly.

## Related pages

- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
