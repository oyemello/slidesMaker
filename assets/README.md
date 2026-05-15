# AmEx PowerPoint Maker Assets

This directory contains design reference files and templates for the PowerPoint generation skill.

## Folders

### `sample-ppts/`
Place American Express PowerPoint template files here. These serve as style references for the generation system.

**Recommended templates to add:**
- `amex-standard.pptx` — Default presentation template
- `amex-data-dashboard.pptx` — Data visualization template
- `amex-pitch-deck.pptx` — Sales/pitch template
- `amex-report.pptx` — Report/analysis template

When sample PPTs are added, the skill will:
- Extract color schemes
- Analyze typography and fonts
- Study layout patterns
- Reference design standards for new presentations

## Usage

1. Create or export your American Express branded PowerPoint templates
2. Save them in this `sample-ppts/` folder
3. The skill will automatically analyze them when generating new presentations
4. All new presentations will maintain design consistency with these samples

## Best Practices

- **One template per use case** — Different templates for different presentation types
- **Include all slide types** — Title, content, data, closing slides
- **Brand consistency** — Ensure templates reflect current AmEx branding
- **Update regularly** — Refresh templates when brand guidelines change

## File Naming Convention

Use clear, descriptive names:
```
amex-[purpose]-[version].pptx

Examples:
- amex-standard-v1.pptx
- amex-data-v2.pptx
- amex-pitch-v1.pptx
```

This makes it easy to identify and update templates over time.
