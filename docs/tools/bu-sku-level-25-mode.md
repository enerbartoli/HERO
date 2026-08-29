<!-- docs/tools/bu-sku-level-25-mode.md -->

# BU-SKU / Level 2.5 reconciliation mode

## Who should read this page

Brand Captains, Demand Planning, and Marketing doing later-stage aggregate review. Brand Captains author the brand-level number; Demand Planning and Marketing use similar BU-level reconciliation templates.

## Purpose

Explain the **BU-SKU (Business Unit–SKU) / Level 2.5** reconciliation mode and how it differs from standard reconciliation.

## What it is

BU-SKU mode is a **later-stage reconciliation view built bottom-up** from forecast-partner rows. You edit **signed BU-SKU weekly reconciliation-adjustment totals** at Business Unit + Planning SKU + Shipment Channel level, rather than partner-level detail.

It is triggered when you download with **All Forecast Partners** selected. In that mode the workbook **skips the full enrichments render and hides the enrichments tab** to keep downloads faster and to avoid adding new enrichments during BU-SKU review.

## The core rule

!!! warning "A BU-SKU entry is not the final weekly number"
    A BU-SKU weekly entry sets the **desired BU-SKU weekly total for the reconciliation-adjustment layer** for that week. HERO then works backward and recomputes the Level 1 partner-level deltas needed to land on that target, distributing by **baseline share** (equal split only when the slice baseline is zero).

This is the opposite of standard reconciliation, which says *"apply this exact delta to this exact Level 1 row."*

!!! note "This applies to every enrichment type, not only Base Trend Adjustments"
    The baseline-share fan-out described here is HERO's own proportional step for any Level 2.5 capture reaching Level 1, whatever enrichment type carries it.

!!! note "Earlier enrichments and reconciliation do not change the weights"
    The weights used to split a new Level 2.5 target are calculated fresh from the current baseline, at the level and for the record in question, each time. **Earlier enrichments and carried-forward reconciliation changes do not affect these weights.** It is reasonable to assume they would; they do not. Also, because the basis is per record rather than a market-wide or brand-wide average, two SKUs sitting inside the same BU-SKU entry can be weighted differently.

!!! warning "The partial-resultant trap"
    Where some partners and weeks inside one Level 2.5 entry carry a baseline and others do not, baseline-share weighting concentrates the whole delta onto the minority that do. That can be worse than a flat split, and nothing about it looks broken on the surface. Check the Level 1 result after fan-out rather than assuming the split landed evenly.

!!! note "A Level 2.5 change is visible at Level 1, once fan-out runs"
    The Level 1 template carries the Level 2.5 adjustment as a read-only context column (see [Forecast Reconciliation Template](forecast-reconciliation-template.md)). The only limitation is timing: the value appears at Level 1 only after post-processing has run, which is minutes after upload, not instantly. Do not direct a Level 1 user to the dashboard for something their own template already shows them.

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
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md) — different mechanism: the range decides *which customers* are forecast; Level 2.5 decides *how an adjustment splits* across them.

!!! success "No open questions identified"
    No open questions were identified from the available source material.
