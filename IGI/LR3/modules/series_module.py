# modules/series_module.py
"""
Module: series_module.py
Description: Task 1 - Power series expansion for sin(x)
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

import math
from typing import Tuple, Optional
from .common.input_utils import get_float_input

def get_eps_input() -> float:
    """
    Get epsilon (precision) input from the user.
    ONLY USED IN TASK 1 for series expansion.
    
    Returns:
        Positive epsilon value
    """
    def is_positive(v: float) -> bool:
        return v > 0
    
    return get_float_input(
        "Enter epsilon (precision, positive number): ",
        "Epsilon must be a positive number.",
        validator=is_positive
    )


def factorial(n: int) -> int:
    """
    Calculate factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
    
    Returns:
        n! (factorial)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sin_series_term(x: float, n: int) -> float:
    """
    Calculate the n-th term of the sin(x) series expansion.
    
    Series: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    Term formula: (-1)^n * x^(2n+1) / (2n+1)!
    
    Args:
        x: The value to calculate the term for
        n: The term number (0-indexed)
    
    Returns:
        The n-th term of the series
    """
    if n < 0:
        raise ValueError("Term number must be >= 0")
    
    power = 2 * n + 1
    sign = (-1) ** n
    term = sign * (x ** power) / factorial(power)
    return term


def calculate_sin_series(x: float, eps: float, max_iter: int = 500) -> Tuple[Optional[float], int, Optional[str]]:
    """
    Calculate sin(x) using power series expansion with given precision.
    Args:
        x: The value to calculate sin(x) for
        eps: Required precision (epsilon)
        max_iter: Maximum number of iterations
    Returns:
        Tuple of (calculated sum, number of terms, error message)
    """
    if eps <= 0:
        return None, 0, "Epsilon must be positive"
    
    total = 0.0
    n = 0
    term = x  # First term
    
    while n <= max_iter:
        if n > 0:
            # Recurrence relation for efficiency
            term = term * (-x * x) / ((2 * n) * (2 * n + 1))
        
        total += term
        
        if abs(term) < eps:
            return total, n + 1, None
        
        n += 1
    
    return None, max_iter, f"Maximum iterations ({max_iter}) reached"

def get_math_value(x: float) -> float:
    """Calculate sin(x) using math module."""
    return math.sin(x)

def format_result(x: float, series_result: Optional[float], n_terms: int, 
                  math_result: Optional[float], eps: float) -> str:
    """Format results for display."""
    result_str = f"\n{'='*60}\nRESULTS:\n{'='*60}\n"
    result_str += f"x = {x:.8f} rad ({math.degrees(x):.2f}°)\n"
    result_str += f"Epsilon = {eps}\n{'-'*60}\n"
    
    if series_result is not None:
        result_str += f"F(x) (series) = {series_result:.12f}\n"
        result_str += f"Number of terms = {n_terms}\n"
    else:
        result_str += f"F(x) (series) = NOT COMPUTED\n"
        result_str += f"Number of terms = {n_terms}\n"
    
    if math_result is not None:
        result_str += f"Math F(x) = {math_result:.12f}\n"
        
        if series_result is not None:
            diff = abs(series_result - math_result)
            result_str += f"Difference = {diff:.12f}\n"
            result_str += f"Precision achieved: {'Yes' if diff < eps else 'No'}\n"
    
    result_str += f"{'='*60}\n"
    return result_str