<!-- docs/workflows/forecast-range-calculation.md -->

# Forecast Calculation Range & Disaggregation

## Who should read this page

Sales / Key Account Managers (KAMs), Demand Planning (DP), and Brand Captains — anyone whose item should be forecast for some customers and periods but not others.

## Purpose

Explain what the **Forecast Calculation Range (FCR)** is, how it is generated and adjusted, and why it matters for **disaggregation** — how the baseline is split down to customers.

!!! note "Name"
    The canonical term is **Forecast Calculation Range**. An underlying pipeline guide informally calls it "Forecast Calendar Range"; treat *Calculation* as canonical.

## What the forecast range is

!!! note "A continuous period, not a year bucket"
    The Forecast Calculation Range carries one start date and one end date. Every period outside those two dates is out of range, whatever calendar year it falls in. "We only use the range for 2027" is a statement about **when the mechanism was adopted**, not about how far it reaches: a range loaded for a 2027 need, on a SKU that also traded in 2026, puts the 2026 weeks out of range for that record too. This is the point to get straight before reasoning about any range-related question below; every other distinction on this page sits on top of it.

The FCR is a **per-product window of Start and End weeks** that tells Logility when a product should be planned: *"this product should be available from week X to week Y."* It is the gate that decides which weeks — and, at customer level, which customers — receive a forecast.

**Two distinct mechanisms are easy to conflate, so keep them apart:**

> The **Forecast Calculation Range** defines which customer and which periods receive part of the resultant, the baseline.
> The **portfolio extension** defines which customers can hold forecast for a SKU at all, whether or not that forecast was generated statistically.

They fail differently. No extension means there is nowhere for the volume to land, and it can genuinely be lost. A closed range means no resultant, so the volume lands but lands flat, at zero.

## How the range is generated

The range is built bottom-up in four steps, starting from launch data:

1. **Planning SKU dates** — extract on-shelf dates and quantities from **P2M**, then apply region- and channel-specific **lead-time** logic to work out when items must ship to be available. End dates are extrapolated from the last year with P2M quantities.
2. **Level 1 (partner)** — the dates are replicated and adjusted per forecast partner.
3. **Level 2 (Parent SKU)** — aggregated using the **earliest Start and latest End** across items sharing the parent SKU, partner, and channel.
4. **Level 3** — extended to Parent SKU + Business Unit; this is the file loaded into Logility.

After initial load, **Logility is the source of truth** for the range.

!!! note "A start date in the earlier calendar year is expected, not an anomaly"
    A start date is derived as **On-Shelf Date minus Lead Time**, which is exactly what pulls a January on-shelf date back to a December start in the prior year. Where an item already had forecast, the full year ahead was taken; where it did not, the derived start date can fall in the prior year. Treat this as the pipeline working as designed, not as a data issue.

    **The early-delivery failure case** follows the same logic in the other direction: where shipments went out earlier than the lead-time calculation anticipated (for example, in October against a lead time that only reaches back to November), those earlier weeks fall outside the range. Whether that volume survives or is lost then follows the Management Indicator rule below, the same as any other out-of-range period.

!!! note "How the range is built differs by market (say which one applies)"
    Do not present either of these as the single global rule.

    - **North America** built the range initially from the **Sales Forecast**, a deliberate decision valid for **2026 and 2027**. From there, and for any newly generated portfolio, the range depends entirely on the P2M and lead-time pipeline above.
    - **United Kingdom and EMEA** used the Sales Forecast differently: as the **disaggregation base at Level 1**, aggregated up to Level 2, with the resulting Level 2 surface used to disaggregate the Resultant. This is a statement about the disaggregation surface, not about how the range itself was built, and it must not be merged with the North America statement above. It also explains why Level 1 in these markets already carried values before any range existed, which matters later on this page.

    `[GAP: Rene Bartoli]` Whether the North America approach travels to Asia Pacific and Latin America, or is North America only.

## How you control / adjust it

