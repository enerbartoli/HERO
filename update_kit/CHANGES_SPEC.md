# HERO Manual Update Spec — 2026-08-28

**Source of truth:** `HERO_Canonical_Facts_OnePager_v15_2026-08-29.txt` in this kit. Ratified by Rene Bartoli. Where the manual and this file conflict, **this file wins**. The two Logility vendor transcriptions and the HERO product-team pack in this kit are the evidence behind it.

**Scope:** the manual is four Canonical Facts sections behind. This spec lands sections **17 to 21**, facts 94 to 130, in one pass. Fourteen changes.

**Read before starting:** `_KIT_README.md` in this kit, then `Repo_Docs_Review_2026-08-28.txt` for the reasoning behind changes 1 and 2.

---

## Change 1 — Fan-out timing: the figures on two pages are wrong [REQUIRED, DO THIS FIRST]

Two pages state a fan-out schedule that does not exist, and users act on it every cycle. This is the highest-priority change in the spec.

**What the manual says today (wrong, remove it):**

- `docs/workflows/timing-system-sync.md` (~lines 30-32): "Monday-Thursday (UK workday): 08:00, 10:00, 12:00, 14:00, 16:00 and 18:00 `Europe/London`", "Friday (UK morning): 08:00, 10:00 and 12:00 `Europe/London`", "Monday-Thursday late-night catch-up: 23:00 `America/New_York`".
- `docs/reference/batch-orchestration-updates.md` (~line 14): the same figures inside an admonition, plus "The fan-out runs **multiple times per UK workday**".

### What is actually true

In the words of the author of the product documentation:

> Your Level 2.5 change is saved immediately, but it does not fan out to forecast partners immediately. HERO post-processing must distribute the adjustment and rebuild the partner-level surfaces. **Scheduled processing is therefore the normal path for Level 2.5, not a fallback.**

**There are two different processes here. Do not merge them into one table.** The manual's previous version did exactly that and it produced wrong answers downstream.

**Process one, the fan-out**, which distributes a Level 2.5 adjustment down to the Level 1 partner rows. It runs Monday to Thursday, and **each market has its own job at its own times**:

| Market | Days | Fan-out runs |
|---|---|---|
| United Kingdom | Monday to Thursday | 08:00, 11:00 and 14:00 `Europe/London` |
| Hasbro U.S. | Monday to Thursday | 12:00, 15:00 and 18:00 `America/New_York` |

**Process two, the weekly export post-processing**, which produces the export to Logility. It runs **inside the export pipeline**, once a week, on a different day per market:

| Market | Day | Runs at |
|---|---|---|
| United Kingdom | Friday | 10:15 `America/New_York` |
| Hasbro U.S. | Saturday | 12:00 `America/New_York` |

**Level 1 writes remain immediate** and need no post-processing. That distinction is the point of the page: Level 1 lands on save, Level 2.5 lands on the next fan-out run for its market.

### Do

- Rewrite the schedule block in `docs/workflows/timing-system-sync.md` using the two-process model above, as **two separate tables under two separate headings**. Lead with "saved immediately, distributed on the next fan-out run for your market".
- **Do not promise minutes.** **Do not call the scheduled runs a safety net, a backstop or a fallback.** They are the normal path for Level 2.5.
- **Do not present a single combined timetable**, and **never write one market's times in a way that reads as applying to the other**. Add a line telling the reader to use the row for their own market.
- **Only the United Kingdom and Hasbro U.S. have defined fan-out schedules.** Markets that are not live on HERO, including Asia Pacific and Latin America, have **no defined schedule**. If the page implies otherwise anywhere, correct it. Never extrapolate one market's times to another.
- Replace the admonition text in `docs/reference/batch-orchestration-updates.md` the same way and fix its cross-reference to the timing page.
- The UK weekday cadence is **three** runs, not six. There is **no 23:00 catch-up**.
- Frequency can be increased if the business needs it, but there is a practical limit. Do not state a future cadence.
- Grep the whole `docs/` tree for `10:00`, `16:00`, `23:00` and `catch-up`, and remove every occurrence tied to this schedule. Leave the weekly export job timings in the cycle-calendar tables alone; those are a different process with their own context.

---

## Change 2 — The Forecast Calculation Range chapter needs the mechanism it is missing [REQUIRED]

`docs/workflows/forecast-range-calculation.md` explains what the range is and how it is generated, but not how it actually removes numbers. Everything below is new to the page.

