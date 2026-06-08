<!-- docs/roles/demand-planner.md -->

# Demand Planner — your role in HERO

## Who should read this page

Demand Planning (DP) users who own final review and reconciliation in the UK pilot.

## What you do in HERO

You are often the **steward of final review**. You reconcile final numbers, use structured functions, and review BU-SKU (Business Unit–SKU) outputs.

- Review the rendered weekly numbers and **reconcile** final week-level totals.
- Use **structured functions**: Version Change and Channel Shift, instead of manual week-by-week edits.
- Review **BU-SKU / Level 2.5** outputs where your cluster has moved to that stage.
- Apply **Base Trend Adjustments** when the ongoing baseline itself is wrong (not for one-off events).

## When you interact with HERO in the cycle

Mainly at the **reconciliation** and **review** stages, after Sales and Marketing have captured enrichments. You also re-review BU-SKU weeks whenever baseline, enrichments, or Level 1 reconciliation move afterward.

## Tools and views you use

- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — your primary tool.
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md) — for later-stage aggregate review.
- [Field-by-field reference](../workflows/field-by-field-reference.md) — for the reconciliation control fields.

## Workflow steps you own or review

| Step | Your involvement |
|---|---|
| Enrichment capture | Review / support; correct enrichment-type mistakes. |
| Standard reconciliation | **Own** — enter weekly Base Trend Adjustments and structured functions. |
| BU-SKU / Level 2.5 review | **Own or co-own** (cluster-specific). |
| Baseline / disaggregation issues | Diagnose and route; correct at the right level. |

## Common mistakes & watchouts

!!! warning "Watchouts"
    - **Deltas, not absolutes.** Reconciliation takes a plus/minus change, not a final overwrite. Think in deltas.
    - **Don't mask baseline errors with repeated enrichments.** If the ongoing baseline is wrong, use a Base Trend Adjustment.
    - **Don't combine** a Version Change and a Channel Shift on the same row.
    - **Re-download** before a later-stage reconciliation or sign-off session — someone may have touched the same scope.
    - Older **Level 1 workbooks are stale** once the process moves to BU-SKU review.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU worked examples](../examples/bu-sku-worked-examples.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)

!!! question "Gaps & Open Questions"
    - Confirm whether **Level 2.5 write ownership** sits with Demand Planning or Brand Captains in the UK pilot.
    - Validate the **frozen-window** exception path DP should follow.
