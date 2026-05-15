---
name: amex-pptx-maker
description: Create professional American Express PowerPoint presentations from markdown files. User provides a markdown file with content (filename.md) and the skill generates a polished, banker-grade .pptx automatically. Applies professional design system, colors, and typography without requiring any design specification. Use this skill whenever the user wants to make a .pptx from markdown content.
compatibility: python-pptx
---

# AmEx PowerPoint Presentation Maker

Generate professional, designer-quality PowerPoint presentations instantly. Provide your content in markdown, the skill handles all the design.

## How It Works

**You do:** Write content in a markdown file  
**Skill does:** Read it, intelligently parse it, apply professional design system, output .pptx

That's it.

## Markdown Format

Create a file (e.g., `content.md`) with this simple structure:

```markdown
# Presentation Title
Optional subtitle or tagline

## Slide 1 Title
Content for slide 1. Can be:
- Bullet points
- Or key: value pairs for metrics
- Or just text

## Slide 2 Title: Financial Results
Revenue: $2.3B (+15%)
Customers: 52M (+8%)
Net Income: $450M (+22%)

## Slide 3 Title: Why We Lead
- Security: Bank-grade protection
- Speed: Instant transactions
- Support: 24/7 availability

## Closing Thought
"The Future of Finance"
Digital. Secure. Personal.
```

The skill **automatically detects**:
- `# Title` = presentation title
- `## Heading` = slide heading
- `Key: Value (+/−percentage)` = financial metrics (auto-colored green/red)
- `- Bullet` = feature/benefit list
- Plain text = paragraph content
- `"Quote"` = impact/closing statement

## Example Usage

Just ask:
```
Create a PowerPoint from content.md
```

Or:
```
Make a presentation using Q2-results.md
```

The skill will:
1. Read your markdown file
2. Parse each section as a slide
3. Intelligently detect slide type (metrics, features, closing, etc.)
4. Apply the AmEx design system (colors, typography, spacing)
5. Auto-color metrics (green for growth +, red for decline −)
6. Output a professional presentation.pptx

## What Gets Applied Automatically

✅ **Professional colors** — AmEx blue (#0066CC), semantic greens/reds, premium cream background  
✅ **Typography hierarchy** — Inter font, proper sizes and weights per content type  
✅ **Spacing & rhythm** — Professional margins, padding, whitespace  
✅ **Visual hierarchy** — What's important looks important  
✅ **Semantic coloring** — +15% is green, −5% is red, CTAs are blue  
✅ **Component styling** — Metric boxes, feature cards, comparison panels, impact statements  
✅ **Material Design icons** — 5,000+ icons, indexed by use case (person = user/profile/avatar)  
✅ **Responsive layout** — Adapts to content length and type  

You describe what to say. The skill handles how it looks.

## Markdown Examples

### Example 1: Financial Report
```markdown
# Q2 2024 Financial Review

## Executive Summary
Strong growth across all segments with record customer acquisition.

## Metrics
Revenue: $2.3B (+15%)
Customers: 52M (+8%)
Net Income: $450M (+22%)
Cards: 18M (+12%)

## Market Position
- #1 in premium payments
- Fastest growing segment: fintech partnerships
- Largest decline: legacy in-person transactions

## Next Steps
Focus on digital expansion and mobile app features.
```

**Output:** Title slide → text slide → metrics slide (auto-colored) → features slide → closing slide

### Example 2: Product Features
```markdown
# Why Choose AmEx

## Security
- Bank-grade encryption
- Fraud detection 24/7
- Zero liability guarantee

## Convenience
- Mobile app access
- One-click payments
- Global acceptance

## Exclusive Benefits
- Premium travel lounge access
- Concierge service
- Rewards program

## Join Today
"The Most Trusted Payments Partner"
Available on all devices. Apply in 5 minutes.
```

**Output:** Title slide → 3 feature slides (one per bullet group) → impact closing slide

### Example 3: Comparison
```markdown
# Traditional vs AmEx

## Speed
Traditional: 3-5 business days
AmEx: Instant

## Mobile
Traditional: Limited
AmEx: Full-featured app

## Support
Traditional: Business hours only
AmEx: 24/7 available
```

**Output:** Title → comparison panel (Traditional vs AmEx side-by-side)

## What You Customize

Edit `references/DESIGN.md` to change:
- Brand colors (currently AmEx blue, green, red, cream)
- Typography (currently Inter font family)
- Spacing rules
- Component styling

Everything else flows from that one design file.

## Tips

- **Keep it simple:** Markdown is enough. No PowerPoint templates needed.
- **Metrics matter:** Use `Value (+percentage)` or `Value (−percentage)` for smart coloring.
- **Section hierarchy:** Each `##` becomes a slide. Each topic area = one slide.
- **Icons:** If you mention "growth", "security", "user", the skill will intelligently select appropriate Material Design icons.
- **Closing strong:** Save an impactful quote for the last slide.

## That's It

Write your content. Run the skill. Get a professional presentation. Done.