**2a. A range is a continuous period, not a year bucket** (fact 112). One start date, one end date, and every period outside them is out of range whatever calendar year it falls in. "We only use the range for 2027" describes when the mechanism was adopted, not how far it reaches. A range loaded for a 2027 need, on a SKU that also traded in 2026, puts the 2026 weeks out of range for that record. **State this first on the page.** It is the misunderstanding that generated every case below it.

**2b. The Management Indicator decides whether an out-of-range value survives** (facts 106, 114, 115). New content, and the page does not mention the field at all today.

- Where a period carries Management Indicator `M`, a value outside the range is **preserved**. Where it carries `H`, it is **removed**.
- The flag must be present at **Levels 3, 2 and 1** for the affected periods. Partial marking is not protection.
- The mechanism, from the Logility vendor documentation in this kit: the range does not zero anything by itself, it zeroes **through the Calculate Forecasts program (FCP)**, and the FCP writes into the Resultant only where the period indicator is `N` or `H`. For any other indicator the quantity and the indicator are left as they were, because management has indicated they are overriding the statistically generated quantities.
- Hasbro uses only `M` and `H`. `N` carries the same exposure as `H` if it ever appears.
- `M` is **forcible**: it protects against the recalculation, not against forcing. Do not let the page imply that `M` is blanket protection.

**2c. The range constrains the force down, not the roll up** (fact 107). What the range removes on the way down stays removed. Values already sitting at a lower level are aggregated upward without the range acting on them, because the roll up is performed by the **Summing program**, which the range does not govern. This is why a Level 3 total can look correct while Levels 2 and 1 are empty, and why a Level 1 value can roll up into a Level 3 number that does not reconcile with the range supposedly governing it.

**2d. Deleting a Level 1 forecast propagates upward** (fact 111). Work at Level 1 is never overwritten by the disaggregation, which is the protection users rely on. The same property cuts the other way: clearing a customer's Level 1 forecast sends that zero up, and because the total is never pushed back down, the Level 3 number is what gets overwritten. The volume does not come back.

**2e. Start dates in the earlier year are expected, not anomalies** (fact 110). The range is derived as **On-Shelf Date minus Lead Time**, which is what pulls a January on-shelf date back to a December start. Add the early-delivery failure case: where shipments went out earlier than the lead-time logic anticipated, those weeks fall outside the range, and whether the volume survives then follows the `M`/`H` rule.

**2f. How the range is built differs by market** (facts 99, 113). Do not present either as the single global rule; say which case applies.

- **North America** decided to build the range from the **Sales Forecast**, valid for 2026 and 2027. From there, and for any newly generated portfolio, the range depends entirely on P2M.
- **UK and EMEA** used the Sales Forecast as the **disaggregation base at Level 1**, aggregated that up to Level 2, and used the resulting Level 2 surface to disaggregate the Resultant. This is a different statement about a different object. Keep them apart.

**2g. Correct the existing "missing or inactive items lose forecast" warning** on this page so it points at the `M`/`H` rule rather than leaving the reader to think any zero is a data-quality failure.

---

## Change 3 — Level 2.5 is visible in the Level 1 template [REQUIRED, corrects existing guidance]

The manual and the assistant have both been telling Level 1 users that a Level 2.5 adjustment does not appear in their template and that they must use the dashboard. **That is no longer accurate** (fact 121).

- The **Level 1 template carries the Level 2.5 adjustment as a read-only context column**, alongside read-only baseline, enrichment, prior-cycle and preliminary-forecast fields. In the forecast-partner template the editable columns are labelled *L1 base trend adjustment* and the read-only cross-level context is labelled *L2.5 adjustment*. In the `_ALL_FORECAST_PARTNERS_` BU-SKU template the labels invert.
- **What still stands** is the timing: the value appears only after post-processing has run. Per change 1 that is minutes, not a scheduled slot.
- **Do:** update `docs/tools/bu-sku-level-25-mode.md` and `docs/tools/forecast-reconciliation-template.md`. Grep `docs/` for any statement that a Level 1 user cannot see a Level 2.5 change, or that directs them to the dashboard for it, and correct each one. Treat timing and visibility as two separate questions throughout.

---

## Change 4 — Fan-out weighting: say baseline share [REQUIRED, wording + one new fact]

Facts 122, 95, 96.

