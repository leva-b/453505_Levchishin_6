# modules/common/init_methods.py
"""
Module: init_methods.py
Description: Common initialization methods for sequences
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

from typing import List, Generator, Optional
import random

# Используем относительный импорт
from .input_utils import get_float_input, get_int_input


def generator_sequence_generator() -> Generator[float, None, None]:
    """
    Generator function that yields test values.
    Used for Task 5 (list processing).
    
    Yields:
        Test values in sequence
    """
    test_values = [5.0, -3.0, 8.0, -2.0, 0.0, 7.0, -4.0, 6.0, -1.0, 3.0]
    
    for value in test_values:
        yield value


def manual_sequence_input(prompt: str = "Enter value") -> List[float]:
    """
    Manually input sequence values from user.
    
    Args:
        prompt: Base prompt for input
    
    Returns:
        List of manually entered values
    """
    values = []
    print(f"\nEnter values (enter 'done' to finish):")
    
    while True:
        value = get_float_input(
            f"{prompt} {len(values) + 1}: ",
            "Invalid input. Please enter a number.",
            allow_none=False
        )
        
        if value is None:
            continue
        else:
            values.append(value)
            
            response = input(f"Added {value}. Add another? (y/n): ").lower().strip()
            if response in ('n', 'no'):
                break
    
    return values


def random_sequence_generator(size: int, min_val: float = -10.0, max_val: float = 10.0) -> List[float]:
    """
    Generate random sequence of specified size.
    
    Args:
        size: Number of elements
        min_val: Minimum value (default: -10.0)
        max_val: Maximum value (default: 10.0)
    
    Returns:
        List of random values
    """
    return [random.uniform(min_val, max_val) for _ in range(size)]


def get_initialization_method() -> str:
    """
    Get initialization method choice from user.
    Used for Task 5 (list processing).
    
    Returns:
        'generator', 'manual', 'random', or 'quit'
    """
    print("\n" + "-"*40)
    print("LIST INITIALIZATION METHOD:")
    print("  1. Using generator function (test values)")
    print("  2. Manual input")
    print("  3. Random generation")
    print("  4. Back to main menu")
    print("-"*40)
    
    while True:
        choice = input("Select method (1-4): ").strip()
        if choice == '1':
            return 'generator'
        elif choice == '2':
            return 'manual'
        elif choice == '3':
            return 'random'
        elif choice == '4':
            return 'quit'
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def initialize_sequence(method: str, size: Optional[int] = None) -> List[float]:
    """
    Initialize sequence using specified method.
    
    Args:
        method: 'generator', 'manual', or 'random'
        size: Size for random generation (if None, user will be prompted)
    
    Returns:
        Initialized sequence
    """
    if method == 'generator':
        print("\nInitializing sequence using generator function...")
        return list(generator_sequence_generator())
    elif method == 'manual':
        print("\nInitializing sequence using manual input...")
        return manual_sequence_input()
    elif method == 'random':
        if size is None:
            size = get_int_input("Enter list size: ", min_val=1)
        print(f"\nGenerating {size} random values...")
        return random_sequence_generator(size)
    else:
        return []


def get_float_sequence_from_user() -> List[float]:
    """
    Get a sequence of floats from user input.
    Alternative method for sequence initialization.
    
    Returns:
        List of floats entered by user
    """
    size = get_int_input("Enter number of elements: ", min_val=1)
    sequence = []
    
    print(f"\nEnter {size} numbers:")
    for i in range(size):
        value = get_float_input(f"Element {i + 1}: ")
        sequence.append(value)
    
    return sequence


def get_int_sequence_from_user() -> List[int]:
    """
    Get a sequence of integers from user input.
    
    Returns:
        List of integers entered by user
    """
    size = get_int_input("Enter number of elements: ", min_val=1)
    sequence = []
    
    print(f"\nEnter {size} integers:")
    for i in range(size):
        value = get_int_input(f"Element {i + 1}: ")
        sequence.append(value)
    
    return sequence