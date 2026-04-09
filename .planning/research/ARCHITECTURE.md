# ARCHITECTURE.md — System Blueprint

## Component Boundaries

1. **Discovery Context Room**: `/trendtracer` (Module) outputs raw JSON to `01-Discovery/Trends/`.
2. **Narrative Context Room**: `/scriptsmith` (Agent) reads Trends and Writes Scripts to `02-Narrative/Scripts/`.
3. **Production Context Room**: `/motionmuse` (Module) reads Scripts and produces MP4 to `03-Production/Output/`.
4. **Distribution Context Room**: `/echoblast` (Module/Agent) publishes to platforms and updates `Linktree`.

## Data Flow

- **Signal In**: JSON (Trends)
- **Insight In**: Markdown (Research Reports)
- **Creative In**: Script JSON + Visual Assets
- **Output**: Video File + Platform Metadata
- **Feedback**: CSV/Postgres (Performance Logs)

## Suggested Build Order

1. **Phase 1: Foundation**: I.A.M. Routing & Shared Workspaces.
2. **Phase 2: Signal Intel**: `/trendtracer` & `/specspy` integration.
3. **Phase 3: Narrative Engine**: `/scriptsmith` Persona grounding.
4. **Phase 4: Fabrication**: `/motionmuse` Basic video templates.
5. **Phase 5: Distribution**: `/echoblast` Automation loops.

---
*Last updated: 2026-04-09*
