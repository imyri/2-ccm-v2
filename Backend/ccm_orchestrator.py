import os
import sys
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

# Ensure we can import from modules
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules"))

import importlib

# Helper to import our numbered modules
def import_ccm_module(module_name):
    return importlib.import_module(f"modules.{module_name}")

CCMModule = import_ccm_module("00S_core_utils").CCMModule
TrendTracer = import_ccm_module("01D_trend_tracer").TrendTracer
SignalAggregator = import_ccm_module("01D_signal_aggregator").SignalAggregator
SpecSpy = import_ccm_module("01D_spec_spy").SpecSpy
ScriptSmith = import_ccm_module("02N_script_smith").ScriptSmith
MotionMuse = import_ccm_module("03P_motion_muse").MotionMuse
AirtableSync = import_ccm_module("01D_airtable_sync").AirtableSync

class CCMOrchestrator(CCMModule):
    def __init__(self):
        super().__init__("Orchestrator")
        self.tracer = TrendTracer()
        self.aggregator = SignalAggregator()
        self.spy = SpecSpy()
        self.smith = ScriptSmith()
        self.muse = MotionMuse()
        self.syncer = AirtableSync()

    def run_pipeline(self, keyword):
        """Execute the full end-to-end automation pipeline."""
        self.logger.info(f"STARTING CCM Pipeline for niche: {keyword}")
        
        # 1. Discovery
        self.logger.info("--- Phase 1: Discovery ---")
        signal_file = self.tracer.fetch_youtube_trends(keyword, max_results=5)
        if not signal_file:
            self.logger.error("Failed to fetch signals. Aborting.")
            return
            
        # 2. Aggregation (Optional but good for cleanliness)
        self.logger.info("--- Phase 2: Aggregation ---")
        summary_file = self.aggregator.aggregate_daily_signals()
        
        # 3. Research (SpecSpy)
        # We'll use the signal_file directly for the top signal
        self.logger.info("--- Phase 3: Technical Research ---")
        research_report = self.spy.research_signal(signal_file)
        if not research_report or "Error" in research_report:
            self.logger.error(f"Research failed: {research_report}")
            return

        # 4. Scripting (ScriptSmith)
        self.logger.info("--- Phase 4: Scripting ---")
        script_file = self.smith.generate_script(research_report, platform="ShortForm")
        if not script_file or "Error" in script_file:
            self.logger.error(f"Scripting failed: {script_file}")
            return

        # 5. Production (MotionMuse)
        self.logger.info("--- Phase 5: Visual Production ---")
        shot_list = self.muse.generate_shot_list(script_file)
        if not shot_list or "Error" in shot_list:
            self.logger.error(f"Shot list generation failed: {shot_list}")
            return

        # 6. Monetization/Sync (Airtable)
        self.logger.info("--- Phase 6: Ecosystem Sync ---")
        sync_result = self.syncer.sync_json_to_airtable(signal_file)
        
        self.logger.info("Pipeline Execution Complete!")
        self.logger.info(f"Final Assets Generated:")
        self.logger.info(f"- Signals: {signal_file}")
        self.logger.info(f"- Research: {research_report}")
        self.logger.info(f"- Script: {script_file}")
        self.logger.info(f"- Shot List: {shot_list}")
        self.logger.info(f"- Sync Result: {sync_result}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ccm_orchestrator.py <keyword>")
        sys.exit(1)
        
    niche = sys.argv[1]
    orchestrator = CCMOrchestrator()
    orchestrator.run_pipeline(niche)