Commercial teams receive **Excel files with the proposed Start/End dates** for each SKU and forecast partner and **adjust them manually** using customer knowledge — delayed launches, exclusivity, and so on. The Level 1 files carry blank "New Start / End Date" override columns and a **status flag** showing whether the range matches Logility or differs. The adjusted dates are then updated in Logility.

Maintenance runs through two routes, and which one applies depends on whether the change is inside the monthly cycle. **In cycle**, the commercial team owns the adjustment, made in the template generated by Genpact for that purpose; this is the normal path. **Outside the monthly cycle**, a planner requests the adjustment directly from the Genpact team in Logility; this is an exception route, not self-service. Either way, a Level 2.5 item sitting in a window where the range is not open is not a case to work around at Level 2.5 (see the Management Indicator section below); it is a range correction, on one of these two routes.

## Why it matters for disaggregation

!!! warning "Default spread causes bad forecasts"
    By default a SKU can extend to **all** forecast partners, which spreads demand to customers that will never take it. The range is how you include **only the relevant customers**.

- **Exclusives** — for a single-customer SKU (e.g. an Amazon exclusive), **set/adjust the end date** so other partners are excluded and the forecast does not spread to them.
- **Stopping a SKU for a customer** — set an end date to stop forecasting that SKU/customer. This is distinct from a phase-out enrichment (which takes the item off normal carry-forward more broadly).
- **An out-of-range value is not automatically a data-quality failure.** Whether it survives or is removed depends on the Management Indicator, below. Do not treat every zero outside the range as missing or bad data before checking the indicator.

## The Management Indicator decides what survives outside the range

The range does not zero anything by itself. It zeroes values **through the Calculate Forecasts program (FCP)**, and the FCP only writes into a period where the **Management Indicator** allows it. The flag has to be present at **Levels 3, 2 and 1** for the affected periods; marking only one of the three is not protection.

| Indicator | What happens to an out-of-range value | Hasbro's name |
|---|---|---|
| `M` | **Preserved.** The FCP leaves the quantity and the indicator as they were, because the flag tells the system a person is deliberately overriding the statistically generated value. | Manual |
| `H` | **Removed.** The FCP zeroes it. | Historical |

Hasbro uses only these two values. If `N` (No override) is ever seen, treat it as carrying the same exposure as `H`; it is not a neutral state.

!!! warning "`M` protects against the recalculation, not against forcing"
    `M` is a **forcible** indicator: it stops the Calculate Forecasts program from overwriting the value, which is the protection above, but it does **not** stop the Force Forecasts (FIF) program from redistributing that same value from a parent. "I marked it `M`, it is safe" is right about the range and not a general statement. One qualifier in Hasbro's favour: periods outside the range are processed by FIF as though inhibited, so an `M` value outside the range is protected from the FCP by its own indicator and separately not forced by FIF because the range has stopped the forcing. Two different doors, both closed.

## The range constrains the force down, not the roll up

What the range removes on the way **down** the hierarchy stays removed. Values already sitting at a **lower** level are aggregated **upward without the range acting on them**, because the roll up is performed by a different mechanism entirely, the **Summing program**, which brings the sum of the children up to the parent and is not governed by the Forecast Calculation Range. This is why a Level 3 total can look correct while Levels 2 and 1 are empty underneath it, and why a Level 1 value can roll up into a Level 3 number that does not reconcile with the range supposedly governing it.

This is not a theoretical asymmetry. In UK and EMEA, Level 1 was already populated (see the market note above) before any range existed, so those Level 1 values survived the range and rolled up regardless of what the range says.

!!! warning "Deleting a Level 1 forecast propagates upward, and the volume does not come back"
    Level 1 work is never overwritten by disaggregation, which is the protection users rely on day to day. The same property cuts the other way: clearing a customer's Level 1 forecast sends that zero up through the summing pass, and because the total is never pushed back down again, the **Level 3 number is what gets overwritten**. The volume does not return on its own.

