<!-- docs/help/faq-common-gotchas.md -->

# FAQ & common gotchas

## Who should read this page

All users. Quick answers to the questions that come up most often.

## Purpose

Resolve the recurring points of confusion in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## Frequently asked questions

**Why does the dashboard not match my upload yet?**
Your upload updates HERO authoring state immediately, but resolved reporting surfaces update only after the backend refresh completes.

**When should I re-download a workbook?**
Before any major working session, after a validation failure, after another user touched overlapping scope, and when the process moves into BU-SKU review.

**Can I use both Enrichments and Reconciliation?**
Yes, for different jobs: Enrichments for dated business events; Reconciliation for direct week-level number changes after those events are considered.

**Can I upload both standard and BU-SKU reconciliation from the same workbook?**
No. BU-SKU mode is a different authoring mode and is treated separately.

**What does blank vs 0 mean in BU-SKU mode?**
Blank keeps the current rendered BU-SKU adjustment total; `0` sets it to zero for that week; a negative value means the adjustment total should be below zero.

**Does DEMAND_PHASE_SHIFT automatically move demand between weeks?**
No — it is tracking only. Use reconciliation for an actual week move.

**Does SUPPLY_SHORTAGE_COMP automatically move volume between SKUs?**
No — it tracks the relationship, but you still capture the compensating demand correctly.

**Can I change actualized weeks?**
Treat shaded / actualized weeks as frozen forecast history unless your operating model explicitly routes an exception through a separate process.

**In the Level 2.5 template, which columns do Demand Planners use for their adjustments?**
The **Baseline Trend Adjustments** columns — the **orange** ones. That is the editable weekly area.

**Then why does my adjustment show under "Marketing and Demand Planning" after I upload?**
Because HERO **classifies** your entry on upload based on **who entered it and when**. You always type into *Baseline Trend Adjustments*; the system then files Demand Planning / Marketing reconciliation entries under the *Marketing and Demand Planning* columns. Both are correct — input vs. how it's classified afterward.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Validation & error catalogue](validation-error-catalogue.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
