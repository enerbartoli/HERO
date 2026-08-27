<!--
  HERO User Manual - consolidated single-file export.
  GENERATED FILE - do not edit by hand.
  Regenerate with: python3 tools/generate_manual_full.py
  Source of truth: the docs/ tree and the mkdocs.yml nav order.
-->

# HERO User Manual - Full Consolidated Manual

**Version 8 - 2026-08-07**

This file concatenates every page of the HERO User Manual in nav order, with MkDocs admonition syntax flattened to plain Markdown. It is generated from the site source; do not edit it by hand (see README.md).

---

<!-- docs/index.md -->

# HERO User Manual

Welcome to the operational manual for **HERO (Hasbro Enrichment & Reconciliation Optimizer)** — the business-user capture layer of the Forecast Enrichment Process.

## Program tools

<div class="tool-grid">
<a class="tool-card" href="Priorization_Matrix/"><span class="tool-card__bar" style="background:#00AEEF"></span><span class="tool-card__body"><span class="tool-card__icon">📊</span><span class="tool-card__title">Prioritization Matrix</span><span class="tool-card__desc">Interactive enhancement prioritization matrix</span></span></a>
<a class="tool-card" href="https://enerbartoli.github.io/mod1-knowledge-check/" target="_blank" rel="noopener"><span class="tool-card__bar" style="background:#005EB8"></span><span class="tool-card__body"><span class="tool-card__icon">🧠</span><span class="tool-card__title">Knowledge Check <span class="tool-card__ext">↗</span></span><span class="tool-card__desc">Self-assessment knowledge check</span></span></a>
<a class="tool-card" href="https://hasbroinc.sharepoint.com/sites/GlobalPlanningCentralCommandCOE/HERO%20Enrichment/Forms/AllItems.aspx?viewid=8ec78d8e%2D6199%2D4641%2D8bb5%2D108cfbe7bc40&amp;newTargetListUrl=%2Fsites%2FGlobalPlanningCentralCommandCOE%2FHERO%20Enrichment&amp;viewpath=%2Fsites%2FGlobalPlanningCentralCommandCOE%2FHERO%20Enrichment%2FForms%2FAllItems%2Easpx" target="_blank" rel="noopener"><span class="tool-card__bar" style="background:#625DA3"></span><span class="tool-card__body"><span class="tool-card__icon">🎥</span><span class="tool-card__title">Training Recordings <span class="tool-card__ext">↗</span></span><span class="tool-card__desc">HERO training session recordings (SharePoint)</span></span></a>
<a class="tool-card" href="https://hasbroinc.sharepoint.com/:f:/r/sites/GenpactStatFCSTAccelerationPrj2/Shared%20Documents/0.%20Baseline%20Management%20Playbook/01.%20Official%20Approved%20Versions_Read%20Only?csf=1&amp;web=1&amp;e=WtdKU6" target="_blank" rel="noopener"><span class="tool-card__bar" style="background:#003C77"></span><span class="tool-card__body"><span class="tool-card__icon">📘</span><span class="tool-card__title">Forecasting Playbook <span class="tool-card__ext">↗</span></span><span class="tool-card__desc">Baseline Management Playbook (SharePoint)</span></span></a>
<a class="tool-card" href="https://glidepath-hero-145364974494823.3.azure.databricksapps.com" target="_blank" rel="noopener"><span class="tool-card__bar" style="background:#00A3AD"></span><span class="tool-card__body"><span class="tool-card__icon">🛠️</span><span class="tool-card__title">HERO Tool <span class="tool-card__ext">↗</span></span><span class="tool-card__desc">Open the HERO tool (Databricks)</span></span></a>
<a class="tool-card" href="https://app.powerbi.com/groups/ffc77157-ca2d-4b70-9f14-2a1c3842f973/reports/1d7dcc05-0d12-40f8-bd0c-184b82bdd406/e26a15167349ce5185cc?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&amp;bookmarkGuid=92641236-1c4a-4f93-be93-803e0577ab14" target="_blank" rel="noopener"><span class="tool-card__bar" style="background:#F0A500"></span><span class="tool-card__body"><span class="tool-card__icon">📈</span><span class="tool-card__title">HERO Dashboard <span class="tool-card__ext">↗</span></span><span class="tool-card__desc">HERO tracking dashboard (Power BI)</span></span></a>
</div>

## How to use this manual

This is a **mechanical guide** to using HERO. It is not a substitute for training on the monthly planning process. Use it when you need to know what a field means, what a button does, how a template behaves, what happens after you upload, or how to interpret a validation message.

**Note — Conventions used throughout**

- **Editable** — you are expected to type into that field.
- **Read-only** — HERO fills the field for context or audit.
- **Resolved state** — the backend has refreshed the weekly reporting layer after uploads.

## Find your starting point

| If you are a… | Start here |
|---|---|
| Demand Planner | [Demand Planner guide](roles/demand-planner.md) |
| Sales / Account Planner | [Sales guide](roles/sales.md) |
| Marketing / GPL | [Marketing / GPL guide](roles/marketing-gpl.md) |
| New to HERO | [What HERO is](getting-started/what-hero-is.md) |
| Looking for a field definition | [Field-by-field reference](workflows/field-by-field-reference.md) |
| Hit a validation error | [Validation & error catalogue](help/validation-error-catalogue.md) |

## What HERO does, in one line

HERO is where you **download** the latest workbook, **enter or review** commercial and planning changes, **upload** those changes back, and then **verify** the resolved outcome through reporting and downstream publication to Logility.

**Success — No open questions identified**

No open questions were identified from the available source material.

---

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

**Warning — Watchouts**

- **Deltas, not absolutes.** Reconciliation takes a plus/minus change, not a final overwrite.
- **Base Trend Adjustments persist across cycles as deltas until manually reversed** — they are not single-cycle. If you meant a one-cycle-only correction, you must zero it out next cycle.
- **A Level 2.5 correction cannot surgically target one account.** It disaggregates across **all** forecast partners by baseline proportion — correcting one account's over-forecast at 2.5 also cuts every other account. The designed path for an inflated single account is peer accountability in the commercial reconciliation session, not a unilateral DP fix at 2.5.
- **Don't mask baseline errors with repeated enrichments.** If the ongoing baseline is wrong, use a Base Trend Adjustment.
- **Don't combine** a Version Change and a Channel Shift on the same row.
- **Re-download** before a later-stage reconciliation session — someone may have touched the same scope.
- Older **Level 1 workbooks are stale** once the process moves to BU-SKU review.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU worked examples](../examples/bu-sku-worked-examples.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/roles/sales.md -->

# Sales / Account Planner — your role in HERO

## Who should read this page

Sales and Key Account Manager (KAM) users who author commercial enrichments in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## What you do in HERO

You capture the real commercial events you know about and make customer-level reconciliation edits in your scope.

- Add **commercial enrichments** — promotions, sets, samples, pre-orders, Trade / pallet adjustments (TMO), phase-outs. **Only Sales can modify commercial enrichments.**
- Review **account-level impact** on the rendered forecast.
- Make **customer-level (Level 1) reconciliation** edits in your owned slice. Demand Planning and Marketing work at the aggregate (BU) level, and can author a BU-level adjustment if agreement with Sales is not reached.

**Note — KAMs have no access to Level 2.5 templates**

Sales / KAM access is scoped to **Level 1, your own customers, only** — there is no KAM access to the Level 2.5 / BU-SKU templates used by Brand Captains, Demand Planning, and Marketing.

## Tools and views you use

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md) — your primary tool.
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — for Level 1 reconciliation.
- The workbook **instructions tab** — scenario catalogue when you know the situation but not the HERO path.

## Common mistakes & watchouts

**Warning — Watchouts**

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

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/roles/marketing-gpl.md -->

# Marketing / GPL — your role in HERO

## Who should read this page

Marketing users and Global Product Leads (GPLs) who add overlays and challenge final outcomes in HERO (Hasbro Enrichment & Reconciliation Optimizer).

## What you do in HERO

- Add **marketing overlays** that reflect planned media and demand-shaping activity.
- **Challenge final forecast outcomes** in review, and propose adjustments at aggregate (BU) level via the marketing / demand-planning reconciliation template. If agreement with Sales is not reached, you can **author the adjustment at BU level**; HERO disaggregates it proportionally to the customer rows.

**Note — Where marketing overlays sit**

Marketing overlays are read in a **separate weekly bucket after sales enrichments**. The order of operations is: baseline → sales enrichments → **MARKETING and DEMAND_PLANNING overlays** → reconciliation adjustments.

## Tools and views you use

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md) — `MARKETING` enrichment type.
- BU-level reconciliation template (aggregate / Level 2.5 review).

## Common mistakes & watchouts

**Warning — Watchouts**

- **Media lift vs override.** Flag whether a lift is evidence-backed media or a top-down override; route it through the agreed Marketing enrichment path.
- The `ALL_FORECAST_PARTNERS` scope is **only valid for MARKETING and DEMAND_PLANNING** rows, and only for authorised users.

