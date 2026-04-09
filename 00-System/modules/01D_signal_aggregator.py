import os
import json
import logging
from datetime import datetime

class SignalAggregator:
    def __init__(self, discovery_root="01-Discovery"):
        self.discovery_root = discovery_root
        self.trends_dir = os.path.join(discovery_root, "Trends")
        
    def aggregate_daily_signals(self):
        """Merge all signals from today into a single summary."""
        today = datetime.now().strftime('%Y%m%d')
        all_signals = []
        
        if not os.path.exists(self.trends_dir):
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
            
            summary_file = os.path.join(self.trends_dir, f"DAILY_SUMMARY_{today}.json")
            with open(summary_file, 'w', encoding='utf-8') as f:
                json.dump(all_signals, f, indent=2, ensure_ascii=False)
            return summary_file
        
        return "No signals to aggregate for today."

if __name__ == "__main__":
    aggregator = SignalAggregator()
    result = aggregator.aggregate_daily_signals()
    print(f"Aggregation result: {result}")
