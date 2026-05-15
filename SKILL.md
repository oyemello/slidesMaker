---
name: amex-pptx-maker
description: Create professional American Express PowerPoint presentations with Google Material Design icons. Use this skill whenever the user wants to make a .pptx file, build PowerPoint presentations, create slides, or needs to design presentations with Material Design icons. Works seamlessly with Claude Code and Copilot. Include this skill for any presentation creation task, AmEx branding needs, slide design, or icon-based visual content.
compatibility: python-pptx, requests (for icon rendering)
---

# AmEx PowerPoint Presentation Maker

Create professional, branded PowerPoint presentations with integrated Google Material Design icons. This skill provides comprehensive icon indexing by use case, branded styling via color tokens, and full presentation generation capabilities.

## When to Use This Skill

- Creating PowerPoint presentations (.pptx files)
- Building American Express-branded slide decks
- Designing presentations with Material Design icons
- Creating visual presentations with icon-based layouts
- Generating multi-slide presentations with consistent branding
- Designing dashboards, reports, or data visualizations in PowerPoint

## Core Capabilities

### 1. **Full PowerPoint Creation**
Generate complete, professionally formatted .pptx files with:
- Multiple slide types (title, content, two-column, icon grid, etc.)
- Consistent branding and styling
- Automatic layout and spacing
- Text formatting and typography

### 2. **Material Design Icon Integration**
- Access to 5,000+ Google Material Design icons
- Icons indexed by use case (not just name)
- Smart icon selection and embedding
- SVG-to-PowerPoint conversion
- Icons as bullet points, callouts, or design elements

### 3. **Branded Color System**
- Uses `color-tokens.json` for consistent color palette
- Support for primary, secondary, accent, and neutral colors
- Automatic color application to slides, icons, and text
- AmEx brand compliance

### 4. **Icon Indexing System**
Icons are indexed by **use case keywords**, not just name. Examples:

| Icon Name | Primary Use Case | Secondary Keywords |
|-----------|------------------|-------------------|
| `person` | Persona | user, human, profile, avatar, PFP |
| `business` | Organization | company, enterprise, corporate, team |
| `trending_up` | Growth | increase, success, performance, metrics |
| `shield` | Security | protection, compliance, risk, safety |
| `cloud` | Cloud | storage, backup, network, data |

This enables smart icon selection: ask for an icon for "user profiles" and the system understands to use `person` or `person_outline`.

---

## How to Use

### Basic Workflow

```
1. User provides presentation details:
   - Title and subtitle
   - Slide content (text, bullets, data)
   - Requested icons (by use case or name)
   - Optional: design preferences, color overrides

2. Script processes request:
   - Loads color-tokens.json for branding
   - Resolves icon keywords to Material icon names
   - Builds PowerPoint structure
   - Embeds icons as SVG objects
   - Applies formatting and layout

3. Output: professional .pptx file ready to use
```

### Example Prompts

**Example 1: Simple deck with icons**
```
Create a 5-slide PowerPoint about financial planning:
- Slide 1: Title - "Your Financial Journey"
- Slide 2: "Budgeting Basics" with a budget icon
- Slide 3: "Saving Strategies" with a piggy bank icon
- Slide 4: "Investment Growth" with a trending up icon
- Slide 5: "Get Started" with a checkmark icon
```

**Example 2: Data-driven presentation**
```
Make a quarterly business review presentation:
- Use the "business" and "analytics" themed icons
- Apply AmEx brand colors (from color-tokens.json)
- 8 slides with metrics, trends, and callouts
- Each section marked with appropriate icons
```

**Example 3: Complex multi-column layout**
```
Create a product comparison slide with:
- Three columns for three products
- Security icons for each product feature
- Color-coded risk levels
- Footer with contact information
```

---

## Configuration Files

### color-tokens.json
**Location:** `references/color-tokens.json`

Define your brand color palette:
```json
{
  "primary": "#0066CC",
  "secondary": "#FF6600",
  "accent": "#00AA44",
  "neutral": {
    "dark": "#1A1A1A",
    "light": "#F5F5F5"
  },
  "semantic": {
    "success": "#00AA44",
    "warning": "#FFAA00",
    "danger": "#DD0000"
  }
}
```

**Note:** You will add this file. Until then, defaults are used.

### Sample PowerPoint Templates
**Location:** `assets/sample-ppts/`

Place reference PowerPoint files here. The skill will:
- Analyze their design system
- Extract color schemes, fonts, and layout patterns
- Use them as style guides for new presentations

Add samples like:
- `amex-standard-template.pptx`
- `amex-data-template.pptx`
- `amex-pitch-template.pptx`

---

## Icon System

### Accessing Icons

The skill includes a comprehensive **material-icons-index.json** that maps:
- **Icon name** → Material Design icon identifier
- **Use cases** → Contextual keywords
- **Categories** → Visual organization
- **Variants** → filled, outlined, rounded, sharp

