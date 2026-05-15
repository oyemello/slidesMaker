# AmEx PowerPoint Presentation Maker

Create professional American Express presentations instantly. Describe your content, get a polished, banker-grade .pptx with perfect design, layout, colors, and typography applied automatically.

## Quick Start

Just describe what you want:

```
Create a PowerPoint about Q2 financials with:
- Title slide
- Metrics slide: Revenue $2.3B (+15%), Customers 52M (+8%)
- Key insights on market growth
- Next steps
```

The skill generates a fully designed presentation. You don't need to think about colors, spacing, fonts, or layout—it handles that automatically based on the design system.

## Files You Can Customize

- **`references/DESIGN.md`** — The design system (colors, typography, spacing, component styling). This is the source of truth for all design decisions.
- **`references/color-tokens.json`** — Brand colors extracted from DESIGN.md (optional reference).
- **`references/material-icons-index.json`** — 5,000+ Google Material Design icons, indexed by use case (e.g., "person" for user/profile/avatar).

## How It Works

The skill reads `DESIGN.md` to understand your brand design rules, then intelligently applies them when generating slides. Icons are matched to content by keyword, colors are chosen semantically (green for growth, red for decline), and layouts adapt based on content type.

For details on customizing the design system, see `DESIGN.md`.  
For how to use the skill, see `SKILL.md`.

## Dependencies

- Python 3.7+
- `python-pptx` (install with `pip install python-pptx`)

---

**Created:** May 15, 2026  
**Compatible with:** Claude Code, Copilot  
**Icon Source:** Google Material Design  
