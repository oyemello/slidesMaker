#!/usr/bin/env python3
"""
Markdown to Presentation Parser
Reads a markdown file and intelligently detects slide content types.
"""

import re
from dataclasses import dataclass
from typing import List, Dict, Optional, Literal


@dataclass
class Metric:
    """Represents a key:value metric pair"""
    key: str
    value: str
    change: Optional[str] = None  # "+15%", "-5%", etc.

    @property
    def has_change(self) -> bool:
        return self.change is not None

    @property
    def is_positive(self) -> bool:
        """True if change starts with +"""
        return self.change and self.change.startswith('+')

    @property
    def is_negative(self) -> bool:
        """True if change starts with -"""
        return self.change and self.change.startswith('-')


@dataclass
class Slide:
    """Represents a single slide"""
    title: str
    slide_type: Literal["title", "metrics", "features", "text", "comparison", "impact"]
    content: any  # Can be list of strings, list of Metrics, dict for comparison

    def __repr__(self) -> str:
        return f"Slide(type={self.slide_type}, title='{self.title}')"


class MarkdownParser:
    """Parses markdown files into presentation slides"""

    def __init__(self, markdown_path: str):
        """
        Initialize parser and read markdown file.

        Args:
            markdown_path: Path to .md file
        """
        self.path = markdown_path
        with open(markdown_path, 'r', encoding='utf-8') as f:
            self.content = f.read()

        self.presentation_title = ""
        self.presentation_subtitle = ""
        self.slides: List[Slide] = []

        self._parse()

    def _parse(self):
        """Parse the markdown file"""
        lines = self.content.split('\n')

        # Extract presentation title and subtitle
        title_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('# '):
                self.presentation_title = line[2:].strip()
                title_idx = i + 1
                break

        # Subtitle is the next non-empty line that's not a heading
        if title_idx < len(lines):
            for line in lines[title_idx:]:
                if line.strip() and not line.startswith('#'):
                    self.presentation_subtitle = line.strip()
                    break

        # Parse slides
        current_section = None
        current_lines = []

        for i, line in enumerate(lines):
            if line.startswith('## '):
                # New slide
                if current_section:
                    slide = self._create_slide(current_section, current_lines)
                    if slide:
                        self.slides.append(slide)

                current_section = line[3:].strip()
                current_lines = []
            elif line.startswith('# '):
                # Skip title
                continue
            elif current_section:
                # Add content line
                if line.strip():
                    current_lines.append(line)

        # Don't forget the last slide
        if current_section:
            slide = self._create_slide(current_section, current_lines)
            if slide:
                self.slides.append(slide)

    def _create_slide(self, title: str, lines: List[str]) -> Optional[Slide]:
        """
        Create a slide from title and content lines.
        Intelligently detect slide type.
        """
        if not lines:
            return None

        # Join lines and detect content type
        content = '\n'.join(lines)

        # Check for metrics pattern: "Key: Value (+%)" or "Key: $Amount (+%)"
        if self._is_metrics_slide(lines):
            metrics = self._extract_metrics(lines)
            if metrics:
                return Slide(
                    title=title,
                    slide_type="metrics",
                    content=metrics
                )

        # Check for bullet list (features)
        elif self._is_features_slide(lines):
            features = self._extract_features(lines)
            if features:
                return Slide(
                    title=title,
                    slide_type="features",
                    content=features
                )

        # Check for comparison (Traditional vs AmEx)
        elif self._is_comparison_slide(lines):
            comparison = self._extract_comparison(lines)
            if comparison:
                return Slide(
                    title=title,
                    slide_type="comparison",
                    content=comparison
                )

        # Check for impact statement (quoted or short powerful text)
        elif self._is_impact_slide(lines):
            return Slide(
                title=title,
                slide_type="impact",
                content=content
            )

        # Default: text slide
        else:
            return Slide(
                title=title,
                slide_type="text",
                content=lines
            )

    def _is_metrics_slide(self, lines: List[str]) -> bool:
        """Check if content looks like metrics (Key: Value pattern)"""
        metric_count = 0
        for line in lines:
            if ':' in line and not line.startswith('-'):
                # Could be a metric
                metric_count += 1

        return metric_count >= 2  # At least 2 key:value pairs

    def _extract_metrics(self, lines: List[str]) -> List[Metric]:
        """Extract metrics from lines"""
        metrics = []

        for line in lines:
            if ':' not in line or line.startswith('-'):
                continue

            # Pattern: "Key: Value (+/-percentage)"
            match = re.match(r'(.+?)\s*:\s*(.+?)\s*(\([+\-][^)]+\))?$', line)
            if match:
                key = match.group(1).strip()
                value = match.group(2).strip()
                change = match.group(3)

                if change:
                    change = change.strip('()')

                metrics.append(Metric(key=key, value=value, change=change))

        return metrics

    def _is_features_slide(self, lines: List[str]) -> bool:
        """Check if content looks like features (bullet list)"""
        bullet_count = 0
        for line in lines:
            if line.strip().startswith('-'):
                bullet_count += 1

        return bullet_count >= 2

    def _extract_features(self, lines: List[str]) -> List[Dict]:
        """Extract features from bullet points"""
        features = []

        for line in lines:
            if line.strip().startswith('-'):
                feature_text = line.strip()[1:].strip()

                # Check if it has "Title: Description" pattern
                if ':' in feature_text:
                    parts = feature_text.split(':', 1)
                    features.append({
                        'title': parts[0].strip(),
                        'description': parts[1].strip()
                    })
                else:
                    features.append({
                        'title': feature_text,
                        'description': ''
                    })

        return features

    def _is_comparison_slide(self, lines: List[str]) -> bool:
        """Check if content looks like a comparison (Traditional vs AmEx)"""
        text = '\n'.join(lines).lower()

        traditional_keywords = ['traditional', 'old', 'legacy']
        amex_keywords = ['amex', 'american express', 'new']

        has_traditional = any(kw in text for kw in traditional_keywords)
        has_amex = any(kw in text for kw in amex_keywords)

        return has_traditional and has_amex

    def _extract_comparison(self, lines: List[str]) -> Optional[Dict]:
        """Extract comparison content"""
        comparison = {
            'left': {'title': 'Traditional', 'items': []},
            'right': {'title': 'AmEx', 'items': []}
        }

        current_side = None

        for line in lines:
            line = line.strip()

            if not line:
                continue

            # Detect which side we're on
            if any(kw in line.lower() for kw in ['traditional', 'old', 'legacy']):
                current_side = 'left'
                # Extract title if provided
                if ':' in line:
                    comparison['left']['title'] = line.split(':', 1)[1].strip()
            elif any(kw in line.lower() for kw in ['amex', 'american express']):
                current_side = 'right'
                if ':' in line:
                    comparison['right']['title'] = line.split(':', 1)[1].strip()

            # Add item to current side
            elif current_side and line.startswith('-'):
                item = line[1:].strip()
                comparison[current_side]['items'].append(item)

        # Only return if we have content on both sides
        if comparison['left']['items'] or comparison['right']['items']:
            return comparison

        return None

    def _is_impact_slide(self, lines: List[str]) -> bool:
        """Check if content looks like an impact/closing statement"""
        text = '\n'.join(lines)

        # Very short (1-2 lines)
        if len(lines) <= 2:
            return True

        # Contains quotes
        if '"' in text and len(text) < 300:
            return True

        # Ends with punctuation like !, ?
        if text.strip().endswith(('!', '?')) and len(text) < 200:
            return True

        return False


def parse_markdown(markdown_path: str) -> tuple[str, str, List[Slide]]:
    """
    Parse a markdown file into presentation structure.

    Returns:
        (title, subtitle, slides)
    """
    parser = MarkdownParser(markdown_path)
    return parser.presentation_title, parser.presentation_subtitle, parser.slides
