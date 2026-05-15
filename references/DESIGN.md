# Design System Inspired by American Express

## 1. Visual Theme & Atmosphere

American Express presents itself as a trusted financial institution with editorial sophistication. The canvas is a neutral cream (`#FAFAF8`) — warm but professional, suggesting premium service paper rather than cold corporate white. On this canvas, everything that matters is shaped with generous radius: heroes carry 36-point corners, cards become pill-shaped, service images are cropped into circles, and buttons maintain 18-point consistency. The visual language emphasizes **trust through clear hierarchy** and **premium through generous whitespace**.

The dominant visual gesture is **professional constraint**: the AmEx blue (`#0066CC`) appears as a primary accent, never dominant. The second gesture is **circular portraiture with service labels** — similar to Mastercard, but less decorative and more functional. Service cards are framed by perfect circles paired with clear labeling and descriptive text. Decorative orbital lines are subtle teal arcs that suggest connection between services.

Typography is set in **Inter** (Google Fonts, excellent x-height and clarity) as the primary family. Headlines use weight 700 (bold) with slightly tighter tracking (-0.5%), creating confidence without excess. Body copy runs at weight 500, preserving readability on financial documents. The system — cream surfaces, pill shapes, circular portraits, teal orbital hints, dark-blue CTAs — feels simultaneously trustworthy (a 160+ year financial institution) and modern (clean, accessible design).

**Key Characteristics:**
- Neutral cream canvas (`#FAFAF8`) — warm, professional, never sterile
- Moderate border-radius as design language: 18px (buttons), 36px (cards), 1000px (pills); minimal sharp corners
- Circular image portraits with attached service labels and subtle teal orbital paths
- Blue primary CTAs (`#0066CC`) — the AmEx brand color, no orange consent confusion
- Neutral dark footer (`#1A1A1A`) with clear link hierarchy
- Generous whitespace and breathing room — financial content demands clarity
- Semantic colors for metrics: green for growth, red for caution, blue for primary

## 2. Color Palette & Roles

### Primary
- **AmEx Blue** (`#0066CC`): The signature AmEx blue — used for primary CTAs, headlines, navigation emphasis, and brand identity. Strong and trustworthy.
- **Ink Black** (`#1A1A1A`): The dark neutral for primary text, footer background, and secondary CTAs. Warm enough to avoid harshness.
- **Dark Teal** (`#004B87`): A darker blue shade used for secondary CTAs and active states.

### Secondary & Accent
- **Success Green** (`#00AA44`): Used for positive metrics, growth indicators, and confirmation states. Applied to "+15%" style metrics.
- **Caution Red** (`#D32F2F`): Used for declining metrics, risk indicators, and warnings. Applied to "-5%" style metrics.
- **Soft Teal** (`#4DBFBF`): A muted teal used for decorative orbital arcs and subtle accent lines. Never as a background.
- **Warm Accent** (`#FF8800`): A burnt orange reserved for special emphasis and premium callouts, distinct from consent colors.

### Surface & Background
- **Canvas Cream** (`#FAFAF8`): The default page/slide canvas. Warm, professional, readable. All content sits on this.
- **Lifted White** (`#FFFFFF`): One step lighter than canvas — used for raised sections, cards, and input backgrounds.
- **Soft Gray** (`#F0F0F0`): A cool-gray alternative surface for nested regions and secondary containers.

### Neutrals & Text
- **Ink Black** (`#1A1A1A`): Primary headline and body text color.
- **Charcoal** (`#333333`): Slightly softer black for text alternates and secondary headings.
- **Slate Gray** (`#666666`): Muted secondary text — labels, disabled states, fine print.
- **Light Gray** (`#CCCCCC`): Borders, dividers, and very muted labels.
- **Dust Taupe** (`#DDDDDD`): Placeholder text and extremely muted content.

### Semantic & Data
- **Positive** (`#00AA44`): Revenue growth, user gain, "up" indicators
- **Negative** (`#D32F2F`): Revenue decline, user loss, "down" indicators
- **Neutral** (`#4DBFBF`): No change or informational metrics
- **Primary CTA** (`#0066CC`): Learn more, proceed, explore
- **Secondary CTA** (`#004B87`): Alternate action, back, close

## 3. Typography Rules