### Icon Selection Logic

When you request an icon:
1. Search by exact name (e.g., "person")
2. Search by use case keyword (e.g., "user" → finds "person")
3. Return closest match or suggest alternatives

### Common Icon Use Cases

**People & Personas:**
- person, person_outline, group, groups, supervisor_account, face, contact_page

**Business & Enterprise:**
- business, domain, apartment, apartment, corporate_fare, storefront, factory

**Finance & Money:**
- attach_money, currency_exchange, trending_up, trending_down, show_chart, analytics

**Security & Compliance:**
- shield, lock, security, verified, policy, rule, law

**Data & Analytics:**
- analytics, data_usage, assessment, insights, auto_graph, leaderboard

**Communication:**
- mail, message, chat, forum, call, contact_support, notifications

**Action & Status:**
- check_circle, cancel, pending, schedule, check, done, close

**Technology & Cloud:**
- cloud, cloud_upload, storage, memory, computer, devices, router

---

## Script Reference

### `scripts/create_pptx.py`

Main script for PowerPoint creation.

**Inputs:**
- presentation_config (dict): Title, slides, colors, icons
- output_path (str): Where to save the .pptx

**Outputs:**
- .pptx file

**Usage within skill:**
```python
from scripts.create_pptx import PowerPointGenerator

generator = PowerPointGenerator(
    title="My Presentation",
    color_tokens_path="references/color-tokens.json",
    icons_index_path="references/material-icons-index.json"
)

generator.add_title_slide("Title", "Subtitle")
generator.add_content_slide("Section", ["bullet 1", "bullet 2"], icon="trending_up")
generator.add_icon_grid_slide(icons=["person", "business", "shield"])
generator.save("output.pptx")
```

### `scripts/icon_manager.py`

Icon resolution and embedding.

**Functions:**
- `resolve_icon(keyword)` → returns Material icon name
- `get_icon_by_use_case(use_case)` → returns icons matching use case
- `embed_icon_in_slide(slide, icon_name, position, size)` → adds icon to slide

---

## Style Guidelines (Reference)

### Typography
- Titles: Bold, 44pt
- Headings: Bold, 32pt
- Body: Regular, 18pt
- Captions: Regular, 14pt

### Spacing
- Slide margins: 0.5"
- Between elements: 0.25"–0.5"
- Icon size: 24pt–48pt depending on usage

### Colors
- Text on light bg: #1A1A1A (dark)
- Text on dark bg: #F5F5F5 (light)
- Accent elements: from color-tokens.json
- Icons: match content color or primary brand

### Layout Patterns
- Title slide: centered, large icon
- Content: icon + text (left-right or top-bottom)
- Data: icon callouts with metrics
- Closing: centered icon + call-to-action

---

## Tips & Best Practices

1. **Icon Density:** 3–5 icons per slide max. More icons = visual clutter.
2. **Icon Sizing:** 32pt for inline, 48pt for callouts, 64pt+ for hero slides.
3. **Icon Color:** Use primary or secondary from color tokens. Avoid too many colors.
4. **Text + Icons:** Always pair icons with descriptive text.
5. **Consistency:** Use the same icon style throughout (all filled or all outlined).
6. **Accessibility:** Include alt text for icons; don't rely on icon alone to convey meaning.

---

## Workflow for AmEx Presentations

### Step 1: Define Your Message
- Slide count
- Key sections
- Main call-to-action

### Step 2: Select Icons
- Use the keyword index to find relevant icons
- Match icons to slide themes
- Ensure visual consistency

### Step 3: Apply Branding
- Reference color-tokens.json
- Use AmEx fonts (if added to samples)
- Follow layout patterns from sample PPTs

### Step 4: Generate & Review
- Script creates .pptx
- You review for content and layout
- Refine as needed

---

## Examples in `assets/sample-ppts/`

Once you add sample PowerPoint files, they'll be analyzed for:
- Color schemes
- Font selections
- Slide layout patterns
- Icon usage conventions

This helps the skill maintain visual consistency across all generated presentations.

---

## Troubleshooting

**Icons not rendering:**
- Verify icon name in material-icons-index.json
- Check icon variant (filled vs. outlined)
- Ensure SVG is valid

**Colors not applied:**
- Verify color-tokens.json exists and is valid JSON
- Check hex color format (#RRGGBB)
- Confirm token name matches script reference

**Slide layout issues:**
- Adjust margins in script (default 0.5")
- Verify element positioning coordinates
- Check font sizes match content length

---

## Next Steps

1. **Add `color-tokens.json`** to `references/` with your brand colors
2. **Add sample .pptx files** to `assets/sample-ppts/` for style reference
3. **Create presentations** by describing what you need
4. **Iterate & refine** based on output

The skill will automatically use these resources to maintain consistency.
