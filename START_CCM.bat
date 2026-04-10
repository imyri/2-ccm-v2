@echo off
echo Starting CCM Control Center...
echo.
echo 1. Activating environment...
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
) else (
    echo [WARNING] .venv not found. Running with global python.
)

echo 2. Launching Orchestrator...
echo Access the dashboard at http://localhost:8000 once ready.
echo.
python Backend/orchestrator_web.py
pause
