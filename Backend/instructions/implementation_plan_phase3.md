# Implementation Plan - Phase 3: Narrative Engine

This phase focuses on the "N" room (Narrative), transforming research reports into high-converting social media scripts.

## Phase Goal
Deploy the `/scriptsmith` module and the Narrative SOP to automate viral scripting.

## Proposed Changes

### 1. ScriptSmith Module ([NARR-01](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [02N_script_smith.py](file:///d:/ysp/2-ccm-v2/00-System/modules/02N_script_smith.py)**: Python module that takes a research Markdown file as input and generates a viral script based on predefined high-retention frameworks.
- **[MODIFY] [00S_core_utils.py](file:///d:/ysp/2-ccm-v2/00-System/modules/00S_core_utils.py)**: Potentially add a generic "Prompting" utility to standardise LLM calls (Anthropic/Gemini).

### 2. Narrative SOP ([NARR-02](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [02N_scripting_sop.md](file:///d:/ysp/2-ccm-v2/02-Narrative/instructions/02N_scripting_sop.md)**: Detailed instructions on tone, pacing, and hooks for different platforms (X, YouTube Shorts, LinkedIn).
- **[NEW] Script Templates**: Add `02N_short_form_template.md` and `02N_thread_template.md` to ensure output consistency.

## User Review Required

> [!IMPORTANT]
> To keep within the **Free Resources Only** rule, `/scriptsmith` will prioritize using free local models (via Ollama) or the Gemini free tier if possible. Please confirm if you have a preference for the "brain" of this module.

## Open Questions

1. **Target Platforms**: Which platforms should we prioritize for the scripts? (e.g., "YouTube Shorts & X Threads" or "Reels & LinkedIn").
2. **Personality Choice**: Do you want a specific persona (e.g., "The Pragmatic Minimalist", "The Hype Specialist") for the generated scripts?

## Verification Plan

### Automated Checks
- Run `02N_script_smith.py` with the research report generated in Phase 2 and verify the script output in `02-Narrative/Scripts/`.

### Manual Verification
- Review the generated script for "cringe-factor" and adherence to the "Free Resources" constraint (i.e., ensure it doesn't recommend paid tools unless requested).
