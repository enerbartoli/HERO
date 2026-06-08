<!-- docs/getting-started/roles-permissions.md -->

# Roles & permissions

## Who should read this page

Anyone who needs to understand who does what in HERO, and which scope they can access.

## Purpose

Summarise the role behaviours the current build supports, and flag where cluster-specific ownership still needs business confirmation.

!!! warning "Draft ownership"
    The current development build clearly supports **workbook scope filtering** and **special BU-SKU mode access**. Some cluster-specific role details below are marked `[DRAFT — confirm with SME]`.

## Role reference

| Role | What they do in HERO | Primary path |
|---|---|---|
| **Sales / KAM** | Add commercial enrichments, review account-level impact, propose reconciliation changes. | Enrichment authoring + standard reconciliation in their owned slice. |
| **Marketing / GPL** | Add marketing overlays and challenge final forecast outcomes. | Marketing enrichment path; some clusters also use BU-SKU review inputs. `[DRAFT — confirm with SME]` |
| **Demand Planning** | Review and reconcile final numbers; use structured functions (version change, channel shift); review BU-SKU outputs. | Standard reconciliation and, by cluster, Level 2.5 / BU-SKU inputs. `[DRAFT — confirm with SME]` |
| **Brand Captains** | Challenge baseline and disaggregation, especially in BU-SKU / Level 2.5 review. | UK training notes place L2.5 write ownership here. `[DRAFT — confirm with SME]` |
| **Supply-Chain COE** | Support data quality, baseline / disaggregation issues, operating-model governance. | Usually advisory / review. `[DRAFT — confirm with SME]` |
| **Supply-Chain Leadership** | Review resolved outputs, governance, publication readiness. | Typically read-only. `[DRAFT — confirm with SME]` |

!!! note "Special access"
    The `ALL_FORECAST_PARTNERS` scope used for BU-SKU mode is restricted to an **explicit allowlist** in the current build.

## Related pages

- [Demand Planner guide](../roles/demand-planner.md) · [Sales guide](../roles/sales.md) · [Marketing / GPL guide](../roles/marketing-gpl.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

!!! question "Gaps & Open Questions"
    - Confirm the **cluster-specific permission matrix** by Business Unit, Forecast Partner, and Brand (deferred in v0).
    - Validate **Level 2.5 write ownership** (Brand Captain vs Demand Planning) for the UK pilot.
    - Confirm whether Marketing / GPL uses BU-SKU review inputs in the UK.
