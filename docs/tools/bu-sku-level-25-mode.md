<!-- docs/tools/bu-sku-level-25-mode.md -->

# BU-SKU / Level 2.5 reconciliation mode

## Who should read this page

Demand Planning and Brand Captains doing later-stage aggregate review. `[DRAFT — confirm L2.5 ownership]`

## Purpose

Explain the **BU-SKU (Business Unit–SKU) / Level 2.5** reconciliation mode and how it differs from standard reconciliation.

## What it is

BU-SKU mode is a **later-stage reconciliation view built bottom-up** from forecast-partner rows. You edit **signed BU-SKU weekly reconciliation-adjustment totals** at Business Unit + Planning SKU + Shipment Channel level, rather than partner-level detail.

It is triggered when you download with **All Forecast Partners** selected. In that mode the workbook **skips the full enrichments render and hides the enrichments tab** to keep downloads faster and to avoid adding new enrichments during BU-SKU review.

## The core rule

!!! warning "A BU-SKU entry is not the final weekly number"
    A BU-SKU weekly entry sets the **desired BU-SKU weekly total for the reconciliation-adjustment layer** for that week. HERO then works backward and recomputes the Level 1 partner-level deltas needed to land on that target, distributing by **baseline share** (equal split only when the slice baseline is zero).

This is the opposite of standard reconciliation, which says *"apply this exact delta to this exact Level 1 row."*

## Blank vs 0 vs signed value

| Entry | Meaning |
|---|---|
| **Blank** | Keep the current rendered BU-SKU adjustment total for that week. |
| **0** | Set the BU-SKU adjustment total to zero for that week. |
| **Positive / negative** | Move the adjustment total above / below zero. |

## Governance

!!! note "Handoff from Level 1"
    Use forecast-partner reconciliation during normal Level 1 review. Once Demand / Marketing reconciliation moves to BU-SKU review, download a **fresh** BU-SKU workbook and make final weekly adjustments there. **Treat older Level 1 reconciliation workbooks as stale** after that handoff. Do not populate both `reconciliation` and `reconciliation_bu_sku` in the same upload.

## Related pages

- [BU-SKU worked examples](../examples/bu-sku-worked-examples.md) — six scenarios showing what moves and what stays fixed.
- [Forecast Reconciliation Template (FRT)](forecast-reconciliation-template.md)

!!! question "Gaps & Open Questions"
    - Confirm **Level 2.5 write ownership** (Brand Captain vs Demand Planning) for the UK pilot.
