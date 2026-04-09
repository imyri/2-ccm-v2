# STACK.md — Resource Engine

## Recommended 2025 Stack

| Layer | Tool | Rationale | Confidence |
|-------|------|-----------|------------|
| **Reasoning** | Claude 4.6 (Sonnet/Opus) | Best-in-class orchestration and coding capabilities. | High |
| **Orchestration** | n8n | Open-source, self-hostable, handles webhooks and long-running loops perfectly. | High |
| **Video Engine** | Remotion | Code-first (React) video generation; highly dynamic compared to static templates. | High |
| **Logic/Utility** | Python (MoviePy, Scrapy, yt-dlp) | Industry standard for data processing and lightweight media manipulation. | High |
| **Social Distribution** | Postiz / Meta Graph API | Centralized scheduling and platform-direct posting. | Medium |
| **Database/State** | Supabase (Postgres) | Simple setup for logging performance data and feedback loops. | Medium |

## Specific Library Decisions

1. **Remotion Lambda**: Recommended for scaling video rendering beyond local hardware limits.
2. **Playwright**: Superior to Selenium for modern web scraping and social media automation due to better fingerprint management.
3. **Pydantic**: For strict data validation between Agents and Modules (Modules are deterministic).

## What NOT to Use

- **Traditional Video Editors APIs**: (e.g., Shotstack) - Often too restrictive for custom branding compared to Remotion.
- **Zapier**: Too expensive at scale compared to self-hosted n8n.
- **Pure GPT-4o**: While capable, Claude 4.6 (Sonnet) consistently outperforms in complex agentic tool use and nuanced script writing.

---
*Last updated: 2026-04-09*
