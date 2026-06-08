<!-- docs/roles/demand-planner.md -->

# Demand Planner — your role in HERO

## Who should read this page

Demand Planning (DP) users who reconcile and review in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## What you do in HERO

You reconcile final numbers, use structured functions, and review aggregate outputs.

- Review the rendered weekly numbers and **reconcile** final week-level totals.
- Use **structured functions**: Version Change and Channel Shift, instead of manual week-by-week edits.
- Review **BU-SKU (Business Unit–SKU) / Level 2.5** outputs and use the BU-level reconciliation template. Propose adjustments, and **author them at BU level when agreement with Sales is not reached** (HERO disaggregates proportionally to the customer rows).
- Apply **Base Trend Adjustments** when the ongoing baseline itself is wrong (not for one-off events).
- Facilitate reconciliation and help diagnose baseline / disaggregation issues.

## Tools and views you use

- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — your primary tool.
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md) — aggregate review.
- [Field-by-field reference](../workflows/field-by-field-reference.md) — the reconciliation control fields.

## Common mistakes & watchouts

!!! warning "Watchouts"
    - **Deltas, not absolutes.** Reconciliation takes a plus/minus change, not a final overwrite.
    - **Don't mask baseline errors with repeated enrichments.** If the ongoing baseline is wrong, use a Base Trend Adjustment.
    - **Don't combine** a Version Change and a Channel Shift on the same row.
    - **Re-download** before a later-stage reconciliation session — someone may have touched the same scope.
    - Older **Level 1 workbooks are stale** once the process moves to BU-SKU review.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU worked examples](../examples/bu-sku-worked-examples.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