Of the three levels (volume sitting at Level 3, at Level 2, and at Level 1 while out of range), the **Level 2 case has not yet been exercised in the system**. The expected behaviour, by the same logic above, is that an out-of-range Level 2 value is not forced down to Level 1, and that a Level 1 zero then rolls up over it, but this is expected, not confirmed (see the Gaps block at the end of this page).

## Scope, validation, and data quality

- Both **8-digit and 9-digit (wave) SKUs** are processed by the range pipeline.
- SKUs **without supporting P2M data** are **deactivated**, and files are generated to classify the reason for the missing dates.
- If a computed **End Date falls before the Start Date**, the row is flagged as a data issue for review.
- Regional teams run **periodic P2M audits** to remove invalid or outdated entries.

## How it relates to the baseline

The statistical model output is generated **first** (forecast before range), and the **range layer is then applied** on top.

## How history cleansing works

Cleansing is how the model is told what really happened, as opposed to what shipped. It is applied in the **Adjusted Demand array**, the editable layer the statistical baseline learns from, and never in raw Actuals.

**The mechanic.** Cleansing runs in the **opposite direction to the enrichment**. When a period closes, cleansed history is actual shipments minus the `SET`. Base trend adjustments are **not** cleansed: they adjust the forward baseline and never enter the cleansing calculation.

That is why a `SET` does two jobs at once. It holds volume in the forecast now, and it is the instruction that removes that same volume from history later. It is also why a pair of offsetting `SET` rows nets to zero in cleansing, which is correct when demand only moved between weeks and nothing new was created, and wrong when the point is to strip a volume out of what the model learns.

**Supply shortage compensation.** When a shortage pushes demand onto a substitute item, `SUPPLY_SHORTAGE_COMP` records the relationship between the item that was unavailable and the item that absorbed the demand. At cleansing, that relationship raises the adjusted demand of the item that was unavailable by the compensating quantity, and reduces the same quantity from the substitute. The model then learns the demand the absent item would have had, and does not carry forward an inflated projection for a substitute that only sold because of the shortage.

Capturing that relationship correctly matters even though nothing moves in the forward forecast: the intent is to use it to **automate** the historical cleansing, so the correction happens without a planner having to reconstruct it by hand.

!!! note "This is the initial logic, and it is expected to change"
    The rules on this page are the starting point, not a finished design. They will evolve as the programme accumulates enough cycles to evaluate which cleansing treatment actually improves forecast accuracy. Two objectives guide that evolution: cleansing should measurably improve accuracy, and it should be automated far enough that it does not consume planner time. Treat the current rules as the working method and expect them to be refined.

## Related pages

- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — the in-template "set an end date to stop forecasting" usage.
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md) — note the difference: the **range** decides *which customers* receive a forecast; **Level 2.5** decides *how an aggregate adjustment is split* across them.
- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)
- [Rules for FCR adjustment within cycle](../special-considerations/fcr-adjustment-rules.md) — what to do when forecast is lost because of the range, and the `(M)` tag used there.

!!! warning "Gaps & Open Questions"
    - **Level 2 out-of-range scenario, not yet exercised.** The expected behaviour under the roll-up rule above is that an out-of-range Level 2 value is not forced down to Level 1 and is then rolled over by a Level 1 zero. `[GAP: test pending]` A dummy-data case in Logility to confirm it.
    - **Whether the North America range-construction decision travels beyond North America.** `[GAP: Rene Bartoli]` Asia Pacific and Latin America are not yet addressed.
    - **Naming convention across the range-related labels** ("Forecast Calculation Range", "forecast range", "portfolio extension") is still unsettled. `[GAP: Rene Bartoli]` Until decided, confirm which one a question is really about rather than assuming.
    - **Whether a corrective Management Indicator pass over 2026 is planned**, or the affected volume is recaptured case by case. `[GAP: Rene Bartoli]`
    - Directional, not a commitment: the scale of any 2026 forecast loss from this mechanism is not quantified in any source available to this manual.
