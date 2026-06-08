<!-- docs/getting-started/roles-permissions.md -->

# Roles & what each role does in HERO

## Who should read this page

Anyone who needs to understand who does what **in the tool**, and which scope they can access.

## Purpose

Summarise what each role does inside HERO (Hasbro Enrichment & Reconciliation Optimizer) and how workbook scope and special access work. This is a tool-capability reference, not an org or governance model.

## What each role does in the tool

| Role | What they do in HERO | Primary path |
|---|---|---|
| **Sales / Key Account Manager (KAM)** | Author commercial enrichments; review account-level impact; make customer-level (Level 1) reconciliation edits in their scope. | Enrichment authoring + customer-level reconciliation. |
| **Brand Captains** | Author brand-level reconciliation in the **BU-SKU (Business Unit–SKU) / Level 2.5** template; propose baseline adjustments and own the brand story. | BU-SKU / Level 2.5 reconciliation. |
| **Demand Planning (DP)** | Reconcile final numbers; use structured functions (version change, channel shift); review BU-SKU outputs; facilitate reconciliation. Propose adjustments, and author at BU level when agreement with Sales is not reached. | Standard and BU-level reconciliation templates. |
| **Marketing / Global Product Lead (GPL)** | Add marketing overlays; challenge final outcomes. Propose adjustments at BU level, and author them when agreement with Sales is not reached. | Marketing overlay + BU-level reconciliation. |

!!! note "Level 2.5 / BU-level reconciliation"
    Brand Captains, Demand Planning, and Marketing all work through the aggregate (Level 2.5 / BU-level) reconciliation templates. Brand Captains author the brand-level number. Demand Planning and Marketing first **propose and challenge**; if agreement with Sales is not reached, they can **author the adjustment at BU level**, which HERO then disaggregates proportionally down to the customer rows. Customer-level (Level 1) edits are made by Sales.

## Scope and special access

- A workbook is downloaded for a chosen scope (Business Unit, Forecast Partner, optional Brand, Fiscal Year).
- Selecting **All Forecast Partners** at download switches the workbook into BU-SKU mode.
- The `ALL_FORECAST_PARTNERS` scope is restricted to an **explicit allowlist** in the current build, and is only valid on MARKETING / DEMAND_PLANNING enrichment rows.

## Related pages

- [Demand Planner guide](../roles/demand-planner.md) · [Sales guide](../roles/sales.md) · [Marketing / GPL guide](../roles/marketing-gpl.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
