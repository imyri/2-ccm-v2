import os
import sys
from pyairtable import Api
from dotenv import load_dotenv

load_dotenv()

def debug_airtable():
    pat = os.getenv("AIRTABLE_PAT")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")
    
    if not pat:
        print("❌ Error: AIRTABLE_PAT not found in .env")
        return

    print(f"🔍 Testing Token (Starts with): {pat[:10]}...")
    print(f"📡 Testing Base ID: '{base_id}'")
    print(f"📡 Testing Table Name: '{table_name}'")
    
    api = Api(pat)
    
    try:
        table = api.table(base_id, table_name)
        # Attempt to fetch 1 record to test connectivity and column access
        records = table.all(max_records=1)
        print("✅ SUCCESS! Connectivity established.")
        if records:
            print(f"Successfully read data from Airtable.")
            print("Fields found in record:", list(records[0]['fields'].keys()))
        else:
            print("Table is connected but appears to be empty.")
            
    except Exception as e:
        print(f"\n❌ CONNECTION FAILED: {str(e)}")
        print("\nFix Checklist:")
        print("1. Scopes: Does your PAT have 'data.records:read' and 'data.records:write'?")
        print("2. Base Access: Does the PAT have access to THIS specific Base ID?")
        print("3. Field Names: Does your table have a field named EXACTLY 'Signal ID'?")

if __name__ == "__main__":
    debug_airtable()
