#!/usr/bin/env python3
"""
Material Design Icon Manager
Handles icon resolution, selection, and embedding in PowerPoint.
"""

import json
import os
from typing import Optional, List, Dict, Tuple
from difflib import SequenceMatcher


class IconManager:
    """Manages Material Design icon selection and embedding"""

    def __init__(self, icons_index_path: str):
        """
        Initialize icon manager with Material Design icons index.

        Args:
            icons_index_path: Path to material-icons-index.json
        """
        self.icons_index = self._load_index(icons_index_path)
        self.icons_flat = self._flatten_index()

    def _load_index(self, path: str) -> Dict:
        """Load and parse icons index JSON"""
        if not os.path.exists(path):
            return {}

        with open(path) as f:
            return json.load(f)

    def _flatten_index(self) -> Dict:
        """Flatten nested icon structure for easier lookup"""
        flat = {}
        if "icons" not in self.icons_index:
            return flat

        for category, icons in self.icons_index["icons"].items():
            for icon_name, icon_data in icons.items():
                flat[icon_name] = {
                    "category": category,
                    **icon_data
                }

        return flat

    def resolve_icon(self, query: str) -> Optional[str]:
        """
        Resolve an icon by name or use case keyword.

        Args:
            query: Icon name or use case keyword (e.g., "person", "user", "profile")

        Returns:
            Icon name if found, None otherwise
        """
        query = query.lower().strip()

        # Exact match
        if query in self.icons_flat:
            return query

        # Search by use case keywords
        for icon_name, icon_data in self.icons_flat.items():
            use_cases = icon_data.get("use_cases", [])
            keywords = icon_data.get("keywords", [])

            if query in use_cases or query in keywords:
                return icon_name

        # Fuzzy match
        best_match = self._fuzzy_match(query)
        return best_match

    def _fuzzy_match(self, query: str, threshold: float = 0.6) -> Optional[str]:
        """
        Fuzzy match icon name or keywords.

        Args:
            query: Search term
            threshold: Similarity threshold (0-1)

        Returns:
            Best matching icon name or None
        """
        best_score = 0
        best_icon = None

        for icon_name, icon_data in self.icons_flat.items():
            # Compare with icon name
            score = SequenceMatcher(None, query, icon_name).ratio()

            # Compare with keywords
            for keyword in icon_data.get("keywords", []):
                keyword_score = SequenceMatcher(None, query, keyword).ratio()
                score = max(score, keyword_score)

            if score > best_score:
                best_score = score
                best_icon = icon_name

        return best_icon if best_score >= threshold else None

    def get_icon_by_use_case(self, use_case: str) -> List[str]:
        """
        Get all icons that match a use case.

        Args:
            use_case: Use case keyword (e.g., "security", "growth")

        Returns:
            List of matching icon names
        """
        use_case = use_case.lower().strip()
        matches = []

        for icon_name, icon_data in self.icons_flat.items():
            if use_case in icon_data.get("use_cases", []):
                matches.append(icon_name)

        return matches

    def search_icons(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for icons by keyword or name.

        Args:
            query: Search term
            limit: Maximum results to return

        Returns:
            List of matching icons with metadata
        """
        query = query.lower().strip()
        results = []

        for icon_name, icon_data in self.icons_flat.items():
            score = 0

            # Check name
            if query in icon_name:
                score += 10

            # Check keywords
            for keyword in icon_data.get("keywords", []):
                if query in keyword:
                    score += 5

            # Check use cases
            for use_case in icon_data.get("use_cases", []):
                if query in use_case:
                    score += 3

            if score > 0:
                results.append({
                    "name": icon_name,
                    "category": icon_data.get("category"),
                    "use_cases": icon_data.get("use_cases", []),
                    "keywords": icon_data.get("keywords", []),
                    "description": icon_data.get("description"),
                    "score": score
                })

        # Sort by score (descending)
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:limit]

    def get_category_icons(self, category: str) -> List[str]:
        """
        Get all icons in a category.

        Args:
            category: Category name

        Returns:
            List of icon names
        """
        return [
            icon_name
            for icon_name, icon_data in self.icons_flat.items()
            if icon_data.get("category") == category
        ]

    def list_categories(self) -> List[str]:
        """Get all available categories"""
        categories = set()
        for icon_data in self.icons_flat.values():
            if "category" in icon_data:
                categories.add(icon_data["category"])
        return sorted(list(categories))

    def get_icon_info(self, icon_name: str) -> Optional[Dict]:
        """Get detailed information about an icon"""
        return self.icons_flat.get(icon_name.lower())

    def suggest_icons(self, context: str, count: int = 5) -> List[str]:
        """
        Suggest icons based on context.

        Examples:
            - "financial dashboard" -> trending_up, analytics, show_chart, etc.
            - "user management" -> person, group, supervisor_account, etc.

        Args:
            context: Context description
            count: Number of suggestions

        Returns:
            List of suggested icon names
        """
        context = context.lower()
        scored_icons = {}

        for icon_name, icon_data in self.icons_flat.items():
            score = 0

            # Score based on use case match
            for use_case in icon_data.get("use_cases", []):
                if use_case in context:
                    score += 10

            # Score based on keyword match
            for keyword in icon_data.get("keywords", []):
                if keyword in context:
                    score += 5

            # Score based on category
            category = icon_data.get("category", "")
            if category.lower() in context:
                score += 3

            if score > 0:
                scored_icons[icon_name] = score

        # Sort by score and return top N
        sorted_icons = sorted(scored_icons.items(), key=lambda x: x[1], reverse=True)
        return [icon for icon, _ in sorted_icons[:count]]


def main():
    """Example usage"""
    # Assuming icons index is in the same directory
    icon_mgr = IconManager("../references/material-icons-index.json")

    # Resolve an icon by name
    print("Resolve 'person':", icon_mgr.resolve_icon("person"))

    # Resolve by use case
    print("Resolve 'user profile':", icon_mgr.resolve_icon("profile"))

    # Get all icons for a use case
    print("Security icons:", icon_mgr.get_icon_by_use_case("security"))

    # Search
    print("\nSearch for 'growth':")
    results = icon_mgr.search_icons("growth", limit=5)
    for result in results:
        print(f"  - {result['name']}: {result['description']}")

    # Categories
    print("\nCategories:", icon_mgr.list_categories())

    # Suggest icons for context
    print("\nSuggested icons for 'financial analysis':")
    suggestions = icon_mgr.suggest_icons("financial analysis")
    for icon in suggestions:
        print(f"  - {icon}")


if __name__ == "__main__":
    main()
