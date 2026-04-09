# PITFALLS.md — Risk Mitigation

## Critical Risks & Prevention

| Risk | Prevention Strategy | Phase Address |
|------|---------------------|---------------|
| **AI Hallucinations** | Grounding with `/specspy` (Opus-level research) and human-in-the-loop review in Narrative workspace. | Phase 2 & 3 |
| **Zero-Click Search Drain** | Focus on building "Owned" traffic channels (Skool community, Email) via `/nexusnode`. | Phase 6 |
| **API Rate Limiting** | Implement robust retry-backoff logic and platform account rotation (Multi-Profile). | Phase 5 |
| **Content ID Flags** | Use royalty-free assets via `/motionmuse` and unique Remotion templates to avoid reused asset penalties. | Phase 4 |
| **Account Bans** | Use Playwright with stealth-plugin for any browser-based automation; prioritize official APIs (Meta, X) where possible. | Phase 5 |

## Common Mistakes in content automation

- **Ignoring Brand Voice**: Avoid generic LLM output; use localized Instructions (I) files per context room.
- **Over-Automation**: Publishing 100 low-quality videos/day. *Strategy: Quality over Quantity — use AI to find the 1 best trend to dominate.*

---
*Last updated: 2026-04-09*