### Font Family
- **Primary**: `Inter` (Google Fonts) — clean, readable, modern geometric sans. Every headline, body, button, and nav link.
- **Fallback stack**: `"Segoe UI", Arial, sans-serif` — system fonts that preserve readability.

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| H1 (hero) | 54px | 700 | 61px (1.13) | -0.5px (-0.9%) | Used in presentation title slides; tight leading for confidence |
| H2 (section) | 36px | 700 | 43px (1.19) | -0.3px (-0.8%) | Section headers and main content headings |
| H3 (card title) | 28px | 700 | 34px (1.21) | normal | Titles inside metric boxes and feature cards |
| H4 (subhead) | 20px | 700 | 24px (1.2) | normal | Card subtitles and label text |
| Body paragraph | 16px | 500 | 24px (1.5) | normal | Standard body copy — balanced readability for longer text |
| Label / Eyebrow | 14px | 600 | 16px | 0.4px (+3%) | Uppercase, paired with a color accent dot |
| Button label | 16px | 700 | 16px | -0.2px | Bold for CTA clarity |
| Small text / caption | 12px | 500 | 16px | normal | Footnotes, captions, metadata |

### Principles
- **Weight 700 on headlines** — creates strong visual hierarchy without a secondary typeface
- **Weight 500 on body** — maintains excellent readability for financial content (contracts, terms, metrics)
- **Tight letter-spacing on H1** (-0.9%) gives power and presence without aggression
- **One-font system** — consistency across all text elements
- **Line-height decreases with size** — H1 is 1.13, H3 is 1.21, body is 1.5. Tight display, comfortable reading.

## 4. Component Stylings

### Buttons

**Primary — AmEx Blue Pill**
- Background: AmEx Blue (`#0066CC`)
- Text: White (`#FFFFFF`)
- Border: none
- Radius: 18px
- Padding: 12px 32px
- Font: Inter 16px / weight 700
- Default: solid blue pill on cream canvas
- Hover: darker blue (`#0052A3`)
- Active: `#004B87` (dark teal)
- Use for: all primary CTAs ("Learn More", "Explore", "Continue")

**Secondary — Outlined Blue**
- Background: White (`#FFFFFF`)
- Text: AmEx Blue (`#0066CC`)
- Border: 2px solid AmEx Blue
- Radius: 18px
- Padding: 10px 30px
- Font: Inter 16px / weight 700
- Default: white-on-cream pill with blue outline
- Hover: light blue background
- Use for: secondary actions paired with a primary, or standalone utility CTAs

**Metric Box** (for positive metrics)
- Background: White (`#FFFFFF`)
- Text: Ink Black (`#1A1A1A`)
- Accent border: 3px solid Success Green (`#00AA44`) on left edge
- Radius: 8px
- Padding: 20px
- Font: Inter 28px / weight 700 for the metric value
- Use for: financial metrics, growth indicators, positive data

**Metric Box** (for negative/caution metrics)
- Same as above, but accent border: 3px solid Caution Red (`#D32F2F`)
- Use for: declining metrics, risk indicators

### Cards & Containers

**Hero Media Frame (Stadium)**
- Background: Dark overlay or imagery
- Radius: 36px all corners
- Width: full viewport minus gutters
- Height: 60% of viewport or 540px minimum
- Shadow: subtle (`rgba(0, 0, 0, 0.08) 0px 8px 24px`)
- Use for: title slide backgrounds, featured content

**Service / Feature Portrait Card**
- Shape: Perfect circle (radius 50%)
- Diameter: 260–300px desktop; 180–220px mobile
- Image crop: square source, cropped to circle
- Border: 2px solid Soft Teal (`#4DBFBF`)
- Label below: H4 (20px / weight 700) in Ink Black
- Descriptive text below: Body (16px / weight 500) in Slate Gray
- Shadow: none (sits directly on canvas)

**Comparison Panel**
- Background: Lifted White (`#FFFFFF`)
- Radius: 36px corners
- Two-column layout: left column (traditional), right column (AmEx)
- Divider: 1px solid Light Gray (`#CCCCCC`)
- Padding: 40px per column
- Checkmarks/X: Success Green for checkmarks, Caution Red for gaps
- Use for: side-by-side feature comparisons, traditional vs modern

**Impact Statement**
- Radius: 36px corners
- Background: AmEx Blue (`#0066CC`) or Lifted White
- Text color: White (if blue bg) or Ink Black (if white bg)
- Padding: 60px horizontal, 40px vertical
- Font: H2 (36px / 700) centered, followed by H4 (20px / 600) subtext
- Optional CTA: Primary button below text
- Use for: closing statements, key brand messages, calls-to-action

