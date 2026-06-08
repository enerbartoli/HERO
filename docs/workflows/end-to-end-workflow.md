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

!!! warning "Rejected uploads are not partially saved"
    If HERO rejects an upload, it does **not** save the bad rows. It returns an annotated workbook so you can fix the issues and try again.

## Related pages

- [Tab-by-tab walkthrough](tab-by-tab-walkthrough.md)
- [Timing & system sync](timing-system-sync.md)
- [Validation & error catalogue](../help/validation-error-catalogue.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
