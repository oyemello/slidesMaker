# AmEx PowerPoint Presentation Maker Skill

A comprehensive skill for creating professional American Express PowerPoint presentations with integrated Google Material Design icons.

## Quick Start

### What This Skill Does

✅ Creates full PowerPoint presentations (.pptx files)  
✅ Integrates 5,000+ Google Material Design icons  
✅ Indexes icons by use case (not just name)  
✅ Applies branded colors via `color-tokens.json`  
✅ Uses sample PPT templates as design references  
✅ Works with both Claude Code and Copilot  

### Skill Capabilities

| Feature | Details |
|---------|---------|
| **Slide Types** | Title, content, two-column, sections, closings |
| **Icons** | 5,000+ Material Design icons indexed by keyword |
| **Branding** | Color tokens + sample template references |
| **Layout** | Auto-formatting, spacing, typography |
| **Output** | Professional .pptx ready to download/edit |

---

## File Structure

```
amex-pptx-maker/
├── SKILL.md                          # Main skill instructions
├── README.md                          # This file
├── scripts/
│   ├── __init__.py
│   ├── create_pptx.py               # Main PowerPoint generator
│   └── icon_manager.py              # Icon resolution & selection
├── references/
│   ├── material-icons-index.json    # All Material Design icons (indexed)
│   ├── color-tokens.json            # Brand colors (you populate)
│   └── (future: amex-branding.md)
└── assets/
    ├── README.md
    └── sample-ppts/
        ├── .gitkeep
        └── (add your templates here)
```

---

## Setup Instructions

### 1. Add Your Brand Colors

Edit `references/color-tokens.json` and replace the default colors with your American Express brand colors:

```json
{
  "primary": "#YOUR_PRIMARY_COLOR",
  "secondary": "#YOUR_SECONDARY_COLOR",
  "accent": "#YOUR_ACCENT_COLOR",
  "neutral": {
    "dark": "#YOUR_DARK_COLOR",
    "light": "#YOUR_LIGHT_COLOR"
  },
  "semantic": {
    "success": "#GREEN_HEX",
    "warning": "#YELLOW_HEX",
    "danger": "#RED_HEX"
  }
}
```

### 2. Add Sample PowerPoint Templates (Optional)

Place American Express branded PowerPoint files in `assets/sample-ppts/`:

- `amex-standard.pptx` — Default template
- `amex-data-dashboard.pptx` — Data visualization
- `amex-pitch-deck.pptx` — Sales/pitches
- `amex-report.pptx` — Reports

The skill will analyze these for design patterns and typography.

### 3. Install Dependencies

The skill requires `python-pptx`:

```bash
pip install python-pptx
```

---

## How to Use

### Example 1: Simple Presentation

```
Create a PowerPoint about our Q1 financials:
- Title: "Q1 2024 Financial Review"
- Slide 1: Executive Summary with 3 key metrics
- Slide 2: Revenue Growth (with a trending_up icon)
- Slide 3: Customer Insights (with a person icon)
- Slide 4: Next Steps
```

### Example 2: Icon-Driven Deck

```
Make a 6-slide presentation about security:
- Each slide has a security-related icon
- Use "shield" for protection, "verified" for compliance
- Apply AmEx brand colors from color-tokens.json
```

### Example 3: Data Dashboard

```
Create a financial dashboard presentation with:
- Title slide with company logo area
- Three content slides with charts and icons
- Use analytics, trending_up, and trending_down icons
- Color-code positive/negative metrics
```

---

## Icon System

### Understanding the Icon Index

The `material-icons-index.json` maps icons by **use case**, not just by name:

```json
"person": {
  "use_cases": ["persona", "user", "human", "profile", "avatar", "pfp"],
  "keywords": ["single user", "individual", "profile picture"],
  "description": "Single person/user representation"
}
```

### Common Icon Use Cases

**People:**
- `person` → user, profile, persona
- `group` → team, audience
- `supervisor_account` → manager, admin

**Finance:**
- `trending_up` → growth, success
- `trending_down` → decline, risk
- `attach_money` → payment, cost