### Inputs & Forms
- Background: White (`#FFFFFF`)
- Border: 1px solid Light Gray (`#CCCCCC`)
- Radius: 8px
- Padding: 12px 16px
- Font: Body (16px / weight 500)
- Focus: border color changes to AmEx Blue, subtle shadow `0px 0px 0px 3px rgba(0, 102, 204, 0.1)`
- Placeholder: Dust Taupe (`#DDDDDD`)

### Navigation
- Background: White (`#FFFFFF`)
- Text: Ink Black (`#1A1A1A`)
- Active link: AmEx Blue (`#0066CC`)
- Radius: 1000px (pill shape) for main nav container
- Padding: 12px 24px per link
- Shadow: subtle lift (`rgba(0, 0, 0, 0.04) 0px 2px 8px`)
- Font: 16px / weight 700

## 5. Layout Principles

### Spacing System
- **Base unit**: 8px
- **Scale**: 8 / 16 / 24 / 32 / 40 / 48 / 64 / 80 / 96 (multiples of 8)
- **Section vertical padding**: 80–96px between major sections on slides; 48–64px on mobile
- **Card internal padding**: 32px on desktop, 24px on mobile
- **Gutters**: 40–48px from viewport edges

### Slide Layout Grid
- **Max content width**: 1200px centered
- **Column pattern**: Flexible — 1-up (title, impact), 2-up (metrics side-by-side), 3-up (feature grid), or asymmetric (title on left, portrait on right)
- **Metric grid**: typically 2×2 or 3×1 (4 metrics or 3 metrics per slide)

### Whitespace Philosophy
Generous whitespace signals premium service. A typical metrics slide:
- Small heading at top (12% of slide height)
- Empty space (8% of slide height)
- 4 metric boxes arranged 2×2 (60% of slide height)
- Footer area (20% of slide height)

This breathing room tells the viewer "this information is important; take your time."

### Border Radius Scale

| Radius | Use |
|--------|-----|
| 4–6px | Tiny elements, toggles, checkboxes |
| 8px | Form inputs, small cards, tags |
| 18px | Primary and secondary CTAs, modest cards |
| 36px | Hero media frames, large section containers |
| 50% | Circular portraits, icon-only buttons |
| 1000px | Full pill shapes — navigation, large buttons |

This scale is deliberate: we avoid 12–16px (which looks dated). We use either small (≤8), medium (18/36), or full-pill (1000px).

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| 0 | No shadow | Default — most surfaces sit on canvas |
| 1 | `rgba(0, 0, 0, 0.04) 0px 2px 8px` | Floating nav, subtle lift |
| 2 | `rgba(0, 0, 0, 0.08) 0px 8px 24px` | Cards, elevated elements |
| 3 | `rgba(0, 0, 0, 0.12) 0px 16px 40px` | Modals, dramatic elevation |

### Shadow Philosophy
Shadows create **atmospheric layering**, not harsh drop effects. Large spread radius (24–40px) with low opacity (4–12%) creates a soft halo that suggests elevation without visual weight.

## 7. Do's and Don'ts

### Do
- ✅ Use Canvas Cream (`#FAFAF8`) as default slide background
- ✅ Use AmEx Blue (`#0066CC`) for all primary CTAs and accents
- ✅ Apply Success Green to "+" metrics and Caution Red to "-" metrics automatically
- ✅ Mask service imagery as perfect circles, not rounded rectangles
- ✅ Keep headlines in weight 700 Inter for clarity
- ✅ Use weight 500 Inter for body paragraphs
- ✅ Maintain 18px button radius — consistent and trustworthy
- ✅ Build page rhythm from whitespace, not dense layouts
- ✅ Use three surface tones: canvas cream → lifted white → ink footer
- ✅ Use subtle Soft Teal arcs between service cards

### Don't
- ❌ Don't use pure white as a slide background — cream establishes warmth
- ❌ Don't use inconsistent border radius — pick 18, 36, or 1000px
- ❌ Don't mix typefaces — Inter is the system
- ❌ Don't use orange for anything except premium callouts (never for compliance/consent)
- ❌ Don't crowd content — generous whitespace is a feature, not waste
- ❌ Don't use hard shadows — all elevation is soft and diffuse
- ❌ Don't use all caps except for labels and metadata
- ❌ Don't place portraits on a grid — asymmetric placement feels more premium
- ❌ Don't use weight <500 for body copy — readability matters

