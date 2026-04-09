import sys
import os
import json
import importlib
from pyairtable import Api
from pyairtable.formulas import match

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class AirtableSync(CCMModule):
    def __init__(self):
        super().__init__("AirtableSync")
        self.pat = os.getenv("AIRTABLE_PAT")
        self.base_id = os.getenv("AIRTABLE_BASE_ID")
        self.table_name = os.getenv("AIRTABLE_TABLE_NAME")
        
    def sync_json_to_airtable(self, json_path):
        """Upload signals from JSON to Airtable with duplicate checking."""
        if not all([self.pat, self.base_id, self.table_name]):
            self.logger.error("Airtable credentials missing in .env")
            return "Error: Missing Credentials"

        if not os.path.exists(json_path):
            self.logger.error(f"JSON file not found: {json_path}")
            return "Error: File Not Found"

        with open(json_path, 'r', encoding='utf-8') as f:
            signals = json.load(f)

        if not isinstance(signals, list):
            self.logger.error("JSON data must be a list of signals.")
            return "Error: Invalid Data Format"

        self.logger.info(f"Connecting to Airtable base: {self.base_id}")
        api = Api(self.pat)
        table = api.table(self.base_id, self.table_name)
        
        synced_count = 0
        skipped_count = 0
        
        # We'll build records based on our schema
        records_to_create = []
        
        for signal in signals:
            signal_id = signal.get("id")
            if not signal_id:
                continue
                
            # Check for duplicate
            formula = match({"Signal ID": signal_id})
            existing = table.all(formula=formula)
            
            if existing:
                skipped_count += 1
                continue
            
            # Map field names
            # Note: Fields must match the Airtable schema exactly
            record_fields = {
                "Signal ID": signal_id,
                "Title": signal.get("title"),
                "Views": signal.get("view_count", 0),
                "Uploader": signal.get("uploader"),
                "URL": signal.get("url"),
                "Captured At": signal.get("captured_at")
            }
            records_to_create.append(record_fields)
            
        # Airtable allows batch creates of 10
        if records_to_create:
            for i in range(0, len(records_to_create), 10):
                batch = records_to_create[i:i+10]
                table.batch_create(batch)
                synced_count += len(batch)
                self.logger.info(f"Uploaded batch of {len(batch)} records.")

        self.logger.info(f"Sync Complete. Added: {synced_count}, Skipped: {skipped_count}")
        return {"added": synced_count, "skipped": skipped_count}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 01D_airtable_sync.py <json_path>")
        sys.exit(1)
        
    path = sys.argv[1]
    syncer = AirtableSync()
    result = syncer.sync_json_to_airtable(path)
    print(f"Sync result: {result}")