- Post-processing distributes a Level 2.5 adjustment to partner rows using **baseline share**. Use that vocabulary rather than "proportional to the resultant".
- Where the slice's baseline sums to zero, the fallback is an **equal split across eligible forecast partners**. The volume survives and the customer allocation is wrong, so the Level 1 result has to be checked rather than assumed.
- The proportional basis is **per record**, not a market-wide or brand-wide average, which is why two SKUs inside one entry can behave differently.
- **New, and not in the manual today:** earlier enrichments and carried-forward reconciliation changes **do not affect the disaggregation weights**. A planner would reasonably assume they do. State it explicitly.
- Also state the partial-resultant trap: where some partners and weeks carry a baseline and others do not inside one entry, proportional weighting concentrates the whole delta onto the minority that have one, which can be worse than a flat split and looks like nothing is wrong.
- Pages: `docs/tools/bu-sku-level-25-mode.md`, `docs/examples/bu-sku-worked-examples.md`.

---

## Change 5 — When forecast is lost, recapture at Level 1 [REQUIRED, new section]

Fact 98, plus the detection correction in fact 126. Add to `docs/special-considerations/fcr-adjustment-rules.md` as a sixth case, closest in shape to Case 3C.

- **The scenario.** A product has forecast for its partners only through a given month and the range for those partners ends there, while the Consensus Forecast still carries volume beyond it. Level 3 disaggregation into those customers has nowhere to put the volume and it disappears.
- **The correct action: recapture at Level 1**, against the specific Forecast Partner that should carry the volume.
- **The trap:** recapturing at Level 2.5 makes it a base trend adjustment. Nothing stops it and nothing looks wrong at capture. On fan-out it spreads across all extended partners instead of reaching the customer that lost the volume. The total ties out and every level below it is wrong.
- **The root-cause alternative:** where the range genuinely should cover those weeks, fix the range instead of patching the symptom.
- **Detection is manual today.** Do not state that an alert exists. There is no forecast-lost check, and the input-data monitor that would host one is not deployed.
- The page currently ends with "No open questions were identified". That is no longer true. Replace it with the open items listed at the end of this spec that belong to this page.
- While on this page: **Case 3C's `(M)` tag is the same Management Indicator** described in change 2b. Today it reads like a one-off trick. Connect it to the general rule.

---

## Change 6 — Where enrichments land: five UA1 types and the rule [REQUIRED]

Facts 119, 120, and section 18.

- **`NON_STATISTICAL_DEMAND` maps to UA1** on the Field Forecast side, with a sign-based Consensus contribution. Three riders, all of which must appear: **percentage input is not supported** (there is no baseline to resolve a percentage against, quantities only); it **inherits the UA1 window**; and it is **not separately labelled in the export change-review report**, because that report classifies every UA1 change as reconciliation or base-trend activity.
- **Five enrichment types map to UA1**, not four: `PHASE_OUT`, `EXCESS_DEPLETION`, `DEMAND_PHASE_SHIFT`, `SUPPLY_SHORTAGE_COMP` and `NON_STATISTICAL_DEMAND`. `docs/reference/logility-array-mart-mapping.md` currently lists four.
- **Teach the generating rule, not just the list**, because the list will grow again: if an entry is an enrichment, is not `MARKETING`, is not `DEMAND_PLANNING`, and is not explicitly mapped to UA2 to UA6, it influences **UA1**.
- Explicit mappings for completeness: `RETAIL_PROMOTION` to UA2, `SET` to UA3, `SAMPLE` to UA4, `TMO` to UA5, `PRE_ORDER` to UA6. `MARKETING` and `DEMAND_PLANNING` have no Field Forecast array and contribute to Consensus only.
- **`NON_STATISTICAL_DEMAND` as an enrichment type** needs a full entry in `docs/tools/enrichment-capture-template.md` and a glossary entry. It carries the **full forecast volume** for a part of the portfolio a market has agreed not to forecast statistically. Scope is decided by market-level agreement, not by channel or item class. Today that means Direct Import and FAN in the UK pilot and FAN in the United States.
- **It does not retire base trend at Level 1.** A market whose non-statistical demand is recurring at SKU and customer level may reasonably prefer the base-trend route, and choosing it is not an error. Both are supported and the choice belongs to the market.
- `<!-- TODO: confirm with Rene -->` the literal value as it appears in the template's Enrichment Type field. `NON_STATISTICAL_DEMAND` follows the convention of every other type but the exact string is unconfirmed.

