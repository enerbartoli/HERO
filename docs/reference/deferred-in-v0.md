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

!!! note "AIM and POS"
    AIM = the Shipment Revenue view; POS = Point of Sale (sell-through) used in the Glidepath view. See [Reference views & dashboards](../tools/reference-views-dashboards.md).

## Related pages

- [Reference views & dashboards](../tools/reference-views-dashboards.md)
- [Roles & what each role does in HERO](../getting-started/roles-permissions.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
