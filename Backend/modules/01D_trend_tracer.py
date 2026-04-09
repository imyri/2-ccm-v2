import sys
import os
import json
from datetime import datetime, timedelta
import yt_dlp

# Adjust path to import core_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib
core_utils = importlib.import_module("modules.00S_core_utils")
CCMModule = core_utils.CCMModule

class TrendTracer(CCMModule):
    def __init__(self):
        super().__init__("TrendTracer")

    def fetch_youtube_trends(self, keyword, max_results=10):
        """Fetch trending YouTube signals using yt-dlp."""
        self.logger.info(f"Fetching signals for niche: {keyword}")
        
        ydl_opts = {
            'quiet': True,
            'extract_flat': 'in_playlist',
            'dump_single_json': True,
            'skip_download': True,
        }
        
        search_query = f"ytsearch{max_results}:{keyword}"
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                result = ydl.extract_info(search_query, download=False)
                if 'entries' in result:
                    signals = []
                    for entry in result['entries']:
                        signals.append({
                            'id': entry.get('id'),
                            'title': entry.get('title'),
                            'view_count': entry.get('view_count'),
                            'duration': entry.get('duration'),
                            'uploader': entry.get('uploader'),
                            'upload_date': entry.get('upload_date'),
                            'url': f"https://www.youtube.com/watch?v={entry.get('id')}",
                            'captured_at': datetime.now().isoformat()
                        })
                    
                    filename = f"signals_{keyword.replace(' ', '_').lower()}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
                    filepath = self.save_output("Signals", filename, signals)
                    self.logger.info(f"Successfully captured {len(signals)} signals.")
                    return filepath
                else:
                    self.logger.warning("No entries found for query.")
                    return None
            except Exception as e:
                self.logger.error(f"Error fetching YouTube signals: {str(e)}")
                return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python trend_tracer.py <niche_keyword>")
        sys.exit(1)
    
    niche = sys.argv[1]
    tracer = TrendTracer()
    tracer.fetch_youtube_trends(niche)
