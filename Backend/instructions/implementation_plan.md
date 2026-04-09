# Implementation Plan - Phase 2: Signal Intelligence

This phase implements the automated discovery of viral triggers and deep niche research.

## Phase Goal
Deploy the `/trendtracer` module to gather raw signals from YouTube and establish the `/specspy` research framework.

## Proposed Changes

### 1. TrendTracer Module ([DISC-01](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [trend_tracer.py](file:///d:/ysp/2-ccm-v2/00-System/modules/trend_tracer.py)**: Python module utilizing `yt-dlp` to extract trending video data (titles, view counts, upload dates) for a specific niche. 
- **[NEW] [signal_aggregator.py](file:///d:/ysp/2-ccm-v2/00-System/modules/signal_aggregator.py)**: Simple utility to merge signals from different sources into a unified daily JSON.

### 2. SpecSpy Research Framework ([DISC-02](file:///d:/ysp/2-ccm-v2/.planning/REQUIREMENTS.md))
- **[NEW] [SPECS_GUIDE.md](file:///d:/ysp/2-ccm-v2/01-Discovery/instructions/SPECS_GUIDE.md)**: SOP for the agent to transform raw JSON signals into a structured research report in Markdown.
- **[NEW] Research Template**: Add a `RESEARCH_TEMPLATE.md` to ensure consistent data points (Problem, Solution, Viral Hook, Technical Specs).

## User Review Required

> [!WARNING]
> Due to X.com's aggressive anti-scraping measures on free tiers, `/trendtracer` will initially prioritize **YouTube** and **Public RSS/Search** signals. We can integrate social scrapers once a more robust proxy/headless solution is needed.

## Open Questions

1. **Target Niche**: What specific niche should we run our first tests on? (e.g., "AI Side Hustles", "SaaS Automation", "Crypto Trends").
2. **Frequency**: Should TrendTracer be designed to run as a cron-style job, or strictly on-demand via slash command for now?

## Verification Plan

### Automated Checks
- Run `trend_tracer.py` with a test keyword and verify JSON output in `01-Discovery/Trends/`.
- Validate that the JSON contains `view_count` and `title` keys.

### Manual Verification
- I will manually execute the `specspy` logic (reading a signal JSON and writing a report) to confirm the `SPECS_GUIDE.md` is practical.
