<!-- docs/examples/bu-sku-worked-examples.md -->

# BU-SKU worked examples

## Who should read this page

Demand Planning and Brand Captains working in BU-SKU (Business Unit–SKU) / Level 2.5 reconciliation.

## Purpose

Show what HERO holds fixed and what can still move after a Level 2.5 adjustment, using six worked scenarios.

## The core rule

!!! warning "Level 2.5 holds the *adjustment target*, not the final total"
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

!!! note "Takeaway"
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

!!! note "Takeaway"
    **Stayed fixed:** your adjustment (+40) *and* the BU-SKU total (440). **Moved:** the per-partner split (10/30 → 20/20). Same headline number, different distribution underneath.

---

## Example 3 — Someone adds Level 1 enrichments later

Start from Example 1 (finals 110 / 330, BU-SKU 440). Later, enrichments are added: **+15** to Target, **+5** to Walmart.

| Partner | Final before | + Enrichment | Final after |
|---|--:|--:|--:|
| Target | 110 | +15 | 125 |
| Walmart | 330 | +5 | 335 |
| **BU-SKU** | **440** | **+20** | **460** |

!!! note "Takeaway"
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

!!! note "Takeaway"
    Later L1 reconciliation does **not** stack on top of your target. HERO **re-nets** the rows so the active BU-SKU target still wins at the aggregate level. This is why older Level 1 workbooks are stale once Level 2.5 review has started.

---

## Example 5 — You change your own Level 2.5 value later

Your original adjustment was **+40** (+10 / +30). Later you decide the week should be **+60** instead.

| Partner | Baseline | Share | New +60, split by share | Final |
|---|--:|--:|--:|--:|
| Target | 100 | 25% | **+15** | 115 |
| Walmart | 300 | 75% | **+45** | 345 |
| **BU-SKU** | **400** | | **+60** | **460** |

!!! note "Takeaway"
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

!!! note "Takeaway"
    Your +40 and the BU-SKU total look unchanged, but the per-partner allocation swung sharply (15/25 → 26/14). The headline can look fine while the distribution underneath is now very different — exactly the case to re-review.

---

## When to re-review a BU-SKU week

!!! tip "Re-open a BU-SKU week after any of these happen later:"
    - the baseline total moves materially,
    - the baseline **share** across partners moves materially,
    - overlapping Level 1 enrichments change,
    - overlapping Level 1 reconciliation changes,
    - another Level 2.5 adjustment is made.

    The question to ask: *"My BU-SKU adjustment is still in place, but the forecast underneath moved — do I still want this same adjustment?"*

!!! note "Review is manual"
    HERO does not automatically flag these conditions — re-review is a manual step.

## Related pages

- [BU-SKU / Level 2.5 mode](../tools/bu-sku-level-25-mode.md)
- [Calculation reference](calculation-reference.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