---

## Change 7 — TMO is not a timing exception [VERIFY + CORRECT if present]

Fact 123. TMO maps to **UA5 only**, is excluded from the Consensus export, does not drive ADS3, and flows across horizon months 0 to 21 like the other non-UA1 field arrays. The earlier model in which TMO alone could flow inside months 0 to 4 was **explicitly abandoned** and the control fields supporting it were removed. TMO is special in **mapping**, not in **timing**. Grep `docs/` for any framing of TMO as a frozen-window timing exception and correct it.

---

## Change 8 — The UA1 horizon and the end of UA1 protection [REQUIRED, handle carefully]

Facts 116 and 117. This one has a live divergence and a partial approval. **Do not flatten either.**

**8a. The horizon ends at month 21.** UA1 reaches the same horizon as UA2 to UA6, ADS2 and Promo Lift. `docs/help/glossary.md` and `docs/reference/logility-array-mart-mapping.md` already say months 5 to 21; **keep 21 as the end**.

**8b. The build currently ends it at month 12.** This is a known gap being corrected with the technical team, not a design change. Add a short, calm note where the horizon is stated: users may observe UA1 not publishing beyond month 12 today, that is the known build gap, and it is not a defect in their own work. Do not teach month 12 as the target. `<!-- TODO: confirm with Rene -->` when the export window has been extended, then remove the note.

**8c. UA1 protection is being retired cycle by cycle.** The start of the window steps down one month per cycle: September protects horizon months 0 to 3, October 0 to 2, November 0 to 1, December 0 only, and from the January 2027 cycle there is no protection and HERO writes UA1 from month 0. **The frozen period itself does not disappear.** What ends is HERO holding UA1 back inside it.

**8d. Approved in both pilot markets.** The United States approved on 27 August 2026 and the United Kingdom on 28 August 2026. Write the step-down as agreed direction for both pilot markets. It is still a **pilot-market** decision, so do not extend it to markets that are not live on HERO.

---

## Change 9 — Frozen-window carry-forward: say which number appears [REQUIRED, precision fix]

Fact 124. `docs/help/glossary.md` currently says the published value "carries the live Logility UA1 / baseline instead", which reads as though either is acceptable. They are different numbers.

- **Intended behaviour:** carry the current live Logility **UA1** array.
- **Current implementation:** carries the current live Logility **baseline**, because the export fetch path does not yet expose the live UA1 array as an input field.

Say which one happens and that the other is intended. Note that this gap shrinks as the protection steps down and disappears when it ends.

---

## Change 10 — What HERO sends to Logility [REQUIRED, new content]

Fact 125. Add to `docs/reference/logility-array-mart-mapping.md` and `docs/workflows/timing-system-sync.md`.

- Users author **deltas** in HERO. The export contains **complete replacement values** for the affected Logility array and week cells. Those are not the same thing and the distinction explains several questions users ask.
- HERO **rounds output to whole units** at partner, SKU and week grain. Small aggregate differences can appear when many fractional Level 2.5 fan-out cells are rounded separately. This is the answer to "why does my BU-SKU total not tie exactly to the sum of the partners".

---

## Change 11 — Glossary entries [REQUIRED]

Add to `docs/help/glossary.md`:

- **Management Indicator** — the per-item, per-level, per-week flag that tells Logility how to treat a period's forecast. `M` (Manual) means the planner owns the number and an out-of-range value is preserved. `H` (Historical) means the statistical model owns it and an out-of-range value is removed. It is the same field Logility calls the **Resultant Forecast Override Indicator**; Hasbro uses two of its six user-settable values.
- **Forecast Calculation Range** — tighten the existing "Forecasting range" entry so it states the continuous-period property from change 2a, and separate it cleanly from the **portfolio extension**, which decides which customers can hold forecast for a SKU at all. Two lines worth teaching directly:
  > The Forecast Calculation Range defines which customer and which periods receive part of the resultant, the baseline.
  > The portfolio extension defines which customers can hold forecast for a SKU at all, whether or not that forecast was generated statistically.
- **`NON_STATISTICAL_DEMAND`** — per change 6.
- **Summing program** — the pass that brings the sum of the children up to the parent, operating only on Resultant Forecasts. Not governed by the Forecast Calculation Range. Needed for change 2c to make sense.

---

## Change 12 — Consolidated dashboard [REQUIRED if absent]

