<!-- docs/roles/sales.md -->

# Sales / Account Planner — your role in HERO

## Who should read this page

Sales and Key Account Manager (KAM) users who author commercial enrichments in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## What you do in HERO

You capture the real commercial events you know about and make customer-level reconciliation edits in your scope.

- Add **commercial enrichments** — promotions, sets, samples, pre-orders, Trade / pallet adjustments (TMO), phase-outs. **Only Sales can modify commercial enrichments.**
- Review **account-level impact** on the rendered forecast.
- Make **customer-level (Level 1) reconciliation** edits in your owned slice. Demand Planning and Marketing work at the aggregate (BU) level, and can author a BU-level adjustment if agreement with Sales is not reached.

## Tools and views you use

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md) — your primary tool.
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — for Level 1 reconciliation.
- The workbook **instructions tab** — scenario catalogue when you know the situation but not the HERO path.

## Common mistakes & watchouts

!!! warning "Watchouts"
    - **Units *or* percent, never both** on the same enrichment row. Pick one mode per record.
    - **Confirmed events only** within the near-term supply window; use *Proposed* for longer-horizon events. Don't use enrichments to fix a wrong baseline.
    - **Right type, right field.** A correct number under the wrong enrichment type still fails review. Reclassify rather than delete-and-recreate.
    - **TMO comes from FAST** — don't author or edit TMO in the template; it is seeded from FAST.
    - **New enrichments can't use past dates** (format `YYYY-MM-DD`).
    - **Coordinate on shared scope** — the latest upload prevails.

## Related pages

- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)
- [Calculation reference](../examples/calculation-reference.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
