<!-- docs/roles/sales.md -->

# Sales / Account Planner — your role in HERO

## Who should read this page

Sales and Key Account Manager (KAM) users who author commercial enrichments in the UK pilot.

## What you do in HERO

Your work moves from data wrangling to **insight ownership**: you capture the real commercial events you know about, and you propose reconciliation changes for your accounts.

- Add **commercial enrichments** — promotions, sets, samples, pre-orders, Trade / pallet adjustments (TMO), phase-outs.
- Review **account-level impact** on the rendered forecast.
- Propose **reconciliation** changes in your owned slice.

## When you interact with HERO in the cycle

At the **event-capture** stage — usually the first place a known business event is recorded — and during **commercial pre-work** before alignment sessions.

## Tools and views you use

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md) — your primary tool.
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — for standard reconciliation in your slice.
- The workbook **instructions tab** — scenario catalogue when you know the business situation but not the HERO path.

## Workflow steps you own or review

| Step | Your involvement |
|---|---|
| Enrichment capture | **Own** — author promo / set / pre-order / TMO rows with correct timing, status, and magnitude. |
| Standard reconciliation | Propose changes in your owned scope; coordinate on overlapping scope. |
| BU-SKU / Level 2.5 | Generally not authored by Sales. |

## Common mistakes & watchouts

!!! warning "Watchouts"
    - **Units *or* percent, never both** on the same enrichment row. Pick one mode per record.
    - **Confirmed events only.** Use enrichments for events tied to dates, channels, and items — not to fix a wrong baseline.
    - **Right type, right field.** A correct number under the wrong enrichment type still fails review. Reclassify rather than delete-and-recreate.
    - **New enrichments can't use past dates** (format `YYYY-MM-DD`).
    - **Coordinate on shared scope** — last uploader wins.

## Related pages

- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)
- [Calculation reference](../examples/calculation-reference.md)

!!! question "Gaps & Open Questions"
    - Confirm the canonical handling for **out-of-aisle / secondary placement** and **ladder orders** (no single mechanism is locked yet; follow customer playbook).