## Related pages

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [Roles & what each role does in HERO](../getting-started/roles-permissions.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/getting-started/what-hero-is.md -->

# What HERO is

## Who should read this page

Everyone using HERO for the first time — Sales, Marketing / Global Product Lead (GPL), and Demand Planning. Read this before any tool page.

## Purpose

Explain what **HERO (Hasbro Enrichment & Reconciliation Optimizer)** is, what it is *not*, and the two core jobs it supports.

## What HERO is

HERO is the **business-user capture layer** that sits between the base forecasts in Logility and the reviewed forecast changes the business wants to publish.

It supports two core jobs:

1. **Capturing event-driven enrichments** — promotions, sets, pre-orders, Trade / pallet adjustments (TMO), marketing overlays, and other demand signals tied to dates or commercial events.
2. **Capturing final week-level reconciliation adjustments** — when the business needs to change the final number after those enrichments are considered.

In practical terms, HERO is where you download the latest workbook, enter or review changes, upload them back, and verify the resolved outcome through reporting and publication.

**Warning — What HERO is not**

HERO is **not** the source of the base forecast. The statistical baseline is generated upstream; HERO captures *adjustments* and *final reconciliation* on top of it.

## Related pages

- [Where HERO fits in the cycle](hero-in-the-cycle.md)
- [HERO portal](../tools/hero-portal.md)
- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/getting-started/hero-in-the-cycle.md -->

# Where HERO fits in the planning flow

## Who should read this page

All users. This page gives the context for when you use HERO (Hasbro Enrichment & Reconciliation Optimizer) relative to the systems around it.

## Purpose

Show HERO as the operational layer between baseline preparation, business-adjustment capture, review / reporting, and publication back to Logility.

**Note**

The exact meeting calendar, cadence, and governance are set by each market's operating model and are **not** part of this tool manual. This page describes the tool stages, not a specific cycle schedule.

## The five tool stages

| Stage | What happens | Your action in HERO |
|---|---|---|
| **1. Baseline ready** | The statistical baseline is generated upstream (Logility / Daybreak). | Download a fresh workbook. HERO is not the source of the base forecast. |
| **2. Event capture** | Real-world events are known (promotions, sets, pre-orders, Trade / pallet adjustments (TMO), marketing overlays). | Capture them as enrichments. |
| **3. Reconciliation** | The rendered weekly numbers need final adjustment. | Use standard (forecast-partner / Level 1) reconciliation, or BU-SKU (Business Unit–SKU / Level 2.5) reconciliation. |
| **4. Reporting / review** | Resolved dashboards and review outputs refresh after the backend run. | Read resolved outputs. The workbook shows authored intent immediately; dashboards match only after refresh. |
| **5. Publication** | Approved export logic writes the updated arrays back to Logility. | Nothing in HERO — publication is a separate step on the configured export cadence. |

## How the layers relate

The model produces the baseline from history (pattern, trend, seasonality). HERO is where business knowledge is layered on top — the events the model cannot infer — and where the final number is reconciled. The agreed result is published to Logility.

## Related pages

- [End-to-end workflow](../workflows/end-to-end-workflow.md)
- [Timing & system sync](../workflows/timing-system-sync.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

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

**Note — Level 2.5 / BU-level reconciliation**

Brand Captains, Demand Planning, and Marketing all work through the aggregate (Level 2.5 / BU-level) reconciliation templates. Brand Captains author the brand-level number. Demand Planning and Marketing first **propose and challenge**; if agreement with Sales is not reached, they can **author the adjustment at BU level**, which HERO then disaggregates proportionally down to the customer rows. Customer-level (Level 1) edits are made by Sales.

## Scope and special access

- A workbook is downloaded for a chosen scope (Business Unit, Forecast Partner, optional Brand, Fiscal Year).
- As of the **20 July 2026 release**, HERO access controls have been cleaned up: users only see the **Business Units they are authorised to work with** in the BU selection.
- Selecting **All Forecast Partners** at download switches the workbook into BU-SKU mode.
- The `ALL_FORECAST_PARTNERS` scope is restricted to an **explicit allowlist** in the current build, and is only valid on MARKETING / DEMAND_PLANNING enrichment rows.

## What each role authors, and what nobody overwrites

Key Account Managers author at **Level 1**. Brand Captains, Demand Planning and Marketing author at **Level 2.5**.

In both cases the statistical **Resultant is never modified**. HERO does not overwrite it. HERO influences the published number by layering enrichments and base trend adjustments on top of it, and the Resultant itself travels into HERO read-only.

**Note — \"Level 2-only overrides, Level 1 resultant untouched\"**

This phrasing describes the North America and Europe approach and it is easy to misread. It means the Level 1 **Resultant** is not overwritten. It does **not** mean Level 1 authoring stops: Key Account Managers continue to capture enrichments and base trend adjustments at Level 1. *(Confirmed by Rene Bartoli, 7 August 2026.)*

## How access is actually granted

The roles above describe what people **do** in the tool. The permissions underneath them are simpler than the role list suggests.

- Access is granted only through **Platform-managed regional groups** (Databricks workspace membership). The earlier manual grant route is closed.
- There is **no granularity by role**. Nothing in the permission model distinguishes Marketing from Sales from Demand Planning.
- There are exactly **two access levels**: the **planner** level, which opens the Level 2.5 templates, and the **regular user** level, which opens Level 1 only.
- Usage can be monitored, but it cannot be gated per day or per role. Staged enablement — for example letting demand planners in before the commercial team — cannot be enforced by permissions; users can only be advised.
- Requests go through a Platform ticket, so plan access well ahead of a go-live rather than in the launch week.

**Note — Which people get which level**

The mapping of individuals to the planner or regular-user level is an enablement decision taken per market, not something the tool derives from a job title.

## Related pages

- [Demand Planner guide](../roles/demand-planner.md) · [Sales guide](../roles/sales.md) · [Marketing / GPL guide](../roles/marketing-gpl.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

**Warning — Gaps & Open Questions**

- The mapping of named users to the planner versus regular-user level is decided per market at enablement and is not documented here.

---

# Which items have a statistical baseline

## Who should read this page

Anyone capturing a forecast in HERO, in any market. This page explains a difference that changes how you work, and it is one of the few things that varies from market to market.

## Purpose

Some parts of the portfolio arrive in HERO with a Daybreak statistical baseline underneath them and some do not. What decides that is a market-level agreement, not the channel and not the item class. This page states the rule and shows how it currently differs between markets.

## The rule

Each market agrees which parts of its portfolio will be forecast statistically.

- **Where Daybreak produces a baseline**, that baseline is the starting point. The team layers enrichments and base trend adjustments on top of it, and the Resultant is never overwritten.
- **Where the market has agreed not to forecast a segment statistically**, there is no baseline underneath. The **full forecast volume is captured as a Base Trend enrichment at Level 1**, and the Level 1 lock is essentially all base trend, with no statistical signal to challenge against.

The practical question to ask about any item is therefore not "is this Direct Import?" or "is this a FAN item?" but "did this market agree to forecast this segment statistically?"

## How it differs by market

| Market | Direct Import (DI) | FAN |
|---|---|---|
| United Kingdom (pilot) | Not forecast statistically. Full volume captured as base trend at Level 1, built bottom-up by the Key Account Manager (KAM) partner by partner. | Not forecast statistically. Volume owned by the regional category team; the KAM validates timing and feasibility. |
| United States | Forecast statistically. DI carries a baseline in the Resultant and behaves like any other segment: enrichments and base trend adjustments layer on top. | Not forecast statistically. |

## FAN at United States go-live

At United States go-live the carry-forward is held for FAN. Because FAN has no statistical proposal underneath it, **no base trend adjustment is needed to force that hold**: what already sits in the carry-forward is the starting point. As future periods are loaded, HERO is the tool used to reflect the forecast aligned by the regional and brand teams, and base trend adjustments are the mechanism for doing so. *(Ratified by Rene Bartoli, process owner, 7 August 2026. This supersedes an earlier working description of the hold being forced through a system-generated Level 1 base trend adjustment.)*

## Related pages

- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md)
- [Roles & what each role does in HERO](roles-permissions.md)

**Warning — Gaps & Open Questions**

- **EMEA treatment is not recorded here.** How Europe treats Direct Import and FAN has not been confirmed for this page.
- **Which other segments, if any, sit outside the statistical model** in each market has not been enumerated beyond DI and FAN.

---

<!-- docs/tools/hero-portal.md -->

# HERO portal

## Who should read this page

All users. The portal is where every HERO session starts and ends.

## Purpose

Describe the single working page where you select scope, download a workbook, and upload it back.

## What the portal does

The current **HERO (Hasbro Enrichment & Reconciliation Optimizer)** portal centres on one working page where you:

1. Select **Business Unit**.
2. Select **Forecast Partner**.
3. Optionally narrow by **Brand**.
4. Select **Fiscal Year**.
5. Decide whether to **Generate Forecast-Partner Reconciliation Data**.
6. **Download** a workbook.
7. **Upload** a workbook.

**Warning — The All Forecast Partners switch**

If you select the special **All Forecast Partners** value at download, HERO switches into **BU-SKU reconciliation mode** instead of the standard forecast-partner reconciliation path. See [BU-SKU / Level 2.5 mode](bu-sku-level-25-mode.md).

**Tip — Enrichment-only vs reconciliation download**

If you only need to add or update enrichments, download an **enrichment-only** workbook — it is faster because reconciliation data is skipped.

## Related pages

- [End-to-end workflow](../workflows/end-to-end-workflow.md)
- [Timing & system sync](../workflows/timing-system-sync.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/tools/enrichment-capture-template.md -->

# Enrichment Capture Template (ECT)

## Who should read this page

Sales / KAM and Marketing / GPL users who author event-driven enrichments; Demand Planning when reviewing.

## Purpose

Explain when to use the **Enrichment Capture Template (ECT)** and which enrichment types it supports.

## When to use it

Use the enrichments workflow when you have a **real-world event or overlay** tied to an item, channel, and time period — promotions, sets, pre-orders, Trade / pallet adjustments (TMO), marketing inputs, and demand-planning overlays.

**Tip — Enrichments vs reconciliation**

Use **enrichments** for dated business events. Use **reconciliation** when the ask is effectively *"change the final number for these weeks."* See [Forecast Reconciliation Template (FRT)](forecast-reconciliation-template.md).

## Supported enrichment types

| Type | Use for | Required extra field |
|---|---|---|
| `RETAIL_PROMOTION` | Promo / retail event | Retail Promotion Mechanism; Price Discount % when relevant |
| `SET` | Set build / one-time pipeline fill | — |
| `SAMPLE` | Free sample volume | — |
| `PRE_ORDER` | Committed launch volume | — |
| `TMO` | Trade / pallet adjustment | Pallet Tag; SPU SKU optional |
| `PHASE_OUT` | Item should no longer carry a normal baseline | — |
| `EXCESS_DEPLETION` | Depletion-style adjustment (excess inventory) | — |
| `DEMAND_PHASE_SHIFT` | Re-phasing demand between weeks (pull-forward / push-out, e.g. deals): author a **positive + negative pair** — a positive row where the demand lands, a negative row where it is taken from | — |
| `SUPPLY_SHORTAGE_COMP` | Compensating item for a shortage | Shortage Planning SKU |
| `MARKETING` | Marketing overlay | `ALL_FORECAST_PARTNERS` allowed |
| `DEMAND_PLANNING` | Demand-planning overlay | `ALL_FORECAST_PARTNERS` allowed |

**Note — Status values**

`PROPOSED` = planned / working input · `CONFIRMED` = approved active input · `DECLINED` = preserved for visibility in the template and audit trail, but **excluded from calculated downstream outputs**. As of the **20 July 2026 release**, setting a row to `DECLINED` is the recommended way to remove its effect — see *Cancelling or removing an enrichment* below.

**Tip — Re-phasing demand: use DEMAND_PHASE_SHIFT, not SET (ratified, 16 July 2026)**

When the business decision is to **move existing demand between weeks** (deals, pull-forwards, ladder buys — and in general demand timing changes that do **not** originate from problems in history), use a `DEMAND_PHASE_SHIFT` **positive + negative pair** instead of `SET`. Reserve `SET` for a **true set build**; if a true set build also pulls existing demand forward, offset it with **negative `SET` rows** on the weeks the demand comes from — the same enrichment type for both legs, consistent with the ladder rule (DPS pair). That `SET` pair does **not** cover the case where the baseline already carries the fill — see *NPI channel fill* below.

**Tip — NPI channel fill: negative base trend plus positive SET (corrected, 7 August 2026)**

When the Daybreak New Product Introduction (NPI) launch baseline **already embeds the channel fill** in its curve, this is not a `SET` pair. Enter a **negative base trend adjustment in F1** for the excess the baseline encoded, plus a **positive `SET` of equal magnitude in F1** to make the fill visible as a discrete commitment for allocation and supply sizing. Both legs sit on exactly the same weeks — the launch window — so neither carries into the next cycle and neither needs manual retirement.

The leg types differ on purpose. Base trend adjustments are not cleansed from history; they adjust the forward baseline. History cleansing runs in the **opposite direction** to the enrichment, so cleansed history is actual shipments minus the `SET`, which leaves replenishment demand only and stops the model relearning the fill next year. Two offsetting `SET` rows would hold the F1 total just as well, but they net to zero in the cleansing calculation and the fill would be relearned.

The two magnitudes do not have to match: the negative base trend is the excess the baseline assumed, the positive `SET` is the fill actually agreed, and where they differ the total moves, which is correct. True up the `SET` against the fill actually shipped before the period closes, or the residual enters next year's baseline.

Where the baseline does **not** carry the fill — new distribution, new stores, a partner the baseline has never served — there is no excess to correct, so no negative base trend. Enter a positive `SET` for the one-time fill, and if the new distribution also lifts the ongoing run rate, capture that lift as a separate positive base trend adjustment. The question that separates the two cases is simply: does the baseline already carry this volume?

**Note — Boundary with reconciliation**

If the phasing issue stems from the **baseline / history** — defects or one-off events in history whose adjustment was not made in time, or that cannot be explained by commercial actions — correct it through **reconciliation** (base trend adjustment), not an enrichment. `DEMAND_PHASE_SHIFT` is for known commercial timing events; reconciliation is for history-driven baseline corrections.

**Warning — No single-row move; SUPPLY_SHORTAGE_COMP stays tracking-only**

A single `DEMAND_PHASE_SHIFT` row does **not** automatically move demand — it takes **two rows** (positive where the demand lands, negative where it comes from). Do **not** confuse it with **Channel Shift** (a reconciliation control): Channel Shift moves demand between channels (`DOM` ↔ `DI`) and creates the offsetting negative **automatically**; `DEMAND_PHASE_SHIFT` moves demand between **weeks** and both legs are authored manually. `SUPPLY_SHORTAGE_COMP` remains **tracking metadata**: it does not move volume between SKUs. Tracking-only refers to the forward forecast. The relationship it records is used at history cleansing, where it raises the adjusted demand of the item that was unavailable and reduces the same quantity from the substitute. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works).

**Note — TMO comes from FAST**

`TMO` rows are sourced from **FAST** and the template is seeded from FAST once a month. Do **not** author or edit TMO directly in the template — that would desynchronise FAST and Logility.

**Tip — Confirmed vs Proposed horizon**

Use `CONFIRMED` for near-term events inside the supply window; use `PROPOSED` for longer-horizon events that are not yet locked. `EXCESS_DEPLETION` and `PHASE_OUT` are separate types in the tool; "Phase-Out" is the business term for taking an item off normal carry-forward, and excess-inventory depletion is captured the same way.

## Working in the template (Excel, formulas, copying data)

The HERO templates are **ordinary Excel files** — while you prepare your entries you can use anything Excel offers: copy/paste from other files, `VLOOKUP` and other formulas, and so on. Before you **upload** the file to HERO, take these precautions (mostly good practice, not always hard rules):

- **Don't overwrite rows.**
- **Replace any formulas with their values** before uploading (copy → paste as values). The upload expects static values, not live formulas.
- **Avoid blank rows** — don't leave empty lines between enrichments. As of the **20 July 2026 release**, upload validation detects mid-sheet blank rows (and blanked headers) and rejects the upload with an explanation, instead of silently dropping the data below them.
- **Insert any new or copied row below the last row that has data.**

## Cancelling or removing an enrichment

**Warning — Never delete rows**

Do **not** delete enrichment rows. Every enrichment must stay traceable through its key (Enrichment ID) — deleting a row breaks that audit trail.

As of the **20 July 2026 release**, the recommended way to cancel an enrichment is to set its **Status** to `DECLINED`. A `DECLINED` row is preserved in the template and the audit trail for visibility, but is **excluded from calculated downstream outputs** — its effect is removed from the forecast while the record of the decision remains.

**Note — Previous method: zeroing the quantity**

Before the 20 July 2026 release, Status was a log-only field and the only way to remove an enrichment's effect was to **zero the quantity** (set *Expected Shipment Lift* to 0). Zeroing still removes the effect, but `DECLINED` is now the preferred method because it removes the effect *and* records the decision explicitly in the audit trail.

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Tab-by-tab walkthrough](../workflows/tab-by-tab-walkthrough.md)

**Warning — Gaps & Open Questions**

- The 16 July 2026 decision is **formally ratified**; taxonomy and training sources were corrected the same day (Taxonomy Playbook v2, Examples for Enrichment Training v2, Enrichment Training Examples Deck v2, Scenarios & Examples v2, MOD2 deck v4, EU Day1 deck v3). Superseded versions should be retired/archived so only the 2026-07-16 versions circulate.

---

<!-- docs/tools/forecast-reconciliation-template.md -->

# Forecast Reconciliation Template (FRT)

## Who should read this page

Demand Planning (primary) and Sales when proposing final-number changes.

## Purpose

Explain when to use the **Forecast Reconciliation Template (FRT)** and what is editable on it.

## When to use it

Use reconciliation when the business needs to **directly change the final week-level number** after enrichments are already considered. If the ask is *"change the final number for these weeks,"* it belongs here rather than in enrichments.

## What you can edit

**Note — Editable controls only**

On the reconciliation tab, edit only these fields:

- Weekly **Base Trend Adjustments**
- **Adjusted Planning SKU** (Version Change)
- **Version Adjustment Start Week** / **End Week**
- **Channel Shift Proportion**
- **Channel Shift Start Week** / **End Week**

Treat item-dimension fields, Lifecycle Status, Blended A-Price, baseline totals, and the rendered baseline / sales-enrichment / marketing-and-demand-planning weekly columns as **read-only context**.

**Warning — Two rules to remember**

- **Deltas, not absolutes** — reconciliation does not support an absolute overwrite. Enter a plus/minus change.
- **One structured control per row** — do not combine an Adjusted Planning SKU (version change) and a Channel Shift Proportion on the same row.

**Tip — Which columns do Demand Planning / Marketing edit? (incl. Level 2.5)**

Enter your weekly adjustments in the **Baseline Trend Adjustments** columns — the **orange** ones. That is the editable weekly area on both the standard and the BU-SKU / Level 2.5 reconciliation templates. After you upload, HERO **automatically classifies** the entry and it appears under the **Marketing and Demand Planning** weekly columns — the classification is based on **who entered it and when**. So: you edit in *Baseline Trend Adjustments*, and your change shows up under *Marketing and Demand Planning* after upload. The template's **Instructions** page also covers this.

## What changed in the 20 July 2026 release

- **Clearer template layout** — cleaner labels and formatting, and **rounded display values** so the template is easier to read. (Rounding on the weekly display does not change the underlying stored values.)
- **Clearer calculated forecast totals** — the template now shows calculated totals so you can **see the effect of your entries before you upload**.
- **Level 1 / Level 2.5 behaviour tightened** — adjustments are handled more consistently between the two levels, and the template better explains **what is coming from each level**.
- **Stale or invalid planning SKUs are removed** from reconciliation templates, so you no longer see rows you cannot act on.
- **Fresh templates only** — always download a fresh template before working; avoid stale saved templates, and report any template/dashboard mismatch immediately.

**Warning — Gaps & Open Questions**

- Exact new column labels and the placement/format of the calculated forecast totals are not yet documented — confirm against the released template and add screenshots.
- Confirm the precise rounding rule used for display values (and that stored values remain unrounded).
- Confirm what "tightened" Level 1 / Level 2.5 handling changes in practice for users, if anything beyond clearer labelling.

## Actualized vs forward weeks

Weeks in the actualized period use exact row-level shipment actuals where they exist, and 0 where no exact actual is available; values are zero-floored so negative net shipment weeks render as 0. **Shaded** cells mark the actualized shipment period (historical cutoff); **unshaded** cells are forward forecast weeks.

**Note — Channel shift moves the enrichments too**

A Channel Shift moves demand between `DOM` and `DI`. Make sure any enrichments associated with the moved volume are also moved to the correct channel. Capture a genuine change in total demand separately.

**Tip — Forecasting range (start / end dates)**

To stop forecasting a SKU for a customer, adjust the **forecast calculation range** (set an end date) — distinct from a phase-out enrichment. See [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md).

**Warning — Zero the Version Change / Channel Shift pair once the Forecasting Range is fixed**

A Version Change or Channel Shift creates an offsetting +/− base-trend-adjustment pair for its week range — it never touches the baseline or forecasting range itself. The durable fix is updating the **Forecasting Range**. Once that range is fixed, the offsetting pair must be **manually zeroed**, or it persists as a delta indefinitely (fixing the range without zeroing the pair leaves you wrong for exactly one cycle, then correct).

## Related pages

- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Calculation reference](../examples/calculation-reference.md)
- [BU-SKU / Level 2.5 mode](bu-sku-level-25-mode.md)

