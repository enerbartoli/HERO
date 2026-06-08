<!-- docs/help/validation-error-catalogue.md -->

# Validation & error catalogue

## Who should read this page

Anyone whose upload was rejected, and anyone supporting users in office hours.

## Purpose

List the validation messages HERO can return and how to fix each one.

!!! note "How rejection works"
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

## Related pages

- [End-to-end workflow](../workflows/end-to-end-workflow.md)
- [Field-by-field reference](../workflows/field-by-field-reference.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
