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
| **Case 4** | Forecast is lost during disaggregation because the forecasting range ends before the Consensus Forecast does | Demand Planner, recapturing at Level 1 | Volume recaptured on the named customer that lost it; Level 3 unaffected |

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

!!! note "The `(M)` tag is the Management Indicator"
    This is not a one-off trick specific to Case 3C. `(M)` is the same **Management Indicator** used across the Forecast Calculation Range mechanism generally (see [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)): it tells the Calculate Forecasts program to leave the tagged record's quantity and indicator as they are rather than overwriting it. The same tag, and the same protection, apply anywhere a value needs to survive outside the range.

The team then waits for the **end-of-day disaggregation batch**, which recalculates Level 3 → Level 2 → Level 1. Finding no Level 2 forecast for that partner, it sets the corresponding Level 1 to zero, so the volume redistributes only across the remaining customers.

!!! note "When the change becomes visible"
    After the disaggregation batch, the updated data is transmitted to the EDW tables at **12:30 PM Eastern Time**. The changes become visible in HERO the **following day**, once the EDW tables are updated and HERO refreshes its data.

Result: **Level 3 stays stable**; **Level 1 is redistributed** only across the correct customers. Use this only when the business decision is to preserve the total SKU forecast and redistribute, rather than reduce the SKU or compensate through another product.

## Case 4: forecast lost during disaggregation, recapture at Level 1

Applies when a product has forecast for its partners only through a given month, and the forecasting range for those partners ends at that same point, while the Consensus Forecast still carries volume beyond it. Level 3 disaggregation into those customers then has nowhere to put the extra volume, and it disappears rather than landing anywhere wrong.

**The correct action is to recapture the volume at Level 1**, against the specific Forecast Partner that should carry it.

!!! warning "Never recapture this at Level 2.5"
    Recapturing at Level 2.5 is accepted by the system and nothing looks wrong at the point of capture, but on fan-out that volume spreads across **all** extended Forecast Partners using baseline share, instead of reaching the one customer that actually lost it. The total ties out at the aggregate level and every level below it is wrong. Level 1 assigns the volume to a named Forecast Partner directly; Level 2.5 cannot target one.

**The root-cause alternative.** Where the forecasting range genuinely should cover the weeks in question, fix the range instead of patching around it with a Level 1 recapture. A recapture treats the symptom; a range correction removes the cause.

!!! note "Detection is manual today"
    There is no automated alert for this scenario. The input-data monitor that would host a check like this is not currently deployed, so do not treat any monitor job name as an available gate. Finding this case today depends on someone noticing the gap between the Consensus Forecast and what the range is carrying, not on a system warning.

## Guiding principle

Preserve the right level of accountability while keeping the process practical:

- **Customer-specific corrections** → KAM, through the Reconciliation template.
- **Brand-level decisions** affecting total volume or requiring cross-account compensation → validated and coordinated by the Brand Captain.
- **Preserving a total SKU forecast by redistributing across remaining customers** → Demand Planner, through the traditional Logility forecasting-range process so the disaggregation logic recalculates correctly.
- **Forecast lost during disaggregation because the range ended early** → Demand Planner, recapturing at Level 1 against the named partner, never at Level 2.5.

## Persisting an approved decision into future cycles

When reconciliation approves a **standing** change — e.g. *"Tesco's baseline should permanently increase by 10%"* — how it is persisted so Sales sees it next cycle depends on **what the decision really means**:

### Case A — Raise the total forecast (Level 3 / BU total goes up)

If the intent is a genuine **increase in total demand** (not just a re-split), apply a **Base Trend Adjustment**, held for **~4 months on average**. The purpose is to give the statistical (moving-average) model enough time to **learn the product's new potential** in the market and at that customer. After ~4 months the model should pick up the trend naturally and the enrichment is **no longer needed**.

### Case B — Change the share / proportions (Level 3 total stays the same)

If the intent is that **Tesco should hold a larger share** of the SKU (without changing the BU total), it is a **disaggregation** change, handled by the Demand Planner — not by an enrichment:

1. The **KAM** (in markets without a Brand Captain) or the **Brand Captain** (in markets that have one) requests the change from the **Demand Planner**.
2. The Demand Planner validates the justification and determines the **new Level 2 disaggregation proportions**.
3. The Demand Planner communicates them to **Genpact**, stating **how long** the **fixed disaggregation** (fixed proportions) should apply.
4. Typically after **~6 months** the fixed proportions are no longer needed, because the new split has been in place long enough for the moving-average model to capture it.

!!! warning "Fixed proportions have a hard horizon"
    A fixed-proportion scheme **cannot be maintained beyond the last week of the last open forecasting period**. For example, if the current open forecast reaches 2027, fixed proportions can be reflected **at most through December 2027**; beyond that the **moving-average** model governs.

!!! note "Which mechanism?"
    Total up → **Base Trend Adjustment (~4 months)**. Share change only → **fixed Level 2 disaggregation via the Demand Planner + Genpact (~6 months, capped at the last open forecast period)**. Both are temporary bridges until the moving-average model learns the new pattern.

## Related pages

- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md)

!!! warning "Gaps & Open Questions"
    - **Whether a forecast-lost check will be added when the input-data monitor is deployed.** `[GAP: Rene Bartoli / Jarred Bultema]` The monitor design does not currently include a check for this scenario, and the monitor itself is not deployed.
    - **Whether a corrective Management Indicator pass over 2026 is planned**, or whether affected volume is recaptured case by case instead. `[GAP: Rene Bartoli]`
    - Directional, not a commitment: cases of the Case 4 shape are expected to appear in the first cycle, and not all of them will resolve quickly.