---

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

**Warning — A BU-SKU entry is not the final weekly number**

A BU-SKU weekly entry sets the **desired BU-SKU weekly total for the reconciliation-adjustment layer** for that week. HERO then works backward and recomputes the Level 1 partner-level deltas needed to land on that target, distributing by **baseline share** (equal split only when the slice baseline is zero).

This is the opposite of standard reconciliation, which says *"apply this exact delta to this exact Level 1 row."*

## Blank vs 0 vs signed value

| Entry | Meaning |
|---|---|
| **Blank** | Keep the current rendered BU-SKU adjustment total for that week. |
| **0** | Set the BU-SKU adjustment total to zero for that week. |
| **Positive / negative** | Move the adjustment total above / below zero. |

## Governance

**Note — Handoff from Level 1**

Use forecast-partner reconciliation during normal Level 1 review. Once Demand / Marketing reconciliation moves to BU-SKU review, download a **fresh** BU-SKU workbook and make final weekly adjustments there. **Treat older Level 1 reconciliation workbooks as stale** after that handoff. Do not populate both `reconciliation` and `reconciliation_bu_sku` in the same upload.

## Related pages

- [BU-SKU worked examples](../examples/bu-sku-worked-examples.md) — six scenarios showing what moves and what stays fixed.
- [Forecast Reconciliation Template (FRT)](forecast-reconciliation-template.md)
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md) — different mechanism: the range decides *which customers* are forecast; Level 2.5 decides *how an adjustment splits* across them.

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/tools/reference-views-dashboards.md -->

# Reference views & dashboards

## Who should read this page

All users who consume resolved outputs: Sales, Demand Planning (DP), Marketing / Global Product Lead (GPL), Finance, and Supply Chain.

## Purpose

Describe the Power BI views that present resolved HERO (Hasbro Enrichment & Reconciliation Optimizer) outputs, and how they refresh.

**Warning — Timing**

Resolved dashboards refresh **after the backend processing run completes** — they can lag a successful upload. The workbook shows authored intent immediately after download; dashboards match only after the resolved refresh.

## Forecast Enrichment Power BI dashboard

