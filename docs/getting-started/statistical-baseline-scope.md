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

!!! warning "Gaps & Open Questions"
    - **EMEA treatment is not recorded here.** How Europe treats Direct Import and FAN has not been confirmed for this page.
    - **Which other segments, if any, sit outside the statistical model** in each market has not been enumerated beyond DI and FAN.
