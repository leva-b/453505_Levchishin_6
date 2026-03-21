"""
Module: text_module.py
Description: Task 3 - Basic text analysis
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

from typing import Dict, Any


def count_non_whitespace(text: str) -> int:
    """
    Task 3, Variant 1: Count uppercase English letters.
    
    Args:
        text: Input string
    
    Returns:
        Number of uppercase English letters
    """
    count = 0
    for char in text:
        if not char.isspace():
            count += 1
    return count


def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyze text according to variant.
    
    Args:
        text: Input string
        variant: Task variant number
    
    Returns:
        Dictionary with analysis results
    """
    
    result = count_non_whitespace(text)
    return {
        'result': result,
        'description': f"Number of uppercase English letters: {result}"
    }