# CCM Global Agent Guidelines (CLAUDE.md)

This document defines the behavioral identity and operational rules for the AI Agents within the CCM ecosystem.

## Primary Directive
Transform the local file system into an autonomous production house while strictly adhering to the **I.A.M. Architecture**.

## Universal Rules
1. **Strict Filename Structure**: Every file (scripts, instructions, logs) must follow the `XXY_filename.ext` pattern where `XX` is the room number and `Y` is the room initial (S, D, N, P, M, A, F). 
   - *Example*: `01D_trend_tracer.py` (A discovery module), `02N_context_writer.md` (Narrative instructions).
2. **Free Resources Only**: Every script, API call, and external dependency must utilize free tiers or open-source resources. Avoid paid credits/subscriptions unless explicitly overridden by the user.
3. **Context Isolation**: Always respect the Context Room boundaries. When working in a room (e.g., `01-Discovery`), only read relevant instructions and data from that room.
4. **Deterministic Execution**: Agents (A) must never perform complex technical tasks directly if a Module (M) exists. Always delegate technical execution to Python modules.
5. **Markdown Interface**: All reports, ideas, and configurations must be written in Markdown to remain Obsidian-compatible and human-readable.

## Interaction Model (I.A.M.)
- **Instructions (I)**: Read `CCM_MAP.md` and local `CONTEXT.md` before taking action.
- **Agents (A)**: Use reasoning to plan steps based on Instructions.
- **Modules (M)**: Call modules via slash commands (e.g., `/trendtracer`).

## Coding Standards
- **Python**: Use `venv` for all dependencies. Follow PEP 8.
- **Formatting**: Use clean, descriptive titles and headers in all Markdown artifacts.

---
*Last updated: 2026-04-09*
