"""
AmEx PowerPoint Maker Scripts
Scripts for generating and managing PowerPoint presentations.
"""

from .create_pptx import PowerPointGenerator, SlideLayout
from .icon_manager import IconManager
from .design_system import (
    DesignSystemReader,
    DesignApplier,
    ColorToken,
    TypographyRule,
    create_design_reader,
    create_design_applier,
)
from .markdown_parser import MarkdownParser, Slide, Metric, parse_markdown

__all__ = [
    "PowerPointGenerator",
    "IconManager",
    "SlideLayout",
    "DesignSystemReader",
    "DesignApplier",
    "ColorToken",
    "TypographyRule",
    "create_design_reader",
    "create_design_applier",
    "MarkdownParser",
    "Slide",
    "Metric",
    "parse_markdown",
]
