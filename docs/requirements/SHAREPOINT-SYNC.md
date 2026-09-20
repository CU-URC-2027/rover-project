# SharePoint requirements sync

The Lean Master workbook in SharePoint is the authoritative requirements source.
GitHub stores a mirror at `docs/requirements/URC_2027_Lean_Master.xlsx` and a
generated register at `docs/requirements/master-requirements.md`.

## One-time GitHub setup

The `automation/sharepoint-master` branch receives workbook updates. The
`Sync master requirements` workflow renders the Markdown register on that
branch and creates or updates one pull request to `main`.

In repository settings, allow GitHub Actions to create pull requests and allow
the workflow's `GITHUB_TOKEN` to write repository contents. The workflow
requests only `contents: write` and `pull-requests: write`.

## Power Automate flow

Create a cloud flow owned by the team, not an individual student:

1. Use SharePoint's **When an item or a file is modified** trigger for the
   document library containing the Lean Master workbook.
2. Add a condition that the file name is `URC_2027_Lean_Master.xlsx`. This
   prevents unrelated SharePoint files from starting the sync.
3. Use **Get file content** with the trigger's file identifier.
4. Use the GitHub **Create or update file** action with these values:
   - Repository: `CU-URC-2027/rover-project`
   - Branch: `automation/sharepoint-master`
   - File path: `docs/requirements/URC_2027_Lean_Master.xlsx`
   - File content: the output of **Get file content**
   - Commit message: `docs: mirror SharePoint Lean Master workbook`
5. Save and test the flow by editing a non-sensitive cell in a copy or test
   revision of the workbook. Confirm that the GitHub Action creates or updates
   its review pull request.

Do not point the flow at `main`. A teammate must review and merge the generated
pull request before the agent or other GitHub consumers treat the update as the
current project documentation.

## Failure behavior

The GitHub Action fails without modifying the register when the `Master` sheet
or its required columns are missing. Fix the workbook structure in SharePoint,
then save it again to retry. Review pull requests for changed requirement IDs,
source/basis entries, verification checks, and open choices before merging.
