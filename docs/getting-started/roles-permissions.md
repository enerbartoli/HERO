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
- As of the **20 July 2026 release**, HERO access controls have been cleaned up: users only see the **Business Units they are authorised to work with** in the BU selection.
- Selecting **All Forecast Partners** at download switches the workbook into BU-SKU mode.
- The `ALL_FORECAST_PARTNERS` scope is restricted to an **explicit allowlist** in the current build, and is only valid on MARKETING / DEMAND_PLANNING enrichment rows.

## How access is actually granted

The roles above describe what people **do** in the tool. The permissions underneath them are simpler than the role list suggests.

- Access is granted only through **Platform-managed regional groups** (Databricks workspace membership). The earlier manual grant route is closed.
- There is **no granularity by role**. Nothing in the permission model distinguishes Marketing from Sales from Demand Planning.
- There are exactly **two access levels**: the **planner** level, which opens the Level 2.5 templates, and the **regular user** level, which opens Level 1 only.
- Usage can be monitored, but it cannot be gated per day or per role. Staged enablement — for example letting demand planners in before the commercial team — cannot be enforced by permissions; users can only be advised.
- Requests go through a Platform ticket, so plan access well ahead of a go-live rather than in the launch week.

!!! note "Which people get which level"
    The mapping of individuals to the planner or regular-user level is an enablement decision taken per market, not something the tool derives from a job title.

## Related pages

- [Demand Planner guide](../roles/demand-planner.md) · [Sales guide](../roles/sales.md) · [Marketing / GPL guide](../roles/marketing-gpl.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

!!! warning "Gaps & Open Questions"
    - The mapping of named users to the planner versus regular-user level is decided per market at enablement and is not documented here.
