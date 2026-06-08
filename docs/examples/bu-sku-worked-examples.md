<!-- docs/examples/bu-sku-worked-examples.md -->

# BU-SKU worked examples

## Who should read this page

Demand Planning and Brand Captains working in BU-SKU (Business Unit–SKU) / Level 2.5 reconciliation.

## Purpose

Show what HERO holds fixed and what can still move after a Level 2.5 adjustment, using six worked scenarios.

## The core rule

!!! warning "Level 2.5 holds the adjustment target, not the final total"
    A BU-SKU weekly entry sets the **desired BU-SKU reconciliation-adjustment total** for that week. HERO recomputes the Level 1 partner deltas to land on it, using **current baseline share**. So:
    `Final Rendered Weekly Total = Baseline + Reconciliation Adjustment + Enrichments` — the Level 2.5 edit fixes only the *reconciliation adjustment* piece.

## Example 1 — Baseline changes later

Start: Target baseline 100, Walmart 300 (share 25% / 75%); Level 2.5 adjustment **+40** → distributed +10 / +30 → finals 110 / 330 (**BU-SKU 440**). Baseline later rises to 120 / 360 (same shares) → still +10 / +30 → finals 130 / 390 (**BU-SKU 520**).
**Stayed fixed:** adjustment +40. **Moved:** final total 440 → 520.

## Example 2 — Baseline share changes later

Same +40. Baseline shifts to 200 / 200 (now 50% / 50%, total still 400) → redistributes +20 / +20 → finals 220 / 220 (**BU-SKU 440**).
**Stayed fixed:** adjustment +40 and BU-SKU total 440. **Moved:** partner split 10/30 → 20/20.

## Example 3 — Level 1 enrichments change later

Start finals 110 / 330 (BU-SKU 440). Add Level 1 enrichments +15 (Target) / +5 (Walmart) → finals 125 / 335 (**BU-SKU 460**).
**Stayed fixed:** adjustment +40. **Moved:** final total +20, because enrichments are a separate component. Level 2.5 does not hold against later enrichment changes.

## Example 4 — Level 1 reconciliation changes later

Existing L1 reconciliation +5 / +15; Level 2.5 target +40 wants final partner reconciliation +10 / +30, so extra deltas +5 / +15. If L1 reconciliation later changes to 0 / +20, HERO re-nets: extra deltas become +10 / +10 — final still lands +10 / +30 (**total +40**).
**Key behaviour:** later L1 reconciliation does not stack on top; HERO re-nets so the **active BU-SKU target wins** at aggregate level. This is why older L1 workbooks are stale after the L2.5 handoff.

## Example 5 — A later Level 2.5 change replaces the earlier one

Original +40 (+10 / +30). User changes the week to **+60** → with 25% / 75% share → +15 / +45 → finals 115 / 345 (**BU-SKU 460**). A newer Level 2.5 edit **replaces** the earlier intent for that week.

## Example 6 — Baseline total stays similar but review still matters

Start: 150 / 250 (37.5% / 62.5%); +40 → +15 / +25. Baseline later moves to 260 / 140 (65% / 35%, total still 400) → +26 / +14. Total still +40 and the aggregate may look fine, but the **partner allocation changed substantially** — exactly the case to re-review.

## What to review

!!! tip "Re-review a BU-SKU-week when, after a Level 2.5 edit:"
    - the baseline total moves materially,
    - the baseline share across partners moves materially,
    - overlapping Level 1 enrichments change,
    - overlapping Level 1 reconciliation changes,
    - another Level 2.5 adjustment is made.

    Review question: *"The later-stage BU-SKU adjustment is still in place, but the underlying forecast moved afterward. Do we still want this same Level 2.5 adjustment?"*

## Related pages

- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Calculation reference](calculation-reference.md)

!!! note "Review is manual"
    HERO does not automatically flag these conditions — re-review is a manual step. After any later change to baseline, enrichments, or Level 1 reconciliation, re-open the affected BU-SKU-week and confirm the adjustment is still right.

!!! success "No open questions identified"
    No open questions were identified from the available source material.
