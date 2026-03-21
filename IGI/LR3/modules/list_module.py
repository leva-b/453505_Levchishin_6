"""
Module: list_module.py
Description: Task 5 - List processing
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

from typing import List, Tuple, Optional


def find_max_modulus_index(lst: List[float]) -> int:
    """
    Find index of element with maximum absolute value.
    
    Args:
        lst: List of numbers
    
    Returns:
        Index of element with maximum absolute value
    """
    if not lst:
        return -1
    
    max_abs = abs(lst[0])
    max_index = 0
    
    for i, val in enumerate(lst):
        if abs(val) > max_abs:
            max_abs = abs(val)
            max_index = i
    
    return max_index


def find_first_positive_index(lst: List[float]) -> Optional[int]:
    """
    Find index of first positive element.
    
    Args:
        lst: List of numbers
    
    Returns:
        Index of first positive element, or None if no positive elements
    """
    for i, val in enumerate(lst):
        if val > 0:
            return i
    return None


def sum_after_index(lst: List[float], start_idx: int) -> float:
    """
    Sum elements after a given index.
    
    Args:
        lst: List of numbers
        start_idx: Index after which to sum
    
    Returns:
        Sum of elements after start_idx
    """
    if start_idx < 0 or start_idx >= len(lst) - 1:
        return 0.0
    
    return sum(lst[start_idx + 1:])


def process_list(lst: List[float]) -> Tuple[Optional[float], str]:
    """
    Process list according to variant.
    
    Args:
        lst: List of numbers
        variant: Task variant number
    
    Returns:
        Tuple of (result, description)
    """
    if not lst:
        return None, "\n--- RESULTS ---\nList is empty. Cannot process."
    
    max_mod_index = find_max_modulus_index(lst)
    max_mod_value = abs(lst[max_mod_index])
    
    first_pos_idx = find_first_positive_index(lst)
    
    if first_pos_idx is None:
        sum_after_positive = 0.0
        pos_desc = "No positive elements found in the list"
    elif first_pos_idx == len(lst) - 1:
        sum_after_positive = 0.0
        pos_desc = f"First positive element at index {first_pos_idx} is the last element, no elements after it"
    else:
        sum_after_positive = sum_after_index(lst, first_pos_idx)
        pos_desc = f"Sum of elements after first positive element (index {first_pos_idx}, value {lst[first_pos_idx]})"
    
    description = f"\n--- RESULTS (Variant 6) ---\n"
    description += f"\na) Maximum modulus element:\n"
    description += f"   Index: {max_mod_index}\n"
    description += f"   Value: {lst[max_mod_index]}\n"
    description += f"   Absolute value: {max_mod_value:.4f}\n"
    
    description += f"\nb) {pos_desc}:\n"
    description += f"   Sum: {sum_after_positive:.4f}\n"
    
    if first_pos_idx is not None and first_pos_idx < len(lst) - 1:
        after_elements = lst[first_pos_idx + 1:]
        description += f"   Elements after: {after_elements}\n"
    
    return sum_after_positive, description
    