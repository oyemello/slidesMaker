#!/usr/bin/env python3
"""
AmEx Design System Parser & Applier
Reads DESIGN.md and extracts design rules for intelligent application to presentations.
"""

import re
from dataclasses import dataclass
from typing import Dict, Optional, List, Tuple
from pathlib import Path


@dataclass
class ColorToken:
    """Represents a color in the design system"""
    name: str
    hex_code: str
    role: str  # "primary", "secondary", "surface", "text", "semantic"
    usage: str  # Human-readable usage description

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """Convert hex to RGB tuple"""
        hex_clean = self.hex_code.lstrip('#')
        return tuple(int(hex_clean[i:i+2], 16) for i in (0, 2, 4))


@dataclass
class TypographyRule:
    """Represents a typography rule from the design system"""
    name: str  # "H1", "H2", "body", etc.
    size: int  # in pixels
    weight: int  # 400, 500, 700, etc.
    line_height: str  # "1.13", "24px", etc.
    letter_spacing: str  # "-0.5px", "normal", etc.
    notes: str


class DesignSystemReader:
    """Parses DESIGN.md and extracts design rules"""

    def __init__(self, design_md_path: str):
        """
        Initialize the reader and parse the design file.

        Args:
            design_md_path: Path to DESIGN.md
        """
        self.path = Path(design_md_path)
        self.content = self.path.read_text() if self.path.exists() else ""

        # Extracted data
        self.colors: Dict[str, ColorToken] = {}
        self.typography: Dict[str, TypographyRule] = {}

        self._parse_colors()
        self._parse_typography()

    def _parse_colors(self):
        """Extract color palette from DESIGN.md"""
        # Look for color definitions in the format: "Name (`#HEX`): Description"
        pattern = r'\*\*([^`]+)\*\*\s*\(`([#0-9A-Fa-f]+)`\):\s*(.+?)(?=\n-|\n\*\*|$)'

        matches = re.findall(pattern, self.content, re.MULTILINE)
        for name, hex_code, description in matches:
            # Determine role based on section and content
            role = self._determine_color_role(name, description)

            self.colors[name.lower().replace(' ', '_')] = ColorToken(
                name=name,
                hex_code=hex_code,
                role=role,
                usage=description.strip()
            )

    def _determine_color_role(self, name: str, description: str) -> str:
        """Infer color role from name and description"""
        name_lower = name.lower()
        desc_lower = description.lower()

        if any(x in name_lower for x in ['amex', 'blue', 'primary', 'dark teal']):
            return "primary"
        elif any(x in name_lower for x in ['success', 'green', 'positive']):
            return "semantic"
        elif any(x in name_lower for x in ['red', 'caution', 'negative', 'danger']):
            return "semantic"
        elif any(x in desc_lower for x in ['background', 'canvas', 'surface']):
            return "surface"
        elif any(x in name_lower for x in ['gray', 'black', 'text', 'ink', 'slate', 'charcoal']):
            return "text"
        elif any(x in name_lower for x in ['teal', 'accent', 'warm']):
            return "secondary"
        else:
            return "neutral"

    def _parse_typography(self):
        """Extract typography rules from the hierarchy table"""
        # Find the typography table
        table_pattern = r'\| H\d|body|label|button|caption.*?\|.*?\|(?:\n\|[^\n]+\|)*'

        # Simpler approach: extract lines matching the pattern
        lines = self.content.split('\n')
        in_table = False

        for line in lines:
            if '| Role' in line:
                in_table = True
                continue
            if in_table and line.strip().startswith('|'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 6 and parts[1]:
                    # parts: ['', 'role', 'size', 'weight', 'lineheight', 'letterspacing', 'notes', '']
                    role = parts[1]
                    if role not in ['Role', '---']:
                        try:
                            size = int(parts[2].replace('px', ''))
                            weight = int(parts[3])
                            line_height = parts[4]
                            letter_spacing = parts[5]
                            notes = parts[6] if len(parts) > 6 else ""

                            self.typography[role.lower()] = TypographyRule(
                                name=role,
                                size=size,
                                weight=weight,
                                line_height=line_height,
                                letter_spacing=letter_spacing,
                                notes=notes
                            )
                        except (ValueError, IndexError):
                            continue
            elif in_table and not line.strip().startswith('|'):
                in_table = False

    def get_color(self, color_key: str) -> Optional[ColorToken]:
        """Retrieve a color by key"""
        return self.colors.get(color_key.lower().replace(' ', '_'))

    def get_color_by_role(self, role: str) -> List[ColorToken]:
        """Get all colors with a specific role"""
        return [c for c in self.colors.values() if c.role == role]

    def get_typography(self, type_key: str) -> Optional[TypographyRule]:
        """Retrieve typography rule by key"""
        return self.typography.get(type_key.lower())

    def suggest_color_for_context(self, context: str) -> Optional[ColorToken]:
        """
        Intelligently suggest a color based on context.

        Args:
            context: A string like "growth", "revenue +15%", "user decline", etc.

        Returns:
            A ColorToken or None
        """
        context_lower = context.lower()

        # Detect semantic meaning from text
        if any(x in context_lower for x in ['+', 'growth', 'increase', 'gain', 'up']):
            return self.get_color('success_green')
        elif any(x in context_lower for x in ['-', 'decline', 'decrease', 'loss', 'down']):
            return self.get_color('caution_red')
        elif any(x in context_lower for x in ['primary', 'cta', 'action', 'button']):
            return self.get_color('amex_blue')
        else:
            return self.get_color('ink_black')


class DesignApplier:
    """Applies design system rules when generating presentations"""

    def __init__(self, reader: DesignSystemReader):
        """
        Initialize the applier with a design system reader.

        Args:
            reader: A DesignSystemReader instance
        """
        self.reader = reader

    def apply_heading_style(self, heading_level: str) -> Dict:
        """
        Get styled properties for a heading.

        Args:
            heading_level: "h1", "h2", "h3", "h4", etc.

        Returns:
            Dict with font_size, font_weight, line_height, letter_spacing, color
        """
        typo = self.reader.get_typography(heading_level)
        color = self.reader.get_color('ink_black')

        if not typo:
            # Default H2 style
            typo = self.reader.get_typography('h2') or TypographyRule(
                name="h2", size=36, weight=700, line_height="43px",
                letter_spacing="-0.3px", notes=""
            )

        return {
            'font_size': typo.size,
            'font_weight': typo.weight,
            'line_height': typo.line_height,
            'letter_spacing': typo.letter_spacing,
            'font_name': 'Inter',
            'color': color.hex_code if color else '#1A1A1A'
        }

    def apply_body_style(self) -> Dict:
        """Get styled properties for body text"""
        typo = self.reader.get_typography('body paragraph')
        color = self.reader.get_color('ink_black')

        if not typo:
            typo = TypographyRule(
                name="body", size=16, weight=500, line_height="24px",
                letter_spacing="normal", notes=""
            )

        return {
            'font_size': typo.size,
            'font_weight': typo.weight,
            'line_height': typo.line_height,
            'letter_spacing': typo.letter_spacing,
            'font_name': 'Inter',
            'color': color.hex_code if color else '#1A1A1A'
        }

    def get_cta_button_style(self, button_type: str = 'primary') -> Dict:
        """
        Get styled properties for a CTA button.

        Args:
            button_type: 'primary' (blue), 'secondary' (outline), 'metric' (data box)

        Returns:
            Dict with background, text_color, border, radius, padding, etc.
        """
        if button_type == 'primary':
            return {
                'background_color': '#0066CC',  # AmEx Blue
                'text_color': '#FFFFFF',  # White
                'border': 'none',
                'border_radius': 18,
                'padding': {'top': 12, 'right': 32, 'bottom': 12, 'left': 32},
                'font_size': 16,
                'font_weight': 700,
            }
        elif button_type == 'secondary':
            return {
                'background_color': '#FFFFFF',  # White
                'text_color': '#0066CC',  # AmEx Blue
                'border': '2px solid #0066CC',
                'border_radius': 18,
                'padding': {'top': 10, 'right': 30, 'bottom': 10, 'left': 30},
                'font_size': 16,
                'font_weight': 700,
            }
        elif button_type == 'metric':
            return {
                'background_color': '#FFFFFF',
                'text_color': '#1A1A1A',
                'border': 'none',
                'border_left': '3px solid',  # Color set by semantic context
                'border_radius': 8,
                'padding': {'top': 20, 'right': 20, 'bottom': 20, 'left': 20},
                'font_size': 28,
                'font_weight': 700,
            }

    def get_metric_box_style(self, metric_value: str) -> Dict:
        """
        Get complete style for a metric box, including semantic color.

        Args:
            metric_value: The metric string like "+15%" or "-5%" or "500"

        Returns:
            Dict with all styling including color-coded border
        """
        style = self.get_cta_button_style('metric')

        # Determine semantic color based on the value
        color = self.reader.suggest_color_for_context(metric_value)
        if color:
            style['border_left'] = f"3px solid {color.hex_code}"

        return style

    def get_comparison_styles(self) -> Dict:
        """Get styling for comparison panels (traditional vs AmEx)"""
        return {
            'background_color': '#FFFFFF',
            'border_radius': 36,
            'padding': {'all': 40},
            'divider_color': '#CCCCCC',
            'checkmark_color': '#00AA44',  # Success Green
            'x_color': '#D32F2F',  # Caution Red
            'left_header': 'Traditional',
            'right_header': 'American Express',
        }

    def get_impact_statement_style(self, variant: str = 'blue') -> Dict:
        """
        Get styling for impact/closing statements.

        Args:
            variant: 'blue' (blue background) or 'white' (white background)
        """
        if variant == 'blue':
            return {
                'background_color': '#0066CC',
                'text_color': '#FFFFFF',
                'border_radius': 36,
                'padding': {'horizontal': 60, 'vertical': 40},
                'headline_size': 36,
                'subheading_size': 20,
            }
        else:
            return {
                'background_color': '#FFFFFF',
                'text_color': '#1A1A1A',
                'border_radius': 36,
                'padding': {'horizontal': 60, 'vertical': 40},
                'headline_size': 36,
                'subheading_size': 20,
            }


# Convenience functions for external use
def create_design_reader(design_md_path: str) -> DesignSystemReader:
    """Factory for creating a DesignSystemReader"""
    return DesignSystemReader(design_md_path)


def create_design_applier(design_md_path: str) -> DesignApplier:
    """Factory for creating a DesignApplier"""
    reader = DesignSystemReader(design_md_path)
    return DesignApplier(reader)
