# Implementation Plan - Airtable Signal Synchronisation

This plan introduces external integration with Airtable to provide a centralized, collaborative database for all captured trend signals.

## Phase Goal
Deploy the `01D_airtable_sync.py` module and integrate it into the Discovery workflow.

## Proposed Changes

### 1. Airtable Sync Module ([DISC-03](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [01D_airtable_sync.py](file:///d:/ysp/2-ccm-v2/00-System/modules/01D_airtable_sync.py)**: A Python module that:
    - Reads the `signals_...json` files.
    - Connects to Airtable via `pyairtable`.
    - Batches records (Airtable limit is 10 per request).
    - Checks for existing records by `Signal ID` to avoid duplicates.

### 2. Environment Configuration
- **[MODIFY] [.env](file:///d:/ysp/2-ccm-v2/.env)**: Add placeholders for:
    - `AIRTABLE_PAT`: Personal Access Token.
    - `AIRTABLE_BASE_ID`: Found in the Airtable API documentation for your base.
    - `AIRTABLE_TABLE_NAME`: The name of the table (e.g., "Trend Signals").

### 3. Requirements Update
- **[MODIFY] [requirements.txt](file:///d:/ysp/2-ccm-v2/requirements.txt)**: Add `pyairtable`.

## User Review Required

> [!IMPORTANT]
> **Airtable Setup**: You will need to manually create an Airtable Base and Table with the following fields (case-sensitive) for the sync to work perfectly:
> - `Signal ID` (Single line text / Unique ID)
> - `Title` (Single line text)
> - `Views` (Number)
> - `Uploader` (Single line text)
> - `URL` (URL)
> - `Captured At` (Date/Time)

## Open Questions

1. **Duplicate Handling**: Should I implement a "Check before Insert" logic to ensure a signal isn't added twice if you run the sync multiple times on the same niche?
2. **Auto-Trigger**: Once verified, would you like me to add a hook so that `01D_trend_tracer.py` automatically calls the sync module after a successful capture?

## Verification Plan

### Manual Verification
- I will create a test script to push 2-3 records from your current signal JSON to a "Test" table if you provide the keys. 
- Otherwise, I will verify the module logic by mocking the Airtable API response.