Fact 105. The separate per-market reports are replaced by a **single consolidated dashboard**. A user sees the market they are authorised for and nothing else. Members of regional teams see every market in their region that is already live on HERO, in one view. Update `docs/tools/reference-views-dashboards.md`.

---

## Change 13 — Documentation governance [REQUIRED]

`docs/reference/documentation-governance.md`.

- Log this revision, its date, and the four Canonical Facts sections it lands.
- Record that the **HERO product repository is the canonical source for product behaviour**, and that where this manual describes how the tool behaves it should defer to that source rather than restating it.
- Record the **four-tier authority model** adopted on 28 August 2026: Tier 1 current canonical, Tier 2 current specialised, Tier 3 proposed or in flight and **not proof of deployment**, Tier 4 historical. Where two documents conflict, use the higher tier and open a correction against the lower one.

---

## Rules

- **Never present open design topics as decided.** If a fact is not in this kit, flag it as `<!-- TODO: confirm with Rene -->` rather than inventing it. Changes 6, 8b and 8d each carry one already.
- **Do not restate product behaviour that belongs to the HERO product team's own documentation.** The pack in this kit (`HERO_BRAVE_Knowledge_Base_repo.txt`) covers workbook and upload behaviour, stale-template collisions, enrichment identity and status, Excel formula handling, and the escalation checklist. Cross-reference rather than copy. A second, staler copy of content that changes with the code is the failure this spec exists to avoid.
- **Preserve every `!!! question "Gaps & Open Questions"` block** except where this spec explicitly replaces one (change 5).
- Keep MkDocs Material conventions. **Do not change the nav** unless a change here requires a new page, and if it does, say so in `BUILD_NOTES.md` first.
- Numbers stay **directional**. Nothing in this spec is a commitment.
- No em-dashes in prose you write. Use commas, periods or parentheses.
- Run `mkdocs build --strict` and fix anything you break.
- Regenerate the consolidated manual with `tools/generate_manual_full.py` and produce a drop with `tools/make_drop.py`.

---

## Open items to carry into the pages, not to resolve

These are genuinely open. Record them in the relevant page's Gaps block, do not answer them.

- Whether a forecast-lost check will be added when the input-data monitor is deployed. Owner: Rene Bartoli / Jarred Bultema. Page: `fcr-adjustment-rules.md`.
- Confirmation that the UA1 export window has been extended to month 21. Owner: Jarred Bultema. Pages: glossary, array mapping.
- The Level 2 out-of-range scenario has not yet been exercised in the system. The expected behaviour is stated in change 2c; a dummy-data test in Logility is pending. Page: `forecast-range-calculation.md`.
- Whether a corrective Management Indicator pass over 2026 is planned, or the affected volume is recaptured case by case. Owner: Rene Bartoli. Page: `fcr-adjustment-rules.md`.
- The literal `NON_STATISTICAL_DEMAND` string as it appears in the template. Owner: Rene Bartoli.
- Four Logility configuration questions raised by the vendor documentation and not yet answered: the Resultant Forecast default indicator, which Sum Option is run, whether Summing Resultant runs after the Calculate Forecasts program, and whether the Adjusted Demand indicator set (`M`, `P`, `Z`) is used in history cleansing. Owner: Jarred Bultema / Genpact. Page: `logility-array-mart-mapping.md`.

---

## Change 14 — Do not let a market bloc imply a shared schedule [REQUIRED, verify + correct]

Facts 128 to 130. The manual, like the knowledge base, groups markets into Europe (which operates with FAST) and everywhere else. **That grouping exists to explain how a TMO is captured, and nothing else.**

- It does **not** govern job schedules, system configuration, which markets are live, horizons, windows or cycle calendars.
- A **process rule** may travel across markets. A **configuration value**, such as a schedule or a horizon, is set per market and **never travels by inference**.
- Only the United Kingdom and Hasbro U.S. are live with defined schedules. For any other market the honest answer is **not yet defined**.

**Do:** grep `docs/` for statements that a rule applies to "North America, Asia Pacific and Latin America" or to "the non-FAST markets", and check each one. Where the statement is about **TMO capture or an enrichment process rule**, leave it. Where it is about **a schedule, a configuration value or a system behaviour**, scope it to the markets that actually have one, or state that it is undefined elsewhere. Add a short note to `docs/reference/documentation-governance.md` recording the distinction.
