# Walkthrough: Airtable Sync Integration

We now have a dedicated bridge between our local signal intelligence and a centralized Airtable database.

## 1. The AirtableSync Module
I have deployed `/airtablesync` (`01D_airtable_sync.py`), which automates the upload of trend signals.

- **Duplicate Prevention**: Automatically checks Airtable for the `Signal ID` before inserting to avoid cluttering your base.
- **Batch Processing**: Groups records into batches of 10 to comply with Airtable rate limits and speed up the sync.

## 2. Setup Requirements

To use this module, you must set up your Airtable base with these exact field names:

| Field Name | Type | Purpose |
|------------|------|---------|
| `Signal ID` | Single line text | The unique YouTube/Source ID |
| `Title` | Single line text | Video title |
| `Views` | Number | View count |
| `Uploader` | Single line text | Channel name |
| `URL` | URL | Source link |
| `Captured At` | Date/Time | Timestamp of signal capture |

## 3. Usage

1. **Configure API**: Update your [.env](file:///d:/ysp/2-ccm-v2/.env) with your `AIRTABLE_PAT`, `AIRTABLE_BASE_ID`, and `AIRTABLE_TABLE_NAME`.
2. **Run the Sync**: Execute the following command from the project root:

```powershell
.venv\Scripts\python.exe 00-System/modules/01D_airtable_sync.py "01-Discovery/Trends/signals_ai_automation_for_content_creators_20260409_1713.json"
```

## 4. Verification

- **Dependency**: Added `pyairtable` to `requirements.txt`.
- **Core Update**: Integrated into the [CCM_MAP.md](file:///d:/ysp/2-ccm-v2/CCM_MAP.md) as a primary Discovery module.

> [!TIP]
> Use the **Personal Access Token (PAT)** rather than the legacy API key for better security and future-proofing.
