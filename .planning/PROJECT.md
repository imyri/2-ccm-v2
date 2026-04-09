# CCM — AI-Powered Content Creation Machine

## What This Is

The CCM is a modular automation platform for indie creators built on the I.A.M. architecture (Instructions, Agents, Modules) and a Folder-as-Workspace routing system. It transforms a standard file system into an autonomous production house that handles everything from trend discovery to final social media distribution.

## Core Value

Transforming a file system into an autonomous production house through seamless AI orchestration and deterministic technical modules.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] **System Core (I.A.M.)**: Implement the Instructions, Agents, and Modules infrastructure.
- [ ] **Workflow Routing**: Set up Folder-as-Workspace vault with Context Rooms (Discovery, Narrative, Production, Monetization, Affiliate, Finance).
- [ ] **Trend Discovery**: Implement `/trendtracer` for YouTube/Twitter scanning.
- [ ] **Research Agent**: Implement `/specspy` for deep-dive authority reviews.
- [ ] **Narrative Engine**: Implement `/scriptsmith` for omnichannel script generation.
- [ ] **Multimedia Production**: Implement `/motionmuse` for video assembly using MoviePy/Remotion.
- [ ] **Omnichannel Posting**: Implement `/echoblast` for social publishing and Linktree management.
- [ ] **Community & Monetization**: Implement `/nexusnode` and `/bountybroker` for delivery and affiliate scouting.
- [ ] **Financial Automation**: Implement `/revenuereaper` and `/ledgerlord` for HDFC bank reconciliation.

### Out of Scope

- **Manual Content Editing** — The goal is maximum autonomy; manual tweaks should be handled via Instructions (I) files.
- **Direct Ad Management** — Initial versions focus on organic and affiliate growth.

## Context

The project is built on the **I.A.M. Architecture**:
- **Instructions (I)**: Markdown SOPs and localized CONTEXT.md files (the brains).
- **Agents (A)**: Claude 4.6 orchestration layer (the intelligence).
- **Modules (M)**: Deterministic Python scripts (the muscles).

The workspace is an **Obsidian Vault** organized into Context Rooms to maximize token efficiency by reducing context noise for agents.

## Constraints

- **Tech Stack**: Python (MoviePy, Scrapy, Playwright), Node.js (Remotion, potentially), Claude 4.6 (Intelligence).
- **Ecosystem**: Needs to integrate with YouTube, Twitter, Meta Graph API, HeyGen, Stripe, and HDFC CSV formats.
- **Privacy**: Financial data must be handled securely within the Finance context room.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| I.A.M. Architecture | Clear separation between AI logic and technical execution. | — Pending |
| Folder-as-Workspace | Enables Obsidian-based UI and token-efficient agent routing. | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-09 after initialization*