[Open in Power BI](https://app.powerbi.com/groups/ffc77157-ca2d-4b70-9f14-2a1c3842f973/reports/1d7dcc05-0d12-40f8-bd0c-184b82bdd406/e26a15167349ce5185cc?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&bookmarkGuid=92641236-1c4a-4f93-be93-803e0577ab14)

Provides visualisations of baseline forecasts, enrichments, consensus forecasts, and key performance indicators, with drill-down to SKU-level detail. Domestic (DOM) and Direct Import (DI) data are separated; DI forecasts are reflected as base trend adjustments while Domestic forecasts include captain adjustments.

## POS (Point of Sale) Glidepath

[Open in Power BI](https://app.powerbi.com/links/9YKCWlN-jc?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&pbi_source=linkShare)

Four dashboard tabs, consumed in Power BI with input via a web enrichment template:

1. Monthly POS View
2. Global Overview — POS
3. POS Pace Chart (benchmark is the financial or consensus forecast depending on your role)
4. Global Overview — Shipment

## AIM Shipment Revenue Model

[Open in Power BI](https://app.powerbi.com/links/F5YrmkBmfH?ctid=701edd3e-c7a8-4789-b1ce-8a243620d68f&pbi_source=linkShare)

Pages: Cover Sheet, Full-Year Forecast, Cumulative Forecast Chart, Cumulative / Discrete Forecast Table, Brand Cumulative Forecast, plus appendices (Data Sources, Backtest). Source data: SAP HANA table `Z_CV_SUPPLY_CHAIN`. Owner: the AIM team.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Deferred in v0](../reference/deferred-in-v0.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/workflows/end-to-end-workflow.md -->

# End-to-end user workflow

## Who should read this page

All users. This is the spine of a HERO session, from scope selection to re-download.

## Purpose

Give the ordered steps for a complete HERO working session.

## The workflow

1. **Choose your scope.** Open HERO (Hasbro Enrichment & Reconciliation Optimizer); select Business Unit, Forecast Partner, optional Brand, and Fiscal Year.
2. **Decide which workbook mode you need.** Use the normal workbook for enrichments and standard reconciliation. Use **BU-SKU mode** only when you intentionally selected *All Forecast Partners* for a later-stage Level 2.5 review.
3. **Download a fresh workbook.** Always start from the latest download — especially if existing rows may exist or another user may have touched the same slice.
4. **Start with the information and instructions tabs.** Use the **information** tab for mechanics; use the **instructions** tab when you know the business problem but are unsure which HERO path to use.
5. **Make only the edits that belong in that tab.** Event-driven changes → Enrichments. Direct final-number changes → Reconciliation. In BU-SKU mode → signed BU-SKU reconciliation-adjustment totals, not partner-level detail.
6. **Upload the workbook.** If HERO finds validation issues, it returns an **annotated workbook** with dedicated validation-error tabs instead of loading partial data.
7. **Re-download when necessary.** After a validation round-trip, after another user changes overlapping scope, or when the process moves from Level 1 to BU-SKU review.

**Warning — Rejected uploads are not partially saved**

If HERO rejects an upload, it does **not** save the bad rows. It returns an annotated workbook so you can fix the issues and try again.

## Related pages

- [Tab-by-tab walkthrough](tab-by-tab-walkthrough.md)
- [Timing & system sync](timing-system-sync.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/workflows/tab-by-tab-walkthrough.md -->

# Tab-by-tab walkthrough

## Who should read this page

All users authoring in the workbook. Use it as a map of what each tab is for.

## Purpose

Describe every tab in the standard workbook and the BU-SKU workbook mode.

## Standard workbook tabs

| Tab | Type | Use it for |
|---|---|---|
| **information** | Read-only | Quick reference for how HERO behaves; the split between Enrichments, Reconciliation, and BU-SKU mode. Open first if unsure where a change belongs. |
| **instructions** | Read-only | Scenario-based decision aid. Use when you know the business situation but not the HERO path. |
| **summary** | Read-only | Workbook rollup (when reconciliation data is included in the download). |
| **enrichments** | Editable | Event capture: promotions, sets, pre-orders, TMO, marketing overlays. Creates or updates enrichment rows. |
| **reconciliation** | Editable | Forecast-partner reconciliation: review baseline + overlays, then enter final deltas. |
| **enrichment_validation_errors** | Read-only | Row-level enrichment error detail. Only appears when an upload is rejected. |
| **reconciliation_val_errors** | Read-only | Row-level reconciliation error detail. Only appears when an upload is rejected. |
| **data_validation_ranges** | Hidden helper | Dropdowns and lookups. **Never edit.** |
| **_hero_template_scope** | Hidden helper | Carries the workbook scope so HERO can verify the upload matches the download. **Never edit.** |

## BU-SKU workbook mode

**Note — Triggered by All Forecast Partners**

Selecting *All Forecast Partners* at download produces a later-stage reconciliation workbook, **not** the normal forecast-partner workbook.

- **Visible scope:** aggregated to Business Unit + Planning SKU + Shipment Channel + Fiscal Year. Forecast Partner fields stay blank / hidden.
- **Editable weekly behavior:** edit signed BU-SKU weekly reconciliation-adjustment totals in units. Blank keeps the current rendered total; `0` sets it to zero; positive and negative values are allowed.
- **Upload treatment:** HERO keeps only changed weeks and range controls, then redistributes the net effect to forecast-partner rows by baseline share (even split if the baseline total is zero).

**Warning — Do not mix modes**

Do not upload both standard reconciliation and BU-SKU reconciliation from the same workbook. Once teams move into BU-SKU review, older Level 1 workbooks are stale. Author BU-SKU rows only on the `reconciliation_bu_sku` tab and leave partner fields blank.

## Editable reconciliation fields

Edit only: weekly **Base Trend Adjustments**, **Adjusted Planning SKU**, **Version Adjustment Start/End Week**, **Channel Shift Proportion**, **Channel Shift Start/End Week**. Everything else (item dimensions, Lifecycle Status, Blended A-Price, baseline totals, rendered weekly columns) is read-only context.

## Related pages

- [Field-by-field reference](field-by-field-reference.md)
- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/workflows/timing-system-sync.md -->

# Timing & system sync

## Who should read this page

All users. Understanding *when a change actually takes effect* is one of the most important parts of using HERO (Hasbro Enrichment & Reconciliation Optimizer) correctly.

## Purpose

Explain why a download, an upload, a dashboard refresh, and a Logility publication do **not** all happen at the same time.

## What updates when

| Action / surface | Reads from | When it takes effect |
|---|---|---|
| Download any workbook (enrichment-only, standard, or BU-SKU) | Current HERO / Logility data for the selected scope | Immediately, at download (a point-in-time extract) |
| **Upload** a valid workbook | HERO raw authored state | Authoring state is captured **immediately**; the export later emits only the rows you changed |
| A **Level 2.5 (BU-SKU) reconciliation** change broadcast down to Level 1, and shown in the dashboard | Resolved weekly reporting layer | After the next **fan-out** run — **not instantly** |
| View **resolved dashboard / reporting** | Resolved weekly reporting layer | After the fan-out run completes |
| **Publish to Logility** | Resolved HERO state packaged into the export surfaces | **Only through the weekly Friday export pipeline** |

## The fan-out (how Level 2.5 changes reach Level 1)

A Level 2.5 adjustment does not drop to Level 1 the instant you save it. A **post-processing ("fan-out") job** picks it up, distributes it down to the Level 1 partner rows, and refreshes the dashboard-facing Level 1 view.

**Note — Fan-out schedule**

The fan-out runs on a frequent, day-of-week schedule so Level 2.5 changes reach Level 1 quickly:

- **Monday–Thursday (UK workday):** 08:00, 10:00, 12:00, 14:00, 16:00 and 18:00 `Europe/London`.
- **Friday (UK morning):** 08:00, 10:00 and 12:00 `Europe/London`.
- **Monday–Thursday late-night catch-up:** 23:00 `America/New_York` (≈04:00 `Europe/London` next day) — so UK users start the next workday with any late-uploaded changes already fanned out.

A Level 2.5 change becomes visible at Level 1 / in the dashboard at the **next** scheduled run.

## The dashboard has its own cadence

The Power BI dashboard is not refreshed by your upload. It is rebuilt on a schedule of its own, after HERO's materialisation step has run.

**Note — Dashboard refresh**

The current cadence is **90 minutes**, with a target of one hour maximum. The constraint is hosting: the dashboard runs in an individual session rather than a service context.

If you have heard "15 minutes" quoted, that figure described something else — the delay between a load and the underlying data being updated, not the dashboard's own refresh cadence.

## What runs on its own, and what still needs a person

**Tip — HERO does run scheduled jobs**

Running without anyone triggering it: ingestion of the Resultant baseline on its own scheduled path, the cycle refresh and post-processing jobs that build each cycle's render snapshots, the previous-cycle computation, dashboard materialisation and the Power BI refresh, and the Friday export batch — which runs whether or not anything changed that week.

Still needing a person: anything changed directly in Logility, because HERO never reads it. Seeing a new cycle, because your workbook is a point-in-time snapshot that has to be re-downloaded. And clearing a stale adjustment, because a display fix corrects what you see, not what you entered.

## Publication to Logility

**Warning — Logility is updated only through the Friday export**

Uploading a workbook does **not** push Logility. HERO publishes to Logility **only through the weekly Friday noon Eastern export pipeline**. Anything authored during the week is held in HERO until that pipeline runs. (Downstream transport from Databricks into Logility is external orchestration — see [Batch orchestration & updates](../reference/batch-orchestration-updates.md).)

## Urgent changes — the three governed paths

**Warning — The weekly export is not skippable — use one of these three paths instead**

HERO exports to Logility only through the weekly Friday export, regardless of urgency. If a change cannot wait for that cadence, it must go through one of these three governed paths, depending on what it is:

1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today — never flowing into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0; this is a deliberate, phased choice. See [Deferred in v0](../reference/deferred-in-v0.md).

## Practical rules

**Tip — Four rules to live by**

- A workbook download is a **point-in-time** extract of the current state.
- A successful upload updates HERO **authoring** state immediately, but the dashboard and Level 1 view only catch up at the **next fan-out run** (multiple times per UK workday — see the schedule above).
- **Re-download** if someone else has touched the same scope — especially before a later-stage reconciliation session.
- Publication to Logility happens **only through the Friday export pipeline** — not on upload.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md) — the full export step and downstream orchestration detail.
- [Where HERO fits in the planning flow](../getting-started/hero-in-the-cycle.md)
- [FAQ & common gotchas](../help/faq-common-gotchas.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/workflows/field-by-field-reference.md -->

# Field-by-field reference

## Who should read this page

Anyone entering data in the enrichment or reconciliation tabs. Use it to look up what a field means and whether it is editable.

## Purpose

Define each field, whether it is required / editable, and its allowed values.

## Enrichment template fields

| Field | Required? | Allowed values / source | Notes |
|---|---|---|---|
| Business Unit | Required | Dropdown of BUs the user is authorised for | Defines which time series the enrichment applies to. As of the 20 July 2026 release, users only see the Business Units they are authorised to work with. |
| Forecast Partner | Required | Dynamic dropdown by BU + Brand | `ALL_FORECAST_PARTNERS` only for authorised users and only on MARKETING / DEMAND_PLANNING rows. |
| Forecast Partner Customer Number | Required | Auto-populated | From the selected Forecast Partner. |
| Planning SKU | Required | Dynamic dropdown in scope | The planning item code. |
| SKU Description | Read-only | Auto-populated | Confirm the item. |
| Shortage Planning SKU | Required for `SUPPLY_SHORTAGE_COMP` | Text | Tracking only in the forecast; drives the history cleansing. |
| Enrichment Type | Required | See [ECT types](../tools/enrichment-capture-template.md) | Determines bucket and downstream treatment. |
| Status | Required | `PROPOSED` / `CONFIRMED` / `DECLINED` | As of the 20 July 2026 release, `DECLINED` rows are preserved in the template / audit trail but **excluded from calculated downstream outputs** — the recommended way to cancel an enrichment. |
| Shipment Impact Start Date | Required | `YYYY-MM-DD` | Defines which fiscal weeks receive the enrichment. |
| Shipment Impact End Date | Optional | `YYYY-MM-DD` | With the start date, sets weekly coverage. If left blank, the enrichment is treated as a **single-week** event (the start week only). |
| Shipment Channel | Required | `DOM` / `DI` | Defines the time series. The reconciliation model uses `DOM` (domestic) and `DI` (direct import). |
| Expected Shipment Lift, percent | Conditional | Excel percent (25% = 0.25) | Use percent **or** units, never both. Converted against baseline. |
| Expected Shipment Lift, units | Conditional | Number | Use units **or** percent, never both. Spread evenly across covered weeks. |
| Retail Promotion Mechanism | Required for `RETAIL_PROMOTION` | `DISCOUNT` / `BOGO` / `COUPON` / `OTHER` | Classification metadata. |
| Price Discount, percent | Optional | Excel percent | Commercial metadata for audit. |
| Pallet Tag | Required for `TMO` | Text | Unique within one upload; groups TMO pallet rows. |
| Special Planning Unit (SPU) SKU | Optional (`TMO` only) | Text | Tracking only; does not change math. |
| Store Count | Optional | Whole number | Supporting context. |
| Notes | Optional | Free text | Supporting context. |
| Brand / Lifecycle Status | Read-only | Auto-populated | Context lookups. |
| Pallet ID / Enrichment ID / Submitted By / Operation Type / Upload Batch ID | Read-only | Auto-populated | Audit and traceability. |

## Reconciliation fields (non-weekly, editable controls)

| Field | Required? | Notes |
|---|---|---|
| Adjusted Planning SKU | Optional | Version-change target. **Do not** use with Channel Shift Proportion on the same row. |
| Version Adjustment Start / End Week | Required with Adjusted Planning SKU | Fiscal week numbers. |
| Channel Shift Proportion | Optional | e.g. `0.25` = 25%. **Do not** use with Adjusted Planning SKU on the same row. |
| Channel Shift Start / End Week | Required with Channel Shift Proportion | Fiscal week numbers. |

**Note — Read-only reconciliation context**

Business Unit, Forecast Partner, Fiscal Year, Shipment Channel, Planning SKU, SKU/Brand/Parent fields, Lifecycle Status, Blended A-Price, all *Total …* columns, and all *Previous Cycle …* / *Cycle-on-Cycle Variation* columns are read-only context.

## Reconciliation weekly field families (Wk 1–Wk 52)

| Family | Editable? | Meaning |
|---|---|---|
| Baseline | Read-only | Current baseline or shipment actuals in the actualized period. |
| Sales Enrichment | Read-only | Weekly contribution from sales / event enrichments. |
| Marketing and Demand Planning | Read-only | Weekly contribution from marketing / DP enrichments. After upload, Demand Planning / Marketing reconciliation entries are **classified here** (see note). |
| **Baseline Trend Adjustments** | **Editable** | Numeric delta in units — the **orange** columns; the main editable weekly area in standard and Level 2.5 reconciliation. |

**Note — Where your adjustment lands after upload**

Demand Planning and Marketing **enter** their weekly adjustments in the editable **Baseline Trend Adjustments** (orange) columns. On upload, HERO **classifies** the entry based on **who entered it and when**, and the value then appears under the read-only **Marketing and Demand Planning** weekly columns.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [Tab-by-tab walkthrough](tab-by-tab-walkthrough.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/workflows/forecast-range-calculation.md -->

# Forecast Calculation Range & Disaggregation

## Who should read this page

Sales / Key Account Managers (KAMs), Demand Planning (DP), and Brand Captains — anyone whose item should be forecast for some customers and periods but not others.

## Purpose

Explain what the **Forecast Calculation Range (FCR)** is, how it is generated and adjusted, and why it matters for **disaggregation** — how the baseline is split down to customers.

**Note — Name**

The canonical term is **Forecast Calculation Range**. An underlying pipeline guide informally calls it "Forecast Calendar Range"; treat *Calculation* as canonical.

## What the forecast range is

The FCR is a **per-product window of Start and End weeks** that tells Logility when a product should be planned: *"this product should be available from week X to week Y."* It is the gate that decides which weeks — and, at customer level, which customers — receive a forecast.

## How the range is generated

The range is built bottom-up in four steps, starting from launch data:

1. **Planning SKU dates** — extract on-shelf dates and quantities from **P2M**, then apply region- and channel-specific **lead-time** logic to work out when items must ship to be available. End dates are extrapolated from the last year with P2M quantities.
2. **Level 1 (partner)** — the dates are replicated and adjusted per forecast partner.
3. **Level 2 (Parent SKU)** — aggregated using the **earliest Start and latest End** across items sharing the parent SKU, partner, and channel.
4. **Level 3** — extended to Parent SKU + Business Unit; this is the file loaded into Logility.

After initial load, **Logility is the source of truth** for the range.

## How you control / adjust it

Commercial teams receive **Excel files with the proposed Start/End dates** for each SKU and forecast partner and **adjust them manually** using customer knowledge — delayed launches, exclusivity, and so on. The Level 1 files carry blank "New Start / End Date" override columns and a **status flag** showing whether the range matches Logility or differs. The adjusted dates are then updated in Logility.

## Why it matters for disaggregation

**Warning — Default spread causes bad forecasts**

By default a SKU can extend to **all** forecast partners, which spreads demand to customers that will never take it. The range is how you include **only the relevant customers**.

- **Exclusives** — for a single-customer SKU (e.g. an Amazon exclusive), **set/adjust the end date** so other partners are excluded and the forecast does not spread to them.
- **Stopping a SKU for a customer** — set an end date to stop forecasting that SKU/customer. This is distinct from a phase-out enrichment (which takes the item off normal carry-forward more broadly).
- **Missing or inactive items lose forecast** — if a SKU is inactive or missing at any hierarchy level during disaggregation, the system can assign **zeros**, losing the forecast. Complete, accurate data at every level is required for correct allocation.

## Scope, validation, and data quality

- Both **8-digit and 9-digit (wave) SKUs** are processed by the range pipeline.
- SKUs **without supporting P2M data** are **deactivated**, and files are generated to classify the reason for the missing dates.
- If a computed **End Date falls before the Start Date**, the row is flagged as a data issue for review.
- Regional teams run **periodic P2M audits** to remove invalid or outdated entries.

## How it relates to the baseline

The statistical model output is generated **first** (forecast before range), and the **range layer is then applied** on top.

## How history cleansing works

Cleansing is how the model is told what really happened, as opposed to what shipped. It is applied in the **Adjusted Demand array**, the editable layer the statistical baseline learns from, and never in raw Actuals.

**The mechanic.** Cleansing runs in the **opposite direction to the enrichment**. When a period closes, cleansed history is actual shipments minus the `SET`. Base trend adjustments are **not** cleansed: they adjust the forward baseline and never enter the cleansing calculation.

That is why a `SET` does two jobs at once. It holds volume in the forecast now, and it is the instruction that removes that same volume from history later. It is also why a pair of offsetting `SET` rows nets to zero in cleansing, which is correct when demand only moved between weeks and nothing new was created, and wrong when the point is to strip a volume out of what the model learns.

**Supply shortage compensation.** When a shortage pushes demand onto a substitute item, `SUPPLY_SHORTAGE_COMP` records the relationship between the item that was unavailable and the item that absorbed the demand. At cleansing, that relationship raises the adjusted demand of the item that was unavailable by the compensating quantity, and reduces the same quantity from the substitute. The model then learns the demand the absent item would have had, and does not carry forward an inflated projection for a substitute that only sold because of the shortage.

Capturing that relationship correctly matters even though nothing moves in the forward forecast: the intent is to use it to **automate** the historical cleansing, so the correction happens without a planner having to reconstruct it by hand.

**Note — This is the initial logic, and it is expected to change**

The rules on this page are the starting point, not a finished design. They will evolve as the programme accumulates enough cycles to evaluate which cleansing treatment actually improves forecast accuracy. Two objectives guide that evolution: cleansing should measurably improve accuracy, and it should be automated far enough that it does not consume planner time. Treat the current rules as the working method and expect them to be refined.

## Related pages

- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md) — the in-template "set an end date to stop forecasting" usage.
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md) — note the difference: the **range** decides *which customers* receive a forecast; **Level 2.5** decides *how an aggregate adjustment is split* across them.
- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/examples/calculation-reference.md -->

# Calculation reference (worked examples)

## Who should read this page

Anyone who needs to predict what a number will do after an enrichment or reconciliation entry — Sales, Demand Planning, Marketing / GPL.

## Purpose

Show, with worked numbers, how HERO resolves enrichments and reconciliation into the final forecast.

## Foundational concept: baseline + enrichment = consensus

**Note — Two layers, one number**

**Baseline** is what the statistical model produces from history alone — pattern, trend, seasonality (owned by Demand Planning). **Enrichment** is the business knowledge layered on top — promos, sets, base trend, channel shifts — that the model cannot infer from history (owned by Sales + Brand Captain). The **consensus forecast** is the agreed number, with every adjustment traceable to its driver and owner. Neither layer is a place to reconcile to a target number; both are evidence-based.

## Key principle: Set vs Base Trend

The single most important modelling choice in enrichment is whether an adjustment should **cleanse out of history** or **enter the baseline permanently**.

| | Commercial building block (e.g. Set) | Base Trend Adjustment |
|---|---|---|
| **Effect** | One-time; removed from history after the period | Structural; becomes part of the baseline going forward |
| **Next year's model** | Will **not** learn it | **Will** learn it as normal |
| **Use for** | Pipeline fills, out-of-aisle, ladders / timing shifts, pre-orders, one-off substitutions, fan spikes | POD expansion / reduction, customer discontinued, recurring year-over-year temporality, ongoing run-rate corrections |

**Warning — Common mistake**

Using a Base Trend Adjustment to handle a **timing** move (a ladder or a lumpy buy). It cleanses correctly the first cycle, but the negative leg permanently distorts the baseline. **When in doubt — if the change is one-time, use a Set.**

## 1. Units lift vs percent lift

Baseline = 100 units/week; event covers weeks 5–15 inclusive (**11 covered weeks**).

- **Percent (+10%):** resolved against baseline first → each week gets 100 × 10% = **10 units**; total lift = **110 units**.
- **Units (+1,200):** spread evenly → each week gets 1,200 / 11 = **109.09 units** (before display/export rounding).

**Tip — Coverage is by fiscal week, not daily proration**

HERO expands enrichments by fiscal-week coverage. A mid-week start/end date still allocates by the fiscal weeks whose start dates fall inside the range.

## 2. Current-cycle enriched forecast

For one week: Baseline 100 + Base Trend Adjustment 15 + Sales Enrichment 20 + Marketing & DP 5 = **140 units**.

## 3. Version change (net-zero SKU move)

Source SKU = 200 units/week for weeks 10–12; Adjusted Planning SKU = target; Start Wk 10, End Wk 12. HERO derives a **negative delta** on the source and a matching **positive delta** on the target for those weeks. Use the structured Version Adjustment controls — do not zero rows manually, and do not combine with a channel shift.

## 4. Channel shift

Weekly resolved demand = 100 units/week; Channel Shift Proportion = 0.25; weeks 12–20. HERO moves **25 units/week** from the source channel to the opposite channel. If total demand is also changing, capture that separately.

## 5. BU-SKU (Level 2.5) disaggregation back to Level 1

Current BU-SKU week-10 adjustment total = 150; user edits it to 100 → required net change = **−50**. Baseline shares: FP A 50%, FP B 30%, FP C 20%. HERO redistributes: FP A −25, FP B −15, FP C −10. (If all eligible baselines are zero, HERO splits evenly.) See [BU-SKU worked examples](bu-sku-worked-examples.md) for what moves afterward.

## 6. Enrichment-to-consensus aggregation

One series-week: RESULTANT_FORECAST 100, Promo +20, Marketing +10, TMO +5 → positive non-TMO enrichments contribute +30 to the positive HERO adjustment path; TMO stays in the TMO path → final consensus = 100 + 30 + 5 = **135**.

## Worked scenario examples (Module 2)

**Example — Historical promo spike that is not repeating**

Last year's spike is baked into the trend, so the stat model overstates F1–F4. **Use a negative Base Trend Adjustment** for the contaminated period only; the corrected baseline returns to the true run-rate. Owner: Brand Captain / DP.

**Example — Recurring year-over-year temporality missing**

A seasonal pattern is not reflected because prior history did not capture it cleanly. **Use a Base Trend Adjustment** (not a one-off set) so the model learns it permanently and the correction is not re-entered each cycle. Owner: Sales.

**Note — Rounding on export and on template display**

Internally a unit spread can be fractional (e.g. 109.09 units/week). On export, published values are **rounded to the nearest whole integer**, with halves rounding **away from zero**. Published outputs are fully populated (no blank cells). As of the **20 July 2026 release**, reconciliation templates also show **rounded display values** for readability — the underlying stored values remain unrounded. *(Confirm the display-rounding rule matches the export rule — not yet documented.)*

## Related pages

- [BU-SKU worked examples](bu-sku-worked-examples.md)
- [Enrichment Capture Template (ECT)](../tools/enrichment-capture-template.md)
- [Field-by-field reference](../workflows/field-by-field-reference.md)
- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/examples/bu-sku-worked-examples.md -->

# BU-SKU worked examples

## Who should read this page

Demand Planning and Brand Captains working in BU-SKU (Business Unit–SKU) / Level 2.5 reconciliation.

## Purpose

Show what HERO holds fixed and what can still move after a Level 2.5 adjustment, using six worked scenarios.

## The core rule

**Warning — Level 2.5 holds the *adjustment target*, not the final total**

When you type a BU-SKU weekly value, you are setting the **target adjustment** for that week — not the final number. HERO then splits that target across the partners **by their share of the baseline**, and recomputes it whenever the baseline changes.

`Final weekly total = Baseline + Reconciliation adjustment + Enrichments`

The Level 2.5 edit fixes only the **reconciliation adjustment** piece. The other two pieces can still move — which is what the examples below show.

In every example below there are two partners, **Target** and **Walmart**, that roll up to one **BU-SKU** total.

---

## Example 1 — The baseline grows later

You set a **+40** adjustment. Later the baseline grows, but you don't touch your +40.

**At the time you set it:**

| Partner | Baseline | Share | Your +40, split by share | Final |
|---|--:|--:|--:|--:|
| Target | 100 | 25% | **+10** | 110 |
| Walmart | 300 | 75% | **+30** | 330 |
| **BU-SKU** | **400** | | **+40** | **440** |

**Later — baseline grows to 120 / 360 (shares unchanged):**

| Partner | Baseline | Share | Your +40, split by share | Final |
|---|--:|--:|--:|--:|
| Target | 120 | 25% | **+10** | 130 |
| Walmart | 360 | 75% | **+30** | 390 |
| **BU-SKU** | **480** | | **+40** | **520** |

**Note — Takeaway**

**Stayed fixed:** your adjustment (+40). **Moved:** the final total (440 → 520), because the baseline grew underneath it.

---

## Example 2 — The split between partners changes later

Same **+40**. The total baseline stays 400, but it shifts from 100/300 to 200/200, so the **shares** change.

| | Baseline | Share | Your +40, split by share | Final |
|---|--:|--:|--:|--:|
| **Before** Target | 100 | 25% | +10 | 110 |
| **Before** Walmart | 300 | 75% | +30 | 330 |
| **After** Target | 200 | 50% | **+20** | 220 |
| **After** Walmart | 200 | 50% | **+20** | 220 |

**Note — Takeaway**

**Stayed fixed:** your adjustment (+40) *and* the BU-SKU total (440). **Moved:** the per-partner split (10/30 → 20/20). Same headline number, different distribution underneath.

---

## Example 3 — Someone adds Level 1 enrichments later

Start from Example 1 (finals 110 / 330, BU-SKU 440). Later, enrichments are added: **+15** to Target, **+5** to Walmart.

| Partner | Final before | + Enrichment | Final after |
|---|--:|--:|--:|
| Target | 110 | +15 | 125 |
| Walmart | 330 | +5 | 335 |
| **BU-SKU** | **440** | **+20** | **460** |

**Note — Takeaway**

**Stayed fixed:** your adjustment (+40). **Moved:** the final total (+20). Enrichments are a **separate component** — your Level 2.5 adjustment does not absorb or block them.

---

## Example 4 — Someone changes Level 1 reconciliation later

Here the focus is the **reconciliation deltas**, not the final units. There is already Level 1 reconciliation of **+5 / +15**, and your BU-SKU target is **+40** (which should land partner totals at +10 / +30).

| Partner | Existing L1 recon | Needs to reach | Extra delta HERO adds |
|---|--:|--:|--:|
| Target | +5 | +10 | **+5** |
| Walmart | +15 | +30 | **+15** |

**Later, the L1 reconciliation is changed to 0 / +20.** HERO re-calculates the extra deltas so the target still holds:

| Partner | New L1 recon | Needs to reach | Extra delta HERO adds |
|---|--:|--:|--:|
| Target | 0 | +10 | **+10** |
| Walmart | +20 | +30 | **+10** |

Final partner totals are still **+10 / +30 (BU-SKU +40).**

**Note — Takeaway**

Later L1 reconciliation does **not** stack on top of your target. HERO **re-nets** the rows so the active BU-SKU target still wins at the aggregate level. This is why older Level 1 workbooks are stale once Level 2.5 review has started.

---

## Example 5 — You change your own Level 2.5 value later

Your original adjustment was **+40** (+10 / +30). Later you decide the week should be **+60** instead.

| Partner | Baseline | Share | New +60, split by share | Final |
|---|--:|--:|--:|--:|
| Target | 100 | 25% | **+15** | 115 |
| Walmart | 300 | 75% | **+45** | 345 |
| **BU-SKU** | **400** | | **+60** | **460** |

**Note — Takeaway**

A newer Level 2.5 value **replaces** the earlier one for that week — HERO recomputes the partner split from the new target.

---

## Example 6 — The total looks fine, but the split moved a lot

Start: baseline 150 / 250 (37.5% / 62.5%); your adjustment **+40** → +15 / +25. Later the total baseline is still **400**, but it swings to 260 / 140.

| | Baseline | Share | Your +40, split by share |
|---|--:|--:|--:|
| **Before** Target | 150 | 37.5% | +15 |
| **Before** Walmart | 250 | 62.5% | +25 |
| **After** Target | 260 | 65% | **+26** |
| **After** Walmart | 140 | 35% | **+14** |

**Note — Takeaway**

Your +40 and the BU-SKU total look unchanged, but the per-partner allocation swung sharply (15/25 → 26/14). The headline can look fine while the distribution underneath is now very different — exactly the case to re-review.

---

## When to re-review a BU-SKU week

**Tip — Re-open a BU-SKU week after any of these happen later:**

- the baseline total moves materially,
- the baseline **share** across partners moves materially,
- overlapping Level 1 enrichments change,
- overlapping Level 1 reconciliation changes,
- another Level 2.5 adjustment is made.

The question to ask: *"My BU-SKU adjustment is still in place, but the forecast underneath moved — do I still want this same adjustment?"*

**Note — Review is manual**

HERO does not automatically flag these conditions — re-review is a manual step.

## Related pages

- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Calculation reference](calculation-reference.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/help/validation-error-catalogue.md -->

# Validation & error catalogue

## Who should read this page

Anyone whose upload was rejected, and anyone supporting users in office hours.

## Purpose

List the validation messages HERO can return and how to fix each one.

**Note — How rejection works**

When a workbook fails validation, HERO returns an **annotated workbook** instead of partially loading bad data. The validation tabs show the Excel row, the item keys, and the exact messages that fired. Fix the rows and upload again.

## Error catalogue

| Message (what fired) | Cause | Fix |
|---|---|---|
| *Upload rejected due to validation errors. Re-downloading the annotated file.* | One or more rows failed on the enrichments or reconciliation tab. | Open the returned workbook, read the validation-error tab, correct the rows, upload again. |
| *New enrichments cannot use past dates.* | A new enrichment uses a start/end date in the past. | Use a date that is today or later (`YYYY-MM-DD`), or convert the row into an update to an existing enrichment. |
| *Start Date must be on or before End Date.* | The date range is inverted or out of range. | Fix the dates; valid `YYYY-MM-DD` values on or after 2020-01-01. |
| *ALL_FORECAST_PARTNERS is only allowed for MARKETING and DEMAND_PLANNING rows.* | The all-partners sentinel used on another enrichment type. | Pick a normal Forecast Partner, or switch to MARKETING / DEMAND_PLANNING if that is the real use case. |
| *Exactly one of Expected Shipment Lift percent or units must be populated.* | The row used both lift fields or neither. | Enter only one lift mode per row. |
| *Mechanism / Shortage SKU / SPU SKU only allowed for their type.* | A conditional field used on the wrong enrichment type. | Clear the field or change the enrichment type. |
| *Only one of adjusted_planning_sku or channel_shift_proportion per row.* | A reconciliation row attempted both a version change and a channel shift. | Split into separate rows / uploads; one structured control per row. |
| *Workbook was downloaded for BU-SKU reconciliation; use the BU-SKU sheet.* | Workbook mode and upload sheet do not match. | Use the sheet that matches the workbook mode, or re-download the correct workbook. |
| *Row is outside the downloaded template scope.* | The row does not match the BU / Forecast Partner / Brand / mode the workbook was downloaded for. | Download a workbook for the right scope and apply the change there. |
| *BU-SKU weekly values must be numeric signed adjustment totals.* | A BU-SKU upload had a non-numeric weekly value. | Enter a numeric value, or leave the cell blank to keep the current rendered total. |

## New checks — 20 July 2026 release

The 20 July 2026 release added safer upload handling. Two new classes of template problems are now **caught and rejected with an explanation** instead of silently dropping data:

| Check | Cause | Fix |
|---|---|---|
| **Blanked header detected** | A header cell was deleted or overwritten, so HERO can no longer map the columns. | Re-download a fresh template and copy your entries across; never edit header rows. |
| **Mid-sheet blank row detected** | An empty row sits between data rows; previously the data below it could be silently dropped. | Remove the blank row(s) so data is contiguous, then upload again. |

**Note — Duplicate uploads: warning + intentional override**

Repeated uploads of the same template used to be silently blocked. As of the 20 July 2026 release, HERO **warns** you that the upload appears to be a duplicate and lets you **intentionally override** where appropriate. Only override when you are sure the repeat upload is deliberate — best practice remains to download a fresh template before every working session.

**Warning — Gaps & Open Questions**

- Exact on-screen message text for the blanked-header, mid-sheet-blank-row, and duplicate-upload warnings is not yet documented — confirm wording with the build team after production validation.

## Related pages

- [End-to-end workflow](../workflows/end-to-end-workflow.md)
- [Field-by-field reference](../workflows/field-by-field-reference.md)

---

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
Not with a single row. To re-phase demand, author a **positive + negative pair**: a positive `DEMAND_PHASE_SHIFT` row where the demand should land, and a negative row where it is taken from. As of the **16 July 2026 decision (ratified)**, this pair — not `SET` — is the recommended way to re-phase demand; reserve `SET` for true set builds. Use it for deals, pull-forwards and timing changes that do **not** come from problems in history; if the phasing issue stems from baseline/history defects or one-offs not adjusted in time, correct it via **reconciliation** (base trend adjustment) instead.

**Does SUPPLY_SHORTAGE_COMP automatically move volume between SKUs?**
No — it tracks the relationship, but you still capture the compensating demand correctly. Tracking-only refers to the forward forecast: nothing moves between SKUs there. The relationship it records is used at **history cleansing**, where it raises the adjusted demand of the item that was unavailable and reduces the same quantity from the substitute. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works).

**Can I change actualized weeks?**
Treat shaded / actualized weeks as frozen forecast history unless your operating model explicitly routes an exception through a separate process.

**In the Level 2.5 template, which columns do Demand Planners use for their adjustments?**
The **Baseline Trend Adjustments** columns — the **orange** ones. That is the editable weekly area.

**Then why does my adjustment show under "Marketing and Demand Planning" after I upload?**
Because HERO **classifies** your entry on upload based on **who entered it and when**. You always type into *Baseline Trend Adjustments*; the system then files Demand Planning / Marketing reconciliation entries under the *Marketing and Demand Planning* columns. Both are correct — input vs. how it's classified afterward.

**How do I cancel or delete an enrichment I captured?**
**Never delete the row.** As of the **20 July 2026 release**, set the row's **Status** to `DECLINED` — the row is preserved in the template and audit trail for visibility, but excluded from calculated downstream outputs. Zeroing the quantity still removes the effect, but `DECLINED` is now the recommended method.

**If I set the Status to "Declined", does that cancel the enrichment?**
**Yes — as of the 20 July 2026 release.** A `DECLINED` enrichment is preserved for visibility in the template and audit trail, but **excluded from calculated downstream outputs**. Setting Status to `DECLINED` is now the best way to "zero out" a previous enrichment. (Before this release, Status was log-only and zeroing the quantity was the only method.)

**Can I use formulas (e.g. VLOOKUP) or copy data from other files into the template?**
Yes — the templates are normal Excel files, so use whatever helps while you prepare. Just, **before uploading**: replace formulas with their values (paste as values), don't overwrite rows, avoid blank rows, and add any new/copied rows below the last row with data. As of the **20 July 2026 release**, upload validation catches blanked headers and mid-sheet blank rows and rejects the upload instead of silently dropping data — see [Validation & error catalogue](validation-error-catalogue.md).

**What happens if I upload the same template twice?**
As of the **20 July 2026 release**, HERO warns you that the upload looks like a duplicate and lets you **intentionally override** where appropriate, instead of silently blocking the repeat upload. Best practice is unchanged: **download a fresh template before every working session** and avoid stale saved templates. If you see any template/dashboard mismatch, report it immediately.

**Does a DP/Marketing adjustment change my sales forecast (UA1)?**
It depends on **which template you used**, not on your role. A Level 1 `MARKETING` or `DEMAND_PLANNING` enrichment captured in the enrichment capture template reaches the consensus only and never touches UA1. An adjustment made in the **forecast reconciliation template** does reach UA1, whoever makes it — including a Demand Planner or a Marketing user. Either way, HERO never overwrites UA1 inside the 0–4-month frozen window. (Ratified by Rene Bartoli, 6 August 2026. This replaces the earlier target-design / pilot-interim answer, which described the same behaviour as a temporary limitation waiting on a user-role layer.)

**I changed UA1 directly in Logility. Will HERO pick it up?**
No, and no amount of downloading or uploading will bring it in. HERO does not read UA1 in any window. The only array HERO reads from Logility is the Resultant. If the change needs to exist in HERO, someone has to make the equivalent change there.

**Does a fresh template download pull the latest UA1 from Logility?**
No. Every array in your template except the Resultant is served from HERO's own database. A fresh download gets you the latest Resultant and the latest HERO state, and nothing else from Logility.

**I removed my adjustment, so why is there still a value in Logility?**
Removing an adjustment zeroes the **delta** that adjustment represented, not the array. And the removal only reaches UA1 while the affected weeks are still **outside** the frozen window. Once those weeks are inside it, HERO does not touch UA1 at all, so the Logility number stays where it was. That is expected behaviour, not a failed upload.

**Logility shows zero, so my inputs must be clean. Right?**
No. Logility applies a zero floor at Level 1, so no Level 1 combination is ever published negative. Because the floor sits on the total, a negative hidden under positive components never surfaces there. Check the total preliminary forecast in HERO instead — a clean published number is not evidence that the components behind it are clean.

**My template is a few weeks old. Can I keep using it?**
Download a fresh one. A template carries the scope you selected **at download time**, and an upload is agnostic to what the dropdowns say now. HERO validates the upload against the latest backend state, so a stale template, or one downloaded at an over-broad scope such as ALL BRANDS, can quietly replace someone else's work in the overlapping scope.

**I made an urgent change and Logility doesn't show it yet — is HERO broken?**
No. HERO exports to Logility only once a week (Friday), by design — see [Timing & system sync](../workflows/timing-system-sync.md). If a change genuinely cannot wait, there are three governed paths, depending on what it is:

1. **Commercial enrichments** (promos, sets, samples, pre-orders, TMOs) **always** go through HERO — even inside the months 0–4 frozen window. Never enter these directly in Logility.
2. **Time-sensitive enrichment changes** (e.g. a DI-to-DOM flip): capture it in HERO and flag it as time-sensitive. A weekly report surfaces it to Demand Planning, who executes it in Logility within the agreed weekly window.
3. **Non-forecast-related edits only** (allocation support, ship-match alignment, holding the month, operational visibility): made directly in Logility on UA1, only within months 0–4, by whoever performs this work today. These never flow into consensus. There is no dedicated NFR (Non-Forecast-Related) functionality in HERO v1.0 — this is a deliberate, phased choice.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md)
- [Validation & error catalogue](validation-error-catalogue.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/help/glossary.md -->

# Glossary

## Who should read this page

All users. Every acronym used in HERO, expanded.

## Purpose

Single reference for HERO terms and acronyms.

| Term | Definition |
|---|---|
| **HERO** | Hasbro Enrichment & Reconciliation Optimizer — the business-user capture layer between Logility baselines and published forecast changes. |
| **ECT** | Enrichment Capture Template — the workbook path for event-driven enrichments. |
| **FRT** | Forecast Reconciliation Template — the workbook path for adjusting final week-level numbers. |
| **Business Unit (BU)** | The geography / organizational slice used throughout HERO. |
| **Forecast Partner** | The customer / retailer Hasbro forecasts shipments for. |
| **Planning SKU** | The planning item code HERO uses as the item identifier. |
| **Shipment Channel** | The shipment route — `DOM` (domestic) or `DI` (direct import). |
| **KAM** | Key Account Manager (Sales). |
| **GPL** | Global Product Lead (a commercial / marketing role). |
| **Level 1 (L1)** | Forecast-partner / customer-level reconciliation. |
| **Level 2.5 (L2.5)** | BU-SKU reconciliation mode used when all forecast partners are selected. |
| **SKU hierarchy levels** | Nodes in the item hierarchy: L5 Brand/BU · L4 Global SKU/BU · L3 Parent SKU/BU/Channel · L2 Planning SKU/Customer · L1 Planning SKU/Customer/Channel. "Level 3" is a hierarchy node (e.g. Parent SKU / BU / Channel), **not** a review stage; the later-stage review stage is Level 2.5 / BU-SKU. |
| **Base Trend Adjustment** | A direct week-level delta against the displayed baseline forecast. Persists across cycles until manually reversed — it is not a single-cycle entry. At Level 2.5 it disaggregates across **all** forecast partners by baseline proportion; it cannot be targeted at one account. |
| **Cleansing** | Correction of the **Adjusted Demand array** so the statistical baseline learns real demand rather than what shipped. It runs in the opposite direction to the enrichment — when a period closes, cleansed history is actual shipments minus the `SET` — and never touches raw Actuals. See [How history cleansing works](../workflows/forecast-range-calculation.md#how-history-cleansing-works). |
| **Frozen window** | The rolling lead-time horizon — months 0–4 counted from the current date, every cycle, not a one-off period after go-live — inside which HERO withholds UA1 authoring and the published value carries the live Logility UA1 / baseline instead. HERO authors UA1 in horizon months 5–21. |
| **Version Change** | A net-zero move of demand from one planning SKU to another over selected weeks. |
| **Channel Shift** | A move of some or all demand between `DOM` and `DI` over selected weeks. |
| **TMO** | Trade / pallet adjustment that travels through the UA5 / TMO path. Sourced from FAST. |
| **FAST** | The upstream system that is the source of truth for TMO; the ECT is seeded from it. |
| **SPU** | Special Planning Unit — optional tracking metadata on TMO rows. |
| **Phase-out** (`PHASE_OUT` in the tool) | An enrichment type captured in the enrichment capture template, used when an item should no longer behave like a normal carry-forward baseline (maps the depletion of available inventory). It is one of the UA1-mapped components (see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md) for the full UA1 composition) and also flows to consensus by sign — positive values to ADS2, negative values to PROMO_LIFT. **Phase-out is the canonical name** (confirmed by Rene Bartoli, 12 July 2026); `PHASE_OUT` is that same name as it appears in the tool/enrichment-type field. `MDP_ENRICHMENT` is a legacy synonym found in older architecture material (Transmission Design Topics V1) and should not be used as current terminology. |
| **Forecasting range** | The start / end dates over which a SKU is forecast for a partner; setting an end date stops future forecasting for that SKU/customer. |
| **Actualized period** | The historical portion of the year where the workbook shows exact shipment actuals when they exist. |
| **RESULTANT_FORECAST** | The baseline consensus forecast before HERO adjustments. |
| **ADS2** | Positive HERO adjustments other than TMO in the consensus path. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT, calculated by Logility. HERO never reads it and never writes it. |
| **Zero floor** | Logility's rule that no Level 1 combination is published negative. It is applied on the Logility side, on the total, so a negative sitting under positive components never surfaces downstream. Inside HERO only UA1 restricts negatives. |
| **One-way flow** | HERO reads only `RESULTANT_FORECAST` from Logility. Every other array travels HERO to Logility only, which is why a change made directly in Logility never reaches HERO. |
| **PROMO_LIFT** | Negative HERO adjustments in the consensus path. |
| **UA1–UA8** | Logility sales-forecast arrays — see [Logility array & mart mapping](../reference/logility-array-mart-mapping.md). |
| **P2M** | The source used to derive on-shelf dates / quantities that seed the forecasting range. |

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/reference/logility-array-mart-mapping.md -->

# Logility array & mart mapping

## Who should read this page

Demand Planning, Supply-Chain COE, and anyone tracing a HERO change through to Logility.

## Purpose

Map HERO outputs to the Logility sales-forecast arrays and consensus path.

## Which direction each array travels

HERO **reads** exactly one array from Logility: `RESULTANT_FORECAST`. Everything else on this page travels one way, **HERO to Logility**. HERO never reads UA1–UA6, ADS2, PROMO_LIFT or ADS3, so a change made directly in Logility on any of them is invisible to HERO. See [Direction of travel](batch-orchestration-updates.md) for the full mechanics.

| | Horizon HERO manages |
|---|---|
| UA1 | months 5–21 (suppressed inside the 0–4 frozen window) |
| UA2–UA6, ADS2, PROMO_LIFT | months 0–21 |
| RESULTANT_FORECAST | not written by HERO; changed in Logility by the baseline owner |
| ADS3 | not written by HERO; calculated by Logility from its components |

## Sales forecast arrays

| Array | Holds | Notes |
|---|---|---|
| **UA1** | Adjusted statistical baseline, and also the Sales (Fill) Forecast | Carries the baseline, the Level 1 base-trend adjustment, the Level 2.5 base-trend adjustment (after fan-out), version adjustments, channel shift, and the UA1-mapped enrichment types `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. Level 1 `MARKETING` and `DEMAND_PLANNING` enrichments from the enrichment capture template do **not** land here; adjustments from the forecast reconciliation template **do**, whoever makes them (see [what routes an entry](batch-orchestration-updates.md)). Authored by HERO in horizon months 5–21; see the [frozen window](../help/glossary.md). |
| **UA2** | Promotional activity | Promo-type sales adjustments. |
| **UA3** | Sets / initial stocking | Set-type sales adjustments. |
| **UA4** | Samples | Sample-type sales adjustments. |
| **UA5** | TMO / pallets | TMO rows. TMO passes through exactly as stored and never sums into ADS3 the way the other arrays do — it stays an independent adjustment, as it is treated in Logility today. A TMO change made in HERO still updates UA5 through the field-forecast export. |
| **UA6** | Pre-orders | Pre-order rows. |
| **UA7** | Previous-cycle sales forecast snapshot | Cycle comparison context. |
| **UA8** | Total sales forecast | Sum of UA1 through UA6. |

## Consensus path

| Element | Definition |
|---|---|
| **RESULTANT_FORECAST** | Baseline consensus forecast before HERO changes. |
| **ADS2** | Positive HERO adjustments except TMO → mapped to enrichment quantity. |
| **PROMO_LIFT** | Negative HERO adjustments → mapped into the promoted resultant line. |
| **ADS3** | RESULTANT_FORECAST + ADS2 + PROMO_LIFT. |
| **TMO** | Consensus TMO bucket → mapped to TMO quantity. |
| **consensus_forecast_quantity** | Final consensus forecast (Logility mart column) — consensus total after HERO adjustments. |

**Warning — The zero floor is applied on the Logility side**

Logility prevents any Level 1 combination from being **published** negative, applying the floor on both sides (RESULTANT_FORECAST + ADS2 + PROMO_LIFT, and the UA arrays). Inside HERO the only negative restriction is on UA1; every other array carries a negative straight out. Because the floor sits on the total, a negative hidden under positive components never surfaces here — which is why you review the total preliminary forecast in HERO rather than trusting a clean-looking published number.

## Related pages

- [Calculation reference](../examples/calculation-reference.md)
- [Glossary](../help/glossary.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/reference/batch-orchestration-updates.md -->

# Batch orchestration & updates

## Who should read this page

Anyone tracing how HERO (Hasbro Enrichment & Reconciliation Optimizer) processes changes and publishes to Logility. For the user-facing *"when does my change take effect?"* view, see [Timing & system sync](../workflows/timing-system-sync.md).

## Purpose

Explain the batch jobs behind HERO, the export to Logility, and the contingency path — the system mechanics beneath the timing rules.

**Note — When changes take effect — in brief**

A change is captured in HERO authoring state immediately. It reaches Level 1 and the dashboard after the next post-processing / fan-out run, and it reaches Logility only through the weekly Friday export pipeline. The fan-out runs **multiple times per UK workday** (Mon–Thu at 08:00 / 10:00 / 12:00 / 14:00 / 16:00 / 18:00 and Fri at 08:00 / 10:00 / 12:00 `Europe/London`, plus a Mon–Thu late-night catch-up at 23:00 `America/New_York`). The full schedule is in [Timing & system sync](../workflows/timing-system-sync.md).

## The batch jobs (what each one does)

- **Post-processing / fan-out** — takes Level 2.5 changes authored in HERO, fans them out to the Level 1 partner rows, and refreshes the dashboard-facing Level 1 view. As of the **20 July 2026 release**, post-processing was improved for reliability as usage grows, with better **business-unit scoping** and more **runtime visibility** into the runs.
- **Weekly Logility export** — runs as the Friday noon Eastern export pipeline. It materializes the Logility pickup tables and, if the contingency path is used, the 8-file wide CSV set.

**Warning — Scheduling is by day-of-week only**

HERO can only run a job "at this time on this day of the week." It does **not** read the 53-week fiscal planning calendar, so batch timing is expressed as weekday schedules, not planning-cycle dates.

## Direction of travel

The flow is one-way, with exactly one exception.

- Everything HERO manages travels **HERO to Logility**. Only the **Resultant** travels **Logility to HERO**.
- HERO **never reads** UA1, UA2–UA6, ADS2, PROMO_LIFT or ADS3. A change made directly in Logility is therefore invisible to HERO: no download and no upload will bring it in, and it exists in HERO only if someone deliberately makes the equivalent change there.
- The Resultant is read-only to HERO. It can only be changed in Logility, by the baseline owner, which protects the statistical proposal from being overwritten by an export.
- Every array except the Resultant is served to the template from **HERO's own database**, not from a live Logility read. A fresh template download brings in the latest Resultant and the latest HERO state, and nothing else from Logility.
- End-to-end latency on that one inbound path (Logility to EDW to Databricks) exceeds 24 hours, so same-day propagation of a baseline change is not a reasonable expectation.
- Divergence between the two systems is **silent**. Nothing errors, nothing is rejected, and nobody is notified when HERO and Logility stop agreeing. HERO has no view that compares itself against Logility, so the gap closes only by correcting the components in the template.

**Warning — ADS3 is the one array that can be forced directly**

HERO neither reads nor writes ADS3 — Logility calculates it as RESULTANT_FORECAST + ADS2 + PROMO_LIFT. Forcing ADS3 directly in Logility therefore cannot desynchronise HERO. It is the exception path for cases that must bypass the forecast entirely. The normal route is still through its components in HERO.

## Export to Logility

The export is changed-row-only, not full-table. HERO emits rows only for changed weekly keys, but each emitted row is fully populated. Unchanged rows are omitted; emitted rows are hydrated according to the outbound rules rather than left blank or sparse.

The full source → array mapping (UA1–UA6, ADS2, and PROMO_LIFT, including how TMO maps to UA5) lives in **[Logility array & mart mapping](logility-array-mart-mapping.md)**. The export rules specific to this layer are:

- **What routes an entry is the template, not the author's role.** Level 1 enrichments of type `MARKETING` and `DEMAND_PLANNING`, captured in the enrichment capture template, do not flow to UA1: they influence the consensus path only, positive values contributing to ADS2 and negative values to PROMO_LIFT. Adjustments made in the **forecast reconciliation template** do flow to UA1, whoever makes them — a Level 2.5 base-trend adjustment entered by Demand Planning or Marketing lands in UA1 exactly as one entered by a Brand Captain or a commercial lead.

    **Note — This replaces the earlier interim framing**

    Earlier versions of this page described the same behaviour as a temporary limitation, with a role-based exclusion waiting on a user-role validation layer. Routing by template is the ratified design, not an interim state. (Ratified by Rene Bartoli, 6 August 2026.)

- **UA1 composition.** UA1 is the adjusted statistical baseline and also the Sales (Fill) Forecast. It carries the baseline, the Level 1 base-trend adjustment, the Level 2.5 base-trend adjustment (after fan-out), version adjustments, channel shift, and the UA1-mapped enrichment types `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. The shorter formula `BASELINE + BASE_TREND + CHANNEL_SHIFT + PHASE_OUT` used in earlier material was the same fact at a lower level of detail.
- **UA1 frozen horizon:** UA1 is authored by HERO in horizon months **5–21** (rolling, counted from the current date, every cycle — not a one-off period after go-live); in months **0–4** the published value carries the current live Logility UA1 / baseline rather than a HERO-authored overwrite. UA2–UA6, ADS2, and PROMO_LIFT are HERO-managed across months **0–21**.
- **What "changed" means for the export.** The export answers only *"did this value change in HERO since the last HERO export?"* It does not compare HERO against Logility. A direct Logility edit is neither detected nor deliberately overwritten, unless HERO also changed that same intersection during the week, in which case HERO overwrites the arrays it authors.
- **Channel moves generate two updates.** Export keys include shipment channel, so DOM and DI are separate export combinations. Moving an enrichment from one channel to another updates both: the original aggregation is reduced and the new one is created. Multiple enrichment rows sharing SKU, customer, channel and week aggregate together.
- **The zero floor lives in Logility.** Logility prevents any Level 1 combination from being published negative, applying the floor on both sides (RESULTANT_FORECAST + ADS2 + PROMO_LIFT, and the UA arrays). Inside HERO the only negative restriction is on UA1; every other array carries a negative straight out. Because the floor sits on the **total**, a negative hidden under positive components never surfaces downstream, so a published zero is not evidence that the inputs are clean.
- **Output format:** emitted outbound values are fully populated, exported as whole integers, and rounded to the nearest whole unit with halves rounded away from zero.
- **Delta-table granularity:** the processing tables are weekly-grain, append-by-run history tables. Within a run, HERO emits only the final effective outbound row for each changed weekly key; later runs append new rows for the same weekly key.

## Orchestration chain (weekly)

**HERO-owned weekly export step**

- **Job 1 (Hasbro / Databricks)** — Fridays at 12:00pm Eastern; runs the final post-processing step and then materializes the HERO field-forecast and consensus export artifacts.

**Downstream orchestration (external, not HERO jobs)**

After the HERO export completes, downstream Hasbro / Logility transport and extraction steps pick up those artifacts for processing on the Logility side. These are external orchestration steps, not HERO-internal jobs, and any specific timings or run controls for them are owned in the downstream orchestration spec rather than the HERO repo.

**Note — Manual runs & transport**

Controlled manual runs via Run Options are available for testing, pilot validation, and fallback operation. The recurring HERO publish cadence itself is the scheduled Friday export pipeline; any downstream pickup from Databricks into Logility should be understood as downstream orchestration rather than a separate HERO authoring rule.

## Contingency CSV (manual fallback)

If direct integration is not ready, HERO can produce a contingency CSV set for manual loading into Logility: **8 files** (UA1–UA6, Positive Enrichments → ADS2, and Negative Enrichments → PROMO_LIFT). Each file is a wide Level 1 file with 3 key columns and ordinal week columns 1–78. A row appears only if that file's measure changed for that Level 1 key, but every included row is fully populated. Clear rules apply: UA1 clears back to the live Logility UA1 / baseline; UA2–UA6, ADS2, and PROMO_LIFT clear to 0.

## How this connects to the end-to-end process

Baseline generated upstream (Logility / Daybreak) → enrichment capture and reconciliation in HERO (with Level 2.5 changes fanned out to Level 1) → dashboard shows the number **before and after** adjustment → executive sign-off → the weekly Friday export publishes the deltas into the Logility arrays / export surfaces.

**Note — Governance after sign-off is audit-based, not lock-based**

No technical lock prevents changes after executive sign-off. The control is the cycle-change filter — every change is visible against the last ADS3 summarization — with escalation to leadership for anything that looks like re-inflating the forecast after sign-off. This is a deliberate design choice made after user pushback during discovery.

## Related pages

- [Timing & system sync](../workflows/timing-system-sync.md) — the when-does-my-change-take-effect view.
- [Logility array & mart mapping](logility-array-mart-mapping.md) — the full array mapping.
- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)

**Warning — Gaps & Open Questions**

- **UA1 upper horizon — pending build confirmation.** Months 5–21 is the design of record (Rene Bartoli, 6 August 2026). On 30 July 2026 the built UA1 export window was described as reaching month 12, and confirmation that the build now matches the design is outstanding.
- **Frozen-window calculation when a cycle opens in the prior month.** A cycle formally opens the month before its name (the July 2026 cycle opened on 22 June 2026). Whether HERO's rolling window can therefore reach into the last month of the frozen period is not confirmed.
- **UA2–UA6 direct-edit lockdown.** The Logility permission that allows direct edits on UA2–UA6 and PROMO_LIFT can be removed so that every change flows through HERO. Whether it has been applied, or remains a process rule only, is not confirmed. UA1 stays directly editable inside months 0–4 by design.

---

<!-- docs/reference/deferred-in-v0.md -->

# Deferred in v0

## Who should read this page

Program leadership, facilitators, and SMEs tracking what is intentionally out of scope for the first release.

## Purpose

Record what is deliberately out of scope for the first release (v0) of the HERO tool, so users know where capability is intentionally limited.

## Deliberately deferred

- A dedicated **Non-Forecast-Related (NFR)** capability in HERO — this is a deliberate, phased choice, not an oversight. Non-forecast-related edits (allocation support, ship-match alignment, holding the month, operational visibility) are made directly in Logility on UA1, months 0–4 only, by whoever performs this work today, and never flow into consensus. Any change to an enrichment is always made in HERO, never in Logility. See the [three governed paths for urgent changes](../workflows/timing-system-sync.md#urgent-changes-the-three-governed-paths).
- Final **cluster-specific permission matrix** by Business Unit, Forecast Partner, and Brand. *Partially superseded: the 20 July 2026 release cleaned up access controls so users only see the Business Units they are authorised for — confirm whether the full matrix (Forecast Partner / Brand level) remains deferred.*
- Any final changes to **enrichment-type taxonomy** before pencils-down.
- Automated **review signals** in the UI (re-review is manual — see [BU-SKU worked examples](../examples/bu-sku-worked-examples.md)).

**Note — AIM and POS**

AIM = the Shipment Revenue view; POS = Point of Sale (sell-through) used in the Glidepath view. See [Reference views & dashboards](../tools/reference-views-dashboards.md).

## Related pages

- [Reference views & dashboards](../tools/reference-views-dashboards.md)
- [Roles & what each role does in HERO](../getting-started/roles-permissions.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/reference/documentation-governance.md -->

# Documentation governance

## Who should read this page

Anyone maintaining or contributing to this manual.

## Purpose

State how this documentation is sourced, versioned, and kept honest about uncertainty.

## Source of truth

This manual is consolidated from controlled source documents — primarily the **HERO User Manual (v0)** and the **BU-SKU Reconciliation Behavior Explainer**, with practical examples drawn from the **Module 2** enablement material. Do not add HERO functionality that is not supported by those sources.

## Handling uncertainty

**Warning — Never hide gaps**

Where a fact, owner, threshold, date, or policy is not fully defined, it is flagged inline as `[DRAFT — confirm with SME]` and surfaced in the page's **Gaps & Open Questions** block. These are review items, not settled decisions.

## Maintenance conventions

- **One page, one topic.** Keep pages scannable; link rather than repeat.
- **Acronyms expand on first use per page**, even if expanded elsewhere.
- **Admonitions** carry notes, tips, warnings, examples, and open questions — keep the same set across pages.
- When the source documents change, update the affected page and clear or revise its Gaps block.

## Editing and contributions

- Content edits should be grounded in the source documents — not authored freehand.
- Structural / build fixes (links, formatting, navigation) are safe to make directly.
- Material that looks missing or contradictory belongs in the page's Gaps block for SME review, not invented.

The **repository is the source of truth** for manual content. Changes arrive as instructions rather than as inbound packaged archives. The process owner's local folder is a **one-way, read-only copy** of the repository — delivered as a generated snapshot (a zip drop produced on each merge to `main`), copied in by hand, never edited in place and never shipped back as a master. This retires the earlier two-way packaged-archive round-trip, which was itself a place where the repository and the local copy could quietly drift apart.

## Revision log

**2026-08-07** — Confirmed by Rene Bartoli (process owner) on 7 August 2026:

1. **NPI channel fill corrected — supersedes the NPI extension in item 1 of the 2026-07-16 entry below.** The clause claiming the `+SET/−SET` simplification covered the NPI set/baseline case is removed; it over-extended the 16 July simplification to a case it does not cover. When the Daybreak New Product Introduction launch baseline already embeds the channel fill, the case uses a **negative base trend adjustment in F1** plus a **positive `SET` of equal magnitude in F1**, not a `SET` pair. Sourced from `HERO_Canonical_Facts_OnePager_v5_2026-08-07` fact 45 and `HERO_Build_Learnings_KnowledgeBase_for_Brave_v11_2026-08-07` section 24. Updated `tools/enrichment-capture-template.md`.
2. **Authoring levels by role stated explicitly.** Key Account Managers author at Level 1; Brand Captains, Demand Planning and Marketing at Level 2.5; the Resultant is never modified in either case. Clarifies the phrase "Level 2-only overrides, Level 1 resultant untouched" — it means the Level 1 Resultant is not overwritten, not that Level 1 authoring stops. Updated `getting-started/roles-permissions.md`.
3. **New page: which items have a statistical baseline.** States the rule that a market agrees which segments are forecast statistically, and that segments outside it are captured in full as base trend at Level 1. Includes the United Kingdom and United States differences for Direct Import and FAN, and the United States FAN go-live hold. New `getting-started/statistical-baseline-scope.md`.
4. **The repository is now the source of truth for manual content.** The packaged-archive round-trip is retired; changes arrive as instructions and the process owner's local folder is a one-way, read-only copy delivered as a generated snapshot. Recorded under *Editing and contributions*.
5. **History cleansing documented.** New *How history cleansing works* section in `workflows/forecast-range-calculation.md`: cleansing corrects the Adjusted Demand array so the baseline learns real demand, and runs in the opposite direction to the enrichment — cleansed history is actual shipments minus the `SET`, while base trend adjustments are not cleansed. `SUPPLY_SHORTAGE_COMP` raises the unavailable item's adjusted demand and reduces the substitute's at cleansing. Reconciled the "tracking-only" wording in `tools/enrichment-capture-template.md`, `help/faq-common-gotchas.md` and `workflows/field-by-field-reference.md` so it refers to the forward forecast while the recorded relationship drives cleansing (the existing rule is unchanged, only completed). New `Cleansing` glossary entry in `help/glossary.md`. The cleansing logic is published explicitly as a starting point expected to be refined as cycles accumulate. Sourced from `HERO_Canonical_Facts_OnePager` v6 facts 79–81 and `HERO_Build_Learnings_KnowledgeBase_for_Brave` v12 section 25.

**2026-08-06** — Aligned the manual with the HERO/Logility data flow ratified by Rene Bartoli (process owner) on 6 August 2026 during the Module 7 build, sourced from `HERO_Canonical_Facts_OnePager_v4_2026-08-06` and `HERO_Build_Learnings_KnowledgeBase_for_Brave_v10_2026-08-06`:

1. **Routing is by template, not by role — supersedes item 1 of the 2026-07-12 entry below.** The interim / target-design split is retired. Level 1 `MARKETING` and `DEMAND_PLANNING` enrichments captured in the enrichment capture template do not reach UA1; adjustments made in the forecast reconciliation template do, whoever makes them. Updated `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/faq-common-gotchas.md`.
2. **Direction of travel documented.** The flow is one-way apart from the Resultant: HERO reads only `RESULTANT_FORECAST` and never reads UA1–UA6, ADS2, PROMO_LIFT or ADS3, so a direct Logility edit is invisible to HERO. New section in `reference/batch-orchestration-updates.md`, summary table in `reference/logility-array-mart-mapping.md`, new glossary entry, four new FAQs.
3. **Horizons corrected.** UA1 is authored across months **5–21** (was 5–12). UA2–UA6, ADS2 and PROMO_LIFT are HERO-managed across months **0–21** (was 0–12). Updated `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/glossary.md`.
4. **UA1 composition stated in full.** Baseline, Level 1 and Level 2.5 base-trend adjustments, version adjustments, channel shift, plus `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT` and `SUPPLY_SHORTAGE_COMP`. The shorter four-term formula was the same fact at lower detail; the glossary now links to the composition instead of repeating a partial formula. Phase-out nomenclature from item 2 of the 2026-07-12 entry is unchanged.
5. **Zero floor located.** The floor lives in Logility and works at Level 1; inside HERO only UA1 restricts negatives. Added to `reference/batch-orchestration-updates.md`, `reference/logility-array-mart-mapping.md`, `help/glossary.md`, `help/faq-common-gotchas.md`.
6. **TMO clarified.** TMO passes through exactly as stored, lives in UA5, and never sums into ADS3 the way the other arrays do. A TMO change in HERO still updates UA5 through the field-forecast export. Updated `reference/logility-array-mart-mapping.md`.
7. **Export change detection, channel moves and template scope.** The export only answers whether a value changed in HERO since the last export; channel moves update both the DOM and DI combinations; templates are scope-locked at download time. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
8. **Scheduled jobs and dashboard cadence.** HERO does run scheduled jobs; the dashboard refresh cadence is 90 minutes for now, target one hour, and the "15 minutes" figure quoted in a training session referred to something else. New sections in `workflows/timing-system-sync.md`.
9. **Access model.** Platform-managed regional groups, no role granularity, exactly two levels (planner for Level 2.5, regular user for Level 1), and a ticket lead time to plan around. New section in `getting-started/roles-permissions.md`.

**2026-07-16** — *Backfilled on 7 August 2026 from `CLAUDE_CODE_PROMPT_8.md`. The changes below were written into the manual pages on 16 July 2026 — the ratified DEMAND_PHASE_SHIFT-vs-SET decision together with the 20 July 2026 HERO release — but were never recorded in this revision log; this entry restores the record. It documents edits already present in the pages and changes no content.* Sourced from `CLAUDE_CODE_PROMPT_8.md` and the `HERO_Manual_Site_for_code_2026-07-16_v6` site source:

1. **DEMAND_PHASE_SHIFT replaces SET for re-phasing demand — ratified 16 July 2026.** Re-phasing existing demand between weeks (pull-forwards, push-outs, deals) is captured with a `DEMAND_PHASE_SHIFT` **positive + negative pair**, not `SET`. `SET` is reserved for a true set build; a set build that also pulls existing demand forward pairs a positive `SET` with **negative `SET` rows** on the source weeks — the same enrichment type on both legs. A single `DEMAND_PHASE_SHIFT` row still moves nothing on its own. **Boundary rule:** timing changes that do **not** originate in history go through `DEMAND_PHASE_SHIFT`; phasing issues stemming from baseline/history defects or one-offs not adjusted in time go through **reconciliation** (base trend adjustment). **Disambiguation:** the automated offsetting zero-out belongs to **Channel Shift** (`DOM` ↔ `DI`, a reconciliation control), which creates its negative automatically; `DEMAND_PHASE_SHIFT` moves demand between weeks with both legs authored manually. Updated `tools/enrichment-capture-template.md` (types table, tip, boundary note, warning, and Gaps block replacing its success block) and `help/faq-common-gotchas.md`. *(The extension of this `+SET/−SET` simplification to the NPI set/baseline case — where the launch baseline already carries the fill — is superseded by item 1 of the 2026-08-07 entry above; that case uses a negative base trend adjustment plus a positive `SET`, not a `SET` pair.)*
2. **DECLINED now cancels an enrichment — behaviour flip.** Previously Status was a log-only field and the only way to remove an enrichment's effect was to zero the quantity. As of the **20 July 2026 release** a `DECLINED` row is preserved in the template and audit trail but **excluded from calculated downstream outputs**, and setting Status to `DECLINED` is the recommended way to cancel an enrichment (zeroing the quantity still works). Updated `tools/enrichment-capture-template.md` (Status note and *Cancelling or removing an enrichment*), `help/faq-common-gotchas.md` (two Q&As flipped, one now answering "Yes"), and `workflows/field-by-field-reference.md` (Status row).
3. **Upload validation catches blanked headers and mid-sheet blank rows.** As of the 20 July 2026 release these are rejected with an explanation instead of silently dropping the data below them. New "New checks — 20 July 2026 release" section in `help/validation-error-catalogue.md`; blank-row guidance updated in `tools/enrichment-capture-template.md` and `help/faq-common-gotchas.md`.
4. **Duplicate uploads warn instead of block.** Repeated uploads of the same template now raise a warning and allow an intentional override, where they were previously blocked silently. Updated `help/validation-error-catalogue.md` and `help/faq-common-gotchas.md`.
5. **Reconciliation template improvements.** Clearer labels and formatting, rounded display values, visible calculated forecast totals, clearer Level 1 vs Level 2.5 attribution, and removal of stale/invalid planning SKUs. New "What changed in the 20 July 2026 release" section in `tools/forecast-reconciliation-template.md`.
6. **Rounding note broadened to template display.** Reconciliation templates now show rounded display values for readability while the stored values remain unrounded; export rounding (nearest integer, halves away from zero) is unchanged. Updated `examples/calculation-reference.md`.
7. **Access controls by Business Unit.** Users see only the Business Units they are authorised for in the BU selection. Updated `getting-started/roles-permissions.md` and `workflows/field-by-field-reference.md`, with a "partially superseded" note on the permission-matrix bullet in `reference/deferred-in-v0.md`.
8. **Post-processing reliability, BU scoping and runtime visibility.** The post-processing / fan-out step was improved for reliability as usage grows, with better business-unit scoping and more runtime visibility into runs. Updated `reference/batch-orchestration-updates.md`.

**2026-07-12** — Aligned the manual with facts confirmed by Rene Bartoli (process owner) on 12 July 2026, sourced from `HERO_Build_Learnings_KnowledgeBase_for_Brave_v4_2026-07-12` (sections 13–16) and the corrected S&OP Data Architecture v2 / NFR Addendum v2:

1. **UA1 routing — interim vs target design.** *(Superseded by item 1 of the 2026-08-06 entry above — routing is by template, not by role.)* The claim "Marketing / Demand-Planning adjustments do not flow to UA1" is the *target* design. Reframed with a pilot-interim admonition: during the pilots, all Level 2.5 base-trend adjustments flow to UA1 regardless of author, because the user-role validation layer is not yet built. Updated `reference/batch-orchestration-updates.md` and `help/faq-common-gotchas.md`.
2. **Phase-out nomenclature.** Confirmed canonical name **Phase-out** (written as `PHASE_OUT` in the tool/enrichment-type field), the fourth component of the UA1 formula; `MDP_ENRICHMENT` documented as a legacy synonym only, never current terminology. Updated `help/glossary.md` and `reference/logility-array-mart-mapping.md`. *(The four-term formula here is expanded by item 4 of the 2026-08-06 entry above — same fact, fuller detail; the Phase-out nomenclature is unchanged.)*
3. **Frozen window wording.** Confirmed 4 months, rolling (months 0–4 from the current date, every cycle) — not a one-off post-go-live period, and not "0–90 days" (an erratum in the prior NFR Addendum). Added an explicit glossary entry.
4. **Urgent changes — three governed paths.** Documented the three paths for changes that can't wait for the weekly Friday export: commercial enrichments always through HERO; time-sensitive enrichment changes via HERO + weekly report; non-forecast-related edits directly on UA1 in Logility, months 0–4 only. Updated `help/faq-common-gotchas.md`, `workflows/timing-system-sync.md`, and `reference/deferred-in-v0.md`.
5. **NA-training clarifications.** Confirmed and documented: Level 2.5 adjustments persist as deltas until manually reversed; a Level 2.5 correction disaggregates across all customers by baseline proportion and cannot target one account; Version Change / Channel Shift pairs must be manually zeroed once the Forecasting Range is fixed; KAMs have no access to Level 2.5 templates; governance after sign-off is audit-based (cycle-change filter), not lock-based. Updated `roles/demand-planner.md`, `roles/sales.md`, `tools/forecast-reconciliation-template.md`, and `reference/batch-orchestration-updates.md`.

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/special-considerations/data-transmission-contingency.md -->

# Data transmission during contingency

## Who should read this page

Everyone involved in the weekly HERO → Logility hand-off during the UK pilot: Demand Planning (DP), the upload owners, and the commercial teams (Captains, Key Account Managers (KAMs), Marketing) whose changes must be in HERO before the weekly cut-off.

## Purpose

Explain the **temporary, semi-automated upload** used during the pilot while the fully automated HERO → Logility pipeline is being built (expected for the pilot plus roughly one additional cycle), including who owns each step and the Friday time windows.

## How it works

Each week HERO generates **up to 8 files (maximum)** — one per array (UA1–UA6 plus the positive / negative enrichment files). The files already have the exact structure Logility needs (SAC extractor for Run Options), so **no editing is required — just upload**.

## Where the files live

Files are posted to the **COE Workspace SharePoint** (the Teams channel set up for this), under **COE Support → UK Pilot Logility Upload Files**:

[UK Pilot Logility Upload Files (SharePoint)](https://hasbroinc.sharepoint.com/sites/COEWorkspace/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FCOEWorkspace%2FShared%20Documents%2FCOE%20Support%2FUK%20Pilot%20Logility%20Upload%20Files&p=true&ga=1)

## Weekly schedule (Fridays)

| Step | Owner | Eastern (ET) | Mexico (CDMX) | UK (BST) |
|---|---|---|---|---|
| 1. HERO export job runs (~2 h) | Jared (Hasbro / Databricks) | 10:00 AM | 8:00 AM | 3:00 PM |
| 2. Files pulled from Databricks → posted to SharePoint | Edgar | ~12:00 PM | ~10:00 AM | ~5:00 PM |
| 3. Upload files into Logility (Run Options) | Rose & Denise (UK), supervised by Elke (EU) | 12:00–4:00 PM | 10:00 AM–2:00 PM | 5:00–9:00 PM |
| 4. Hard cutoff — uploads done, Logility frozen for everyone | All markets | 4:00 PM | 2:00 PM | 9:00 PM |

*The job was moved from 12:00 PM to 10:00 AM ET to give the EU/UK team a more reasonable finish. Exact run length will be confirmed on the first execution.*

**Warning — Weekly pencils-down**

As a consequence of the above, the weekly cut-off for **Captains, KAMs, Demand Planners and Marketing** to make changes in HERO and upload them ends at **3:00 PM London** during the pilot (10:00 AM ET / 8:00 AM Mexico) — that is when the export job starts, so anything not in HERO by then will not be in that week's file. This time can be adjusted once the process is automated post-pilot, but for now it is critical the teams keep it in mind and that it is socialized with the commercial teams.

## File handling

Files live in a **monthly folder** (e.g. `2026.06`) with a **timestamped subfolder per run** — nothing is overwritten. Edgar downloads the whole subfolder and posts the files to the SharePoint location above.

## Nice-to-have vs. critical weeks

- **Weeks 1 & 2 — nice-to-have (not critical).** If an upload does not go through there is no operational impact (the dashboard still shows the data, and HERO protects the sales-forecast figures). The upload owners can submit the files at any time between one Friday and the next if something goes wrong.
- **Week 3 — critical.** This is the post executive sign-off upload with the final Demand Planning + Marketing adjustments used for the regional Demand Management Review (DMR). This one must go through.

## Coordination

- **No other Logility changes during the Friday upload window** — notifications are sent so all markets stay out of the system.
- A **walkthrough call** is held on the first upload, and test scenarios are prepared in the HERO test environment.
- Edgar aligns with Jared on the Logility volume to copy and places a copy of the test files on SharePoint so the access test can be run.

**Note — Temporary bridge**

This manual step is a temporary bridge. Once the automated pipeline is validated, the upload goes away.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)
- [Timing & system sync](../workflows/timing-system-sync.md)

**Success — No open questions identified**

No open questions were identified from the available source material.

---

<!-- docs/special-considerations/fcr-adjustment-rules.md -->

# Rules for FCR adjustment within cycle

## Who should read this page

Key Account Managers (KAMs), Brand Captains, and Demand Planning (DP) — anyone handling a forecast adjustment opportunity identified **inside the planning cycle (W-1 to W3)** during the UK pilot.

## Purpose

Give clear guidance on how to handle forecast adjustment opportunities found within the cycle, depending on whether the impact can be absorbed within the same customer, requires a direct customer-level change, or needs broader compensation across products, accounts, or forecasting partners. It also defines who owns each type of adjustment so impact stays visible across customer, product, and brand hierarchies. (FCR = Forecast Calculation Range.)

## Decision summary

| Scenario | Business situation | Primary owner | Expected Level 3 impact |
|---|---|---|---|
| **Case 1** | Volume reallocation within the same customer, from one reference to another | KAM | Level 3 stays stable |
| **Case 2** | Absolute increase or reduction at customer level, not compensated within the customer | KAM, aligned with Brand Captain | Level 3 changes; variation accepted |
| **Case 3A** | Customer-level impact compensated through another product across all accounts | Brand Captain | Level 3 protected via product-level compensation |
| **Case 3B** | Customer-level impact compensated through a specific account | Brand Captain + compensating KAM | Level 3 protected via account-level compensation |
| **Case 3C** | One customer will not take a SKU, but total SKU volume should be preserved and redistributed | Brand Captain + Demand Planner | Level 3 stays stable; Level 1 reallocated |

## Case 1 — Volume reallocation within the same customer

Applies when the opportunity is for a specific reference and customer, but the volume will be **compensated by another product within that same customer** (e.g. a different colorway, 5-digit code, or parent material).

**Use the Version Change functionality.** At Reconciliation Level 1, the KAM indicates which product should absorb the forecast and the period the adjustment applies to, and the system moves the volume. **Level 3 stays stable** even though volume moves between products / 5-digit codes within the customer.

## Case 2 — Absolute increase or reduction at customer level

Applies when the adjustment is an absolute increase or reduction to a customer's total volume that **will not be compensated within that customer**.

The KAM should **align with the Brand Captain first**, since it changes total customer volume. The Brand Captain decides whether it is significant enough to require compensation from other accounts, or is normal demand variation to be absorbed at customer level. If it is normal variation, the KAM enters the Reconciliation template and applies the increase / reduction to the relevant brand, product, or SKU. The impact is **transmitted automatically to Level 3** and accepted as part of the customer-level update.

## Case 3 — Customer-level adjustment requiring brand-level compensation

A variation of Case 2: the change is not compensated within the customer and, after validating with the Brand Captain, is significant enough to put the **brand budget / total brand forecast** at risk. The Brand Captain defines how compensation is managed:

### Option 3A — Compensate through another product across all accounts

The adjustment is made at **Level 2.5**: the Brand Captain applies it to the compensating product, and it is distributed across accounts using the current baseline as the allocation reference. Simplest broad-reallocation scenario.

### Option 3B — Compensate through a specific account

Coordinated directly with the KAM of the **compensating account**, who applies the adjustment through the Reconciliation template for that account. Ensures the compensation is explicitly agreed with the account owner.

### Option 3C — Compensate in the same SKU across the remaining accounts

The most complex case: the Brand Captain wants to **preserve the total SKU forecast at Level 3**, but one customer / forecasting partner will no longer take the reference, so the volume must be **redistributed across the remaining eligible customers**.

Because this changes the underlying **forecasting range**, it cannot be done through the Reconciliation template — it requires **Demand Planner** intervention. In Logility, the Demand Planner:

1. Adjusts the forecasting range to avoid duplicating effort in future cycles.
2. Tags the record with the indicator **(M)** so the Genpact team does not overwrite it later.
3. Sets the **Level 2** forecast for the relevant forecasting partner to **zero** for all applicable weeks.

The team then waits for the **end-of-day disaggregation batch**, which recalculates Level 3 → Level 2 → Level 1. Finding no Level 2 forecast for that partner, it sets the corresponding Level 1 to zero, so the volume redistributes only across the remaining customers.

**Note — When the change becomes visible**

After the disaggregation batch, the updated data is transmitted to the EDW tables at **12:30 PM Eastern Time**. The changes become visible in HERO the **following day**, once the EDW tables are updated and HERO refreshes its data.

Result: **Level 3 stays stable**; **Level 1 is redistributed** only across the correct customers. Use this only when the business decision is to preserve the total SKU forecast and redistribute, rather than reduce the SKU or compensate through another product.

## Guiding principle

Preserve the right level of accountability while keeping the process practical:

- **Customer-specific corrections** → KAM, through the Reconciliation template.
- **Brand-level decisions** affecting total volume or requiring cross-account compensation → validated and coordinated by the Brand Captain.
- **Preserving a total SKU forecast by redistributing across remaining customers** → Demand Planner, through the traditional Logility forecasting-range process so the disaggregation logic recalculates correctly.

## Persisting an approved decision into future cycles

When reconciliation approves a **standing** change — e.g. *"Tesco's baseline should permanently increase by 10%"* — how it is persisted so Sales sees it next cycle depends on **what the decision really means**:

### Case A — Raise the total forecast (Level 3 / BU total goes up)

If the intent is a genuine **increase in total demand** (not just a re-split), apply a **Base Trend Adjustment**, held for **~4 months on average**. The purpose is to give the statistical (moving-average) model enough time to **learn the product's new potential** in the market and at that customer. After ~4 months the model should pick up the trend naturally and the enrichment is **no longer needed**.

### Case B — Change the share / proportions (Level 3 total stays the same)

If the intent is that **Tesco should hold a larger share** of the SKU (without changing the BU total), it is a **disaggregation** change, handled by the Demand Planner — not by an enrichment:

1. The **KAM** (in markets without a Brand Captain) or the **Brand Captain** (in markets that have one) requests the change from the **Demand Planner**.
2. The Demand Planner validates the justification and determines the **new Level 2 disaggregation proportions**.
3. The Demand Planner communicates them to **Genpact**, stating **how long** the **fixed disaggregation** (fixed proportions) should apply.
4. Typically after **~6 months** the fixed proportions are no longer needed, because the new split has been in place long enough for the moving-average model to capture it.

**Warning — Fixed proportions have a hard horizon**

A fixed-proportion scheme **cannot be maintained beyond the last week of the last open forecasting period**. For example, if the current open forecast reaches 2027, fixed proportions can be reflected **at most through December 2027**; beyond that the **moving-average** model governs.

**Note — Which mechanism?**

Total up → **Base Trend Adjustment (~4 months)**. Share change only → **fixed Level 2 disaggregation via the Demand Planner + Genpact (~6 months, capped at the last open forecast period)**. Both are temporary bridges until the moving-average model learns the new pattern.

## Related pages

- [Forecast Calculation Range & Disaggregation](../workflows/forecast-range-calculation.md)
- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Forecast Reconciliation Template (FRT)](../tools/forecast-reconciliation-template.md)

**Success — No open questions identified**

No open questions were identified from the available source material.
