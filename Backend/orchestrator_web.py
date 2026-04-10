import sys
import os
import asyncio
from fastapi import FastAPI, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import glob
from datetime import datetime

# Adjust path to import modules
# This file is in Backend/orchestrator_web.py
# Modules are in Backend/modules/
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import importlib

# Dynamic imports for modules with numeric prefixes
def load_module(module_path, class_name):
    module = importlib.import_module(module_path)
    return getattr(module, class_name)

TrendTracer = load_module("modules.01D_trend_tracer", "TrendTracer")
SignalAggregator = load_module("modules.01D_signal_aggregator", "SignalAggregator")
AirtableSync = load_module("modules.01D_airtable_sync", "AirtableSync")
ScriptSmith = load_module("modules.02N_script_smith", "ScriptSmith")
MotionMuse = load_module("modules.03P_motion_muse", "MotionMuse")
N8NHandler = load_module("modules.00S_n8n_handler", "N8NHandler")
SpecSpy = load_module("modules.01D_spec_spy", "SpecSpy")

# State tracking for HITL
pending_approvals = {} # niche -> script_path

app = FastAPI(title="CCM Control Center")

# Security & Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StatusManager:
    def __init__(self):
        self.logs = []
        self.status = "Idle"
        self.progress = 0
        self.current_step = ""

    def add_log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")
        print(f"[{timestamp}] {message}")

sm = StatusManager()

# Data Models
class AutomateRequest(BaseModel):
    niche: str

# Endpoints
@app.get("/status")
async def get_status():
    return {
        "status": sm.status,
        "progress": sm.progress,
        "current_step": sm.current_step,
        "logs": sm.logs[-20:] # Return last 20 logs
    }

@app.get("/assets")
async def get_assets():
    backend_root = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(backend_root)
    db_root = os.path.join(project_root, "Db")
    
    assets = []
    
    # --- STEP 1: DISCOVERY ---
    # 1.1 Trends & Signals
    signals = glob.glob(os.path.join(db_root, "Signals", "*.json"))
    for f in signals:
        bname = os.path.basename(f)
        atype = "Signal" if "DAILY_SUMMARY" in bname or bname == "signals_file.json" else "Trend"
        assets.append({
            "name": bname, 
            "type": atype, 
            "category": "Discovery",
            "sub_category": "Signals" if atype == "Signal" else "Trends",
            "path": f"/data/signals/{bname}", 
            "date": os.path.getmtime(f)
        })
    
    # 1.3 Database Sync (Logs)
    sync_logs = glob.glob(os.path.join(db_root, "Logs", "AirtableSync_*.log"))
    for f in sync_logs:
        bname = os.path.basename(f)
        assets.append({
            "name": bname, 
            "type": "Sync", 
            "category": "Discovery",
            "sub_category": "Sync",
            "path": f"/data/logs/{bname}", 
            "date": os.path.getmtime(f)
        })

    # --- STEP 2: NARRATIVE ---
    # 2.1 Research
    research = glob.glob(os.path.join(db_root, "Research", "*.md"))
    for f in research:
        bname = os.path.basename(f)
        assets.append({
            "name": bname, 
            "type": "Research", 
            "category": "Narrative",
            "sub_category": "Research",
            "path": f"/data/research/{bname}", 
            "date": os.path.getmtime(f)
        })

    # 2.2 Scripts
    scripts = glob.glob(os.path.join(db_root, "Scripts", "*.md"))
    for f in scripts:
        bname = os.path.basename(f)
        assets.append({
            "name": bname, 
            "type": "Script", 
            "category": "Narrative",
            "sub_category": "Scripts",
            "path": f"/data/scripts/{bname}", 
            "date": os.path.getmtime(f)
        })
        
    # --- STEP 3: PRODUCTION ---
    # 3.1 Media Assets
    media = glob.glob(os.path.join(db_root, "Media", "*.*"))
    for f in media:
        bname = os.path.basename(f)
        assets.append({
            "name": bname, 
            "type": "Asset", 
            "category": "Production",
            "sub_category": "Assets",
            "path": f"/data/media/{bname}", 
            "date": os.path.getmtime(f)
        })

    # 3.2 Shot Lists
    shots = glob.glob(os.path.join(db_root, "Shots", "*.json"))
    for f in shots:
        bname = os.path.basename(f)
        assets.append({
            "name": bname, 
            "type": "ShotList", 
            "category": "Production",
            "sub_category": "Shots",
            "path": f"/data/shots/{bname}", 
            "date": os.path.getmtime(f)
        })
    
    # Sort by date
    assets.sort(key=lambda x: x["date"], reverse=True)
    return assets

@app.post("/automate")
async def start_automation(req: AutomateRequest, background_tasks: BackgroundTasks):
    sm.status = "Running"
    sm.logs = []
    sm.progress = 0
    sm.current_step = "Initializing Pipeline"
    sm.add_log(f"Starting One-Click Automation for niche: {req.niche}")
    background_tasks.add_task(run_pipeline, req.niche)
    return {"message": "Automation started"}

@app.get("/approve")
async def approve_script(niche: str, background_tasks: BackgroundTasks):
    """Callback for n8n to approve a pending script."""
    if niche not in pending_approvals:
        return {"error": f"No pending approval for niche: {niche}"}
    
    script_path = pending_approvals.pop(niche)
    sm.status = "Running"
    sm.add_log(f"Approval received for {niche}. Resuming production...")
    background_tasks.add_task(resume_pipeline, niche, script_path)
    return {"message": f"Approval processed for {niche}"}