## 8. Responsive Behavior

### Breakpoints
- **Mobile** (≤767px): Single-column layouts; 2-up metric grids become 1-up; portrait size shrinks to ~180px; hero headlines drop from 54px to ~32px
- **Tablet** (768–1023px): 2-column layouts possible; 2×2 metric grids maintained; portraits ~240px; hero headlines ~40px
- **Desktop** (≥1024px): Full featured layouts; asymmetric grids possible; portraits 260–300px; hero headlines 54px
- **Wide** (≥1440px): Content max-width caps at 1200px; gutters grow symmetrically

### Collapsing Strategy
- **Metric grids**: 2×2 (desktop) → 2×1 (tablet) → 1×1 (mobile)
- **Comparison panels**: 2-column (desktop) → stacked (mobile)
- **Navigation**: full nav (desktop) → hamburger menu (mobile)
- **Spacing**: section padding compresses from 96px to 48px on mobile
- **Typography**: H1 drops from 54px → 40px (tablet) → 32px (mobile) with proportional line-height

## 9. Agent Prompt Guide

### Quick Color Reference
- **Primary CTA**: "AmEx Blue (`#0066CC`) — the brand color for buttons and primary accents"
- **Background**: "Canvas Cream (`#FAFAF8`) — warm, professional slide canvas"
- **Lifted surface**: "Lifted White (`#FFFFFF`) — for raised cards and containers"
- **Success metric**: "Success Green (`#00AA44`) — for growth, positive metrics, checkmarks"
- **Caution metric**: "Caution Red (`#D32F2F`) — for decline, risk, negative metrics"
- **Heading text**: "Ink Black (`#1A1A1A`) — primary text color"
- **Body text**: "Ink Black (`#1A1A1A`) at weight 500 Inter"
- **Muted text**: "Slate Gray (`#666666`) — secondary labels and fine print"
- **Accent arc**: "Soft Teal (`#4DBFBF`) — subtle decorative lines between service cards"
- **Footer**: "Ink Black (`#1A1A1A`) background with White text"

### Example Component Prompts
- "Create a metric box showing Revenue: $2.3B (+15%). Use white background, Ink Black text for the label and value, with a 3px left border in Success Green (`#00AA44`). Set the value in 28px bold Inter, the label in 16px regular Inter below it. Apply 20px padding and 8px border-radius."
- "Design a primary CTA button: AmEx Blue (`#0066CC`) background, white text, 18px border-radius, 12px vertical and 32px horizontal padding, Inter font at 16px weight 700. Include hover state with darker blue (`#0052A3`)."
- "Build a 4-metric slide layout: 2×2 grid of metric boxes, centered on the slide. Each box has a metric value (36px bold), a label (16px regular), a color-coded left border (3px, green for positive metrics, red for declining ones), and 20px padding. Spacing between boxes is 24px. The entire grid is centered with 40px margins on left/right."
- "Create a comparison panel: white background, 36px rounded corners, split into two equal columns with a 1px divider. Left column header 'Traditional', right column header 'American Express'. List 5 features below each, with checkmarks (`✓`) in green for AmEx, X's (`✗`) in red for traditional. Use 40px padding per column, 20px spacing between items."
- "Design a hero media frame: 36px border-radius all corners, full viewport width with 40px gutters on sides, 60% viewport height minimum. Apply a subtle shadow `rgba(0, 0, 0, 0.08) 0px 8px 24px`. Place it directly on Canvas Cream background."

### Iteration Guide
When refining slides generated with this design system:
1. Focus on color choices first — green for gains, red for risks, blue for CTAs
2. Reference specific color names AND hex codes
3. Use "warm, professional" and "premium through whitespace" as design principles
4. When sizing type, match the hierarchy table (H1=54px, H3=28px, body=16px, etc.)
5. Default backgrounds to Canvas Cream (`#FAFAF8`), never pure white
6. All metric values automatically get semantic coloring based on sign (+/−)

## 10. Design System Source

This system was adapted from the [awesome-design-md Mastercard template](https://github.com/VoltAgent/awesome-design-md) and customized for American Express brand identity and financial presentation context.
