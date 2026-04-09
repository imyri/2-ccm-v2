# SpecSpy Research Guide (SPECS_GUIDE.md)

This guide defines the process for transforming raw trend signals into high-authority research reports.

## The SpecSpy Loop

1. **Scan Signals**: Look into `Db/Signals/` for the latest JSON files.
2. **Prioritize**: Pick a signal that has:
    - High view count relative to the uploader's subscriber base (outlier performance).
    - A clear "Product" or "Tool" being mentioned.
3. **Deep Dive (The Agent's Job)**:
    - Use browser tools to find the official website of the tool/topic.
    - Identify the "Core Problem" it solves.
    - Find "Free Alternatives" (sticking to global project rules).
    - Analyze the "Viral Hook" used in the original video.
4. **Report**: Use the `Backend/instructions/01D_research_template.md` to draft the report in `Db/Research`.

## Quality Standards
- **Factual**: Zero hallucinations. If a spec isn't found, mark as "N/A".
- **Actionable**: A Narrative Agent should be able to write a script based *only* on this report.

---
*Room: Backend/instructions*
