# Prompt 5 for Claude Code — content was rewritten (tool-focus). Re-sync, don't reintroduce pilot material

Use after Prompts 1–4. The Markdown content under `docs/` was **substantially rewritten** outside Code
to make this a manual for the **HERO tool**, not a guide to the UK pilot. Pull/refresh the repo before
doing anything so you are working on the current content.

## What changed (do not undo)
- **Pilot-specific content and gaps were removed/generalised**: export cadence (Thu/Sat), frozen-window
  governance, executive sign-off ownership, cluster permission matrix, deferred-item owners. These do
  **not** belong in a tool manual. Do not reintroduce them.
- **Roles pages now describe tool capabilities**, not pilot ownership. Level 2.5 / BU-level reconciliation
  is used by Brand Captains (author the brand number) and by Demand Planning and Marketing, who first
  propose/challenge and **can author the adjustment at BU level when agreement with Sales is not reached**
  (HERO disaggregates it proportionally to customer rows). Sales makes customer-level (Level 1) edits.
  Keep this framing.
- **Canonical terms now fixed**: product name = "Hasbro Enrichment & Reconciliation Optimizer"; "Level 3"
  is a hierarchy node (not a review stage); GPL = Global Product Lead; channels are DOM/DI (D2C not used).
- **New tool facts added**: TMO is sourced from FAST (not edited in the template); Confirmed vs Proposed
  horizon; channel shift moves associated enrichments; forecasting range = start/end dates; blank end date
  = single-week event; BU-SKU re-review is manual; dashboards page populated (POS Glidepath, AIM).
- **Open questions reduced to ONE**: only `examples/calculation-reference.md` still has a
  `!!! question "Gaps & Open Questions"` block (the unit-spread rounding convention — a genuine dev/SME
  gap). Every other page ends with `!!! success "No open questions identified"`. **Do not add new gaps.**

## Hard constraints (unchanged)
- Do not rewrite or invent manual content. Fix only Markdown/links/formatting/theme.
- Preserve the single remaining Gaps block and all `!!! success` blocks as written.
- If you build the consolidated "Open Questions" page (Prompt 2 §4), it should now contain **just the one**
  rounding item — aggregate, don't author new ones.

## Small fixes to make
1. **Nav label**: in `mkdocs.yml`, the entry `Where HERO fits in the cycle` should read
   **`Where HERO fits in the planning flow`** to match the page title. (Path unchanged:
   `getting-started/hero-in-the-cycle.md`.)
2. **Re-run** `mkdocs build --strict` and confirm 0 warnings after the re-sync.
3. **Encoding check**: confirm no stray NUL/control bytes in any `docs/**/*.md` (a few files were trimmed
   of trailing padding from an external editor). `grep -rlP '\x00' docs/` should return nothing.
4. Proceed with the Prompt 4 work (collapsible nav with chevrons + larger titles, brand logos, texture
   overlays) on top of this current content.

## Report
Confirm the re-synced build passes, the nav label is fixed, no NUL bytes remain, and the Open Questions
view (if built) lists only the rounding item.
