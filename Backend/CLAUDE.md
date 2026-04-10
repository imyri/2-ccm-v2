# CCM Global Agent Guidelines (CLAUDE.md)

This document defines the behavioral identity and operational rules for the AI Agents within the CCM V2.0 ecosystem.

## Primary Directive
Transform the local file system into an autonomous production house while strictly adhering to the **Full-Stack V2 Architecture (Backend, Db, Frontend)**.

## Universal Rules
1. **Strict Filename Structure**: Every module/script must follow the `XXY_filename.ext` pattern (e.g., `01D_`, `02N_`).
2. **Exponential Backoff**: Every module interfacing with an LLM API (Gemini/Anthropic) **MUST** implement exponential backoff retry logic.
3. **n8n Connectivity**: When `HITL_ENABLED` is true, modules must utilize the `Backend/modules/00S_n8n_handler.py` dispatcher for approvals.
4. **Context Isolation**: Modules must only read from/write to their designated `Db/` subdirectories (Signals, Research, Scripts, Media).
5. **Markdown Interface**: All reports, scripts, and logs must be written in clean Markdown.

## Interaction Model (I.A.M. V2)
- **Instructions (I)**: Check `Backend/instructions/` for SOPs and Context before taking action.
- **Agents (A)**: Reason and plan based on instructions. Use the **Planning Mode** for complex migration or logic changes.
- **Modules (M)**: Use existing scripts in `Backend/modules/`. Do not reinvent core utilities.

## Coding Standards
- **Backend (Python)**: PEP 8, FastAPI for orchestrator. Use standard try-except blocks with logging.
- **Frontend**: Vanilla HTML/CSS/JS. Use glassmorphic design tokens defined in `Frontend/style.css`.
- **Database**: All persistence happens in the `Db/` vault. Never store generated data in the root or code folders.

## Environment Variables
- `GEMINI_API_KEY`: Required for pipeline generation.
- `HITL_ENABLED`: Toggle for n8n/Human-in-the-loop logic.
- `N8N_HITL_WEBHOOK_URL`: Target URL for n8n approval requests.

---
*Last updated: 2026-04-10 (CCM V2.0 Stable Final)*
