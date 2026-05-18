---
name: amex-pptx-maker
description: Create professional American Express PowerPoint presentations from markdown files using pre-designed infographic components. User writes content in markdown, adds .pptx or .odp infographic templates to references/components/, and the skill generates a polished .pptx automatically. No design work needed—just content + components.
compatibility: python-pptx, LibreOffice (for ODP conversion)
---

# AmEx PowerPoint Presentation Maker

Generate professional, designer-quality presentations from markdown + infographic components.

**You provide:** Content (markdown) + Components (pre-designed .pptx/.odp files)  
**Skill does:** Parse content, load components, fill with data, output .pptx

## How It Works

```
content.md (your content)
    ↓
    ├→ Parse: "4 metrics with +percentages" → need metric-grid component
    ├→ Load: references/components/metric-grid-4.pptx
    ├→ Clone: Copy the professionally-designed slide
    ├→ Fill: Update with your Revenue, Customers, etc. values
    └→ Result: Professional metric infographic in presentation
```

## Component-Based Design

Instead of generating layouts, **reuse pre-designed infographic components**:

```
references/components/
├── metric-grid-4.pptx          # 2×2 metric boxes (designed once, reused always)
├── metric-grid-3.pptx          # 3-metric layout
├── comparison-panel.pptx       # Traditional vs AmEx split layout
├── feature-grid-3.pptx         # 3-column feature cards
├── impact-statement.pptx       # Bold closing statement
└── icon-grid.pptx              # Icon-based grid

+ Supports .odp (LibreOffice) format—automatically converted to .pptx
```

**Why this works:**
- Designers create pixel-perfect infographics once in PowerPoint/LibreOffice
- LLM clones them and fills with your data
- Like React components: define once, reuse with different props
- Update a component, all presentations using it improve automatically

## Markdown Format

Create `content.md` with this structure:

```markdown
# Presentation Title
Optional subtitle

## Slide 1 Title
Regular text content

## Metrics Section
Revenue: $2.3B (+15%)
Customers: 52M (+8%)
Net Income: $450M (+22%)
Cards: 18M (+12%)

## Features Section
- Security: Bank-grade protection
- Speed: Instant transactions
- Support: 24/7 support

## Comparison
Traditional: Limited
AmEx: Full-featured

Traditional: 3-5 days
AmEx: Instant

## Closing
"The Future of Finance"
Digital. Secure. Personal.
```

The skill detects:
- `Key: Value (+/−%)` → metrics slide (loads metric-grid component)
- `- Title: Description` → features slide (loads feature-grid component)
- `Traditional: ... AmEx: ...` → comparison slide (loads comparison-panel)
- `"Quote"` → impact statement (loads impact-statement)
- Text only → text slide (no component needed)

## Workflow

### 1. Create Your Components (One-Time)

In PowerPoint or LibreOffice:
- Design a 2×2 metric grid → save as `metric-grid-4.pptx`
- Design a feature card layout → save as `feature-grid-3.pptx`
- Design a comparison panel → save as `comparison-panel.pptx`
- Add them to `references/components/`

The skill will:
- Use `.pptx` files directly
- Auto-convert `.odp` files to `.pptx`

### 2. Write Your Content

Create `content.md` with your presentation narrative. Don't worry about design.

### 3. Run the Skill

```
Create a PowerPoint from content.md
```

The skill:
1. Parses markdown
2. Detects each slide type
3. Loads matching component
4. Clones it into the presentation
5. Fills with your content
6. Outputs presentation.pptx

## Example: Financial Deck

**content.md:**
```markdown
# Q2 2024 Results

## Financial Metrics
Revenue: $2.3B (+15%)
Customers: 52M (+8%)
Net Income: $450M (+22%)
Cards: 18M (+12%)

## Product Strengths
- Security: Bank-grade protection
- Mobile: Full-featured app
- Support: 24/7 availability

## Closing
"Leading the Digital Revolution"
Trust. Speed. Innovation.
```

**What happens:**
1. Skill loads `metric-grid-4.pptx` → copies slide
2. Fills with $2.3B, +15%, etc.
3. Loads `feature-grid-3.pptx` → copies slide
4. Fills with Security, Mobile, Support
5. Creates simple closing slide with quote
6. Output: Professional presentation in 10 seconds

## Tips

- **Design once, use many times:** Create components in PowerPoint/LibreOffice, reuse across all presentations
- **ODP support:** You can use LibreOffice presentations (.odp)—they're auto-converted
- **Keep content simple:** Markdown is all you need
- **Metrics format:** Always use `Value (+/−percentage)` for semantic coloring
- **Features format:** `- Title: Description` for paired labels

## File Structure

```
pptMaker/
├── content.md                    ← Your content (you write this)
├── output.pptx                   ← Generated presentation
└── references/
    └── components/
        ├── metric-grid-4.pptx    ← Component (you design in PowerPoint)
        ├── feature-grid-3.pptx   ← Component
        ├── comparison-panel.pptx ← Component
        ├── impact-statement.odp  ← Or use LibreOffice format!
        └── ...
```

## That's It

1. Design components in PowerPoint/LibreOffice
2. Write content in markdown
3. Run the skill
4. Get professional presentation
