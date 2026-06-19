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

!!! warning "Weekly pencils-down"
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

!!! note "Temporary bridge"
    This manual step is a temporary bridge. Once the automated pipeline is validated, the upload goes away.

## Related pages

- [Batch orchestration & updates](../reference/batch-orchestration-updates.md)
- [Timing & system sync](../workflows/timing-system-sync.md)

!!! success "No open questions identified"
    No open questions were identified from the available source material.