**Security:**
- `shield` → protection, security
- `lock` → encryption, secure
- `verified` → approved, trusted

**Technology:**
- `cloud` → storage, backup
- `computer` → device, system
- `api` → integration, development

### Icon Resolution Logic

When you request an icon, the system:

1. ✅ Searches by exact name (e.g., "person")
2. ✅ Searches by use case keyword (e.g., "user" → finds "person")
3. ✅ Searches by description keyword
4. ✅ Returns closest fuzzy match if needed

---

## Scripts Reference

### `create_pptx.py`

Main PowerPoint generation engine.

**Key Classes:**
- `PowerPointGenerator` — Main API for building presentations
- `SlideLayout` — Enum of supported slide types

**Key Methods:**
```python
generator = PowerPointGenerator(
    title="My Presentation",
    color_tokens_path="references/color-tokens.json",
    icons_index_path="references/material-icons-index.json"
)

generator.add_title_slide("Title", "Subtitle")
generator.add_content_slide("Section", ["bullet 1", "bullet 2"], icon="trending_up")
generator.add_two_column_slide("Comparison", "Left", [...], "Right", [...])
generator.add_section_slide("New Section")
generator.add_closing_slide("Thank You", "Call-to-action")

output_path = generator.save()
```

### `icon_manager.py`

Icon selection and resolution.

**Key Classes:**
- `IconManager` — Icon lookup and suggestions

**Key Methods:**
```python
mgr = IconManager("references/material-icons-index.json")

# Resolve by name or keyword
icon = mgr.resolve_icon("user")  # → "person"
icon = mgr.resolve_icon("growth")  # → "trending_up"

# Get all icons for a use case
security_icons = mgr.get_icon_by_use_case("security")

# Search icons
results = mgr.search_icons("financial", limit=10)

# Suggest icons for context
suggestions = mgr.suggest_icons("financial dashboard", count=5)
```

---

## Design Guidelines

### Typography
- **Titles:** Bold, 44–60pt
- **Headings:** Bold, 32pt
- **Body:** Regular, 18–20pt
- **Captions:** Regular, 14pt

### Spacing
- **Slide margins:** 0.5"
- **Between elements:** 0.25"–0.5"
- **Icon size:** 24pt–48pt (depends on usage)

### Color Usage
- **Primary:** Main titles, headers, backgrounds
- **Secondary:** Alternate sections, emphasis
- **Accent:** Call-to-action, highlights
- **Icons:** Match content color or primary brand

### Icon Best Practices
- Max 3–5 icons per slide
- Always pair icons with text
- Use consistent style (all filled or all outlined)
- Include alt text for accessibility

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Icons not rendering** | Verify icon name in `material-icons-index.json`; check SVG validity |
| **Colors look wrong** | Confirm `color-tokens.json` has valid hex codes |
| **Layout issues** | Adjust margins/positioning in `create_pptx.py`; check font sizes |
| **File won't save** | Ensure output directory exists; check file permissions |

---

## What's Next?

1. ✅ **Add color tokens** → Update `references/color-tokens.json`
2. ✅ **Add sample templates** → Place .pptx files in `assets/sample-ppts/`
3. ✅ **Create presentations** → Use the skill to build your first deck
4. 📊 **Iterate & refine** → Adjust colors, templates, and layouts as needed

---

## Support

### For Questions About...

- **Icon availability** → Check `material-icons-index.json` or search with the skill
- **Color/branding** → Edit `color-tokens.json` and reference sample templates
- **Presentation layout** → See SKILL.md for detailed layout options
- **Integration with code** → See scripts `create_pptx.py` and `icon_manager.py`

### Extending the Skill

The skill is designed to be extended:
- Add more icons to `material-icons-index.json`
- Add new slide layouts to `PowerPointGenerator`
- Create new icon search strategies in `IconManager`
- Add new color token categories to `color-tokens.json`

---

**Created:** May 15, 2024  
**Compatible with:** Claude Code, Copilot  
**Dependencies:** python-pptx  
**Icon Source:** Google Material Design  
