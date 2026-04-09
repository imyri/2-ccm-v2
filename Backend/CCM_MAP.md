# CCM Master Floor Plan (CCM_MAP.md)

This map defines the routing logic for the AI-Powered Content Creation Machine.

## Workspace Routing Table

| Context Room | Focus Area | Key Instructions | Primary Modules |
|--------------|------------|------------------|-----------------|
| **00-System** | Core Infrastructure | n/a | `00S_core_utils.py` |
| **01-Discovery** | Trend Intel & Research | `01D_context_intel.md`, `01D_specs_guide.md` | `01D_trend_tracer.py`, `01D_signal_aggregator.py`, `01D_airtable_sync.py` |
| **02-Narrative** | Ideation & Scripting | `02N_context_writer.md` | `/scriptsmith` |
| **03-Production** | Multimedia Generation | `03P_context_producer.md` | `/motionmuse` |
| **04-Monetization** | Sales & Courses | `04M_context_money.md` | `/nexusnode` |
| **05-Affiliate** | Partnerships | `05A_context_partner.md` | `/bountybroker` |
| **06-Finance** | Revenue & Payouts | n/a | `/revenuereaper` |

## Navigation Rules
- **Enter Room**: Read the local `CONTEXT_*.md` file immediately upon entering a context directory.
- **Cross-Room Data**: Data should flow from 01 → 02 → 03 → 04/05 → 06.
- **Logging**: All internal agent reasoning should be logged in a `SESSIONS.md` (to be created) within the relevant room.

---
*Last updated: 2026-04-09*