async def resume_pipeline(niche: str, script_path: str):
    """Phase 2 of the pipeline: Production (post-approval)."""
    try:
        # Step 3: Production
        sm.current_step = "3.1 Production: Visual Mapping"
        sm.progress = 90
        muse = MotionMuse()
        sm.add_log(f"Generating structured visual shot list for: {os.path.basename(script_path)}")
        shot_list_path = muse.generate_shot_list(script_path)
        if isinstance(shot_list_path, str) and "Error" in shot_list_path:
             raise Exception(f"Production Failure: {shot_list_path}")
        sm.add_log(f"Production planning complete: {shot_list_path}")

        sm.status = "Completed"
        sm.progress = 100
        sm.current_step = "Pipeline Finished Successfully"
        sm.add_log("CCM Pipeline Execution Finished. Assets ready for review.")
        
        # Notify n8n of completion
        n8n = N8NHandler()
        n8n.notify_event("pipeline_completed", {"niche": niche, "shot_list": shot_list_path})

    except Exception as e:
        sm.status = "Error"
        sm.add_log(f"RESUME ERROR: {str(e)}")
        logging.error(f"Resume Error: {str(e)}")

async def run_pipeline(niche: str):
    try:
        # Step 1.1: Tracing
        sm.current_step = "1.1 Discovery: Tracing Trends"
        sm.progress = 15
        tracer = TrendTracer()
        sm.add_log("Searching YouTube for trending signals...")
        json_path = tracer.fetch_youtube_trends(niche)
        if not json_path:
            raise Exception("Discovery failed: No signals found.")
        sm.add_log(f"Discovery complete. Data saved to: {json_path}")

        # Step 1.2: Aggregation
        sm.current_step = "1.2 Discovery: Identifying Signals"
        sm.progress = 30
        aggregator = SignalAggregator()
        sm.add_log("Merging daily signals and ranking views...")
        summary_path = aggregator.aggregate_daily_signals()
        sm.add_log(f"Aggregation complete: {summary_path}")

        # Step 1.3: Sync
        sm.current_step = "1.3 Discovery: Database Sync"
        sm.progress = 40
        syncer = AirtableSync()
        sm.add_log("Synchronizing signals with Content Database...")
        sync_result = syncer.sync_json_to_airtable(summary_path)
        sm.add_log(f"Airtable Sync Result: {sync_result}")

        # Step 1.4: Research (New Step integrated from SpecSpy)
        sm.current_step = "1.4 Discovery: Deep Research"
        sm.progress = 55
        spy = SpecSpy()
        sm.add_log(f"Performing technical extraction on top signal...")
        research_path = spy.research_signal(summary_path)
        if isinstance(research_path, str) and "Error" in research_path:
            raise Exception(f"Research Failure: {research_path}")
        sm.add_log(f"Research complete: {research_path}")

        # Step 2: Scripting
        sm.current_step = "2.1 Narrative: Writing Script"
        sm.progress = 75
        smith = ScriptSmith()
        sm.add_log("Invoking Gemini-2.0-Flash for viral script smithing...")
        # Use research path for scripting
        script_path = smith.generate_script(research_path, platform="ShortForm")
        if isinstance(script_path, str) and "Error" in script_path:
            raise Exception(f"Narrative Failure: {script_path}")
        sm.add_log(f"Narrative complete. Script saved: {script_path}")

        # --- HITL CHECK ---
        n8n = N8NHandler()
        if n8n.enabled:
            sm.status = "Waiting for Approval"
            sm.current_step = "HITL: Awaiting Human Review"
            sm.add_log("HITL Enabled. Sending script to n8n for approval...")
            
            # Read script content for enrichment
            with open(script_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            pending_approvals[niche] = script_path
            
            # Use niche as identifier
            approval_endpoint = f"/approve?niche={niche}"
            success = n8n.send_approval_request(niche, script_path, content, approval_endpoint)
            
            if success:
                sm.add_log("Approval requested. Pipeline paused.")
                return # Stop pipeline here
            else:
                sm.add_log("WARNING: Failed to notify n8n. Proceeding automatically to avoid block.")
        
        # Step 3: Production (Internal if HITL disabled or failed)
        await resume_pipeline(niche, script_path)

    except Exception as e:
        sm.status = "Error"
        sm.add_log(f"PIPELINE ERROR: {str(e)}")
        logging.error(f"Pipeline Error: {str(e)}")

# Set up static file locations
backend_root = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(backend_root)
db_root = os.path.join(project_root, "Db")

app.mount("/data/signals", StaticFiles(directory=os.path.join(db_root, "Signals")), name="signals")
app.mount("/data/logs", StaticFiles(directory=os.path.join(db_root, "Logs")), name="logs")
app.mount("/data/research", StaticFiles(directory=os.path.join(db_root, "Research")), name="research")
app.mount("/data/scripts", StaticFiles(directory=os.path.join(db_root, "Scripts")), name="scripts")
app.mount("/data/shots", StaticFiles(directory=os.path.join(db_root, "Shots")), name="shots")
app.mount("/data/media", StaticFiles(directory=os.path.join(db_root, "Media")), name="media")

# Serve frontend
frontend_dir = os.path.join(project_root, "Frontend")
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
