# Implementation Plan - Phase 4: Fabrication (Multimedia)

This phase completes the core CCM loop by establishing the "P" room (Production) and building the framework to visualize narrative scripts.

## Phase Goal
Deploy the `/motionmuse` module to transform scripts into structured shot lists and automated visual assets.

## Proposed Changes

### 1. MotionMuse Module ([PROD-01, PROD-02](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [03P_motion_muse.py](file:///d:/ysp/2-ccm-v2/00-System/modules/03P_motion_muse.py)**: Python module that parses a finished script and outputs a `03P_shot_list.json`. This JSON will map timestamps to:
    - Visual Description (Prompt for generator).
    - Text Overlay Content.
    - Audio/Voiceover cues.
- **[NEW] Asset Generator Integration**: Use the agent's image generation capabilities to populate the `03-Production/Assets/` folder based on the shot list.

### 2. Production SOP ([PROD-02](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [03P_production_sop.md](file:///d:/ysp/2-ccm-v2/03-Production/instructions/03P_production_sop.md)**: SOP for assembling assets.
- **[NEW] Directory Schema**: Initialize `03-Production/Shots/` and `03-Production/Assets/`.

## User Review Required

> [!CAUTION]
> Automated video rendering (via `ffmpeg`) depends on your local system's installed codecs and binary paths. To maintain the **Free Resources Only** rule and avoid installation headaches, I recommend focusing on generating the **Shot List + Visual Assets**, which you can then drag-and-drop into a free editor like CapCut or DaVinci Resolve.

## Open Questions

1. **Assembly Method**: Would you like me to attempt a basic `ffmpeg` assembly script, or is a **Shot List + Asset Export** workflow sufficient for now?
2. **Standard Visual Style**: Should we define a persistent visual theme for this niche (e.g., "Minimalist Dark Mode", "High-Contrast Blueprint", "Cyberpunk Workspace")?

## Verification Plan

### Automated Checks
- Run `03P_motion_muse.py` on the "Claude Code" script and verify `03P_shot_list.json` is generated.
- Validate that the JSON contains prompts that are ready for image generation.

### Manual Verification
- I will generate 2-3 visual assets based on the shot list and save them to the `Production/Assets` room.
