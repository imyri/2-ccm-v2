import sys
import os
import json
import importlib
from datetime import datetime

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class SignalAggregator(CCMModule):
    def __init__(self):
        super().__init__("SignalAggregator")
        self.trends_dir = os.path.join(self.db_root, "Signals")
        
    def aggregate_daily_signals(self):
        """Merge all signals from today into a single summary."""
        today = datetime.now().strftime('%Y%m%d')
        all_signals = []
        
        if not os.path.exists(self.trends_dir):
            self.logger.warning("No signals found directory.")
            return "No signals found."
            
        for filename in os.listdir(self.trends_dir):
            if filename.startswith("signals_") and today in filename:
                filepath = os.path.join(self.trends_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_signals.extend(data)
                        
        if all_signals:
            # Sort by view count if available
            all_signals.sort(key=lambda x: x.get('view_count', 0) or 0, reverse=True)
            
            filename = f"DAILY_SUMMARY_{today}.json"
            summary_file = self.save_output("Signals", filename, all_signals)
            return summary_file
        
        return "No signals to aggregate for today."

if __name__ == "__main__":
    aggregator = SignalAggregator()
    result = aggregator.aggregate_daily_signals()
    print(f"Aggregation result: {result}")
