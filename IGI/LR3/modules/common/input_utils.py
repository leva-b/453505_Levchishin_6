"""
Module: input_utils.py
Description: Common input handling functions for all tasks
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

from typing import Optional, Callable, Any, List


def get_float_input(prompt: str, 
                   error_msg: str = "Invalid input. Please enter a number.",
                   allow_none: bool = False, 
                   validator: Optional[Callable[[float], bool]] = None) -> Optional[float]:
    """
    Safely get a float input from the user with validation.
    
    Args:
        prompt: The prompt to display to the user
        error_msg: Error message for invalid input
        allow_none: Whether to allow empty input (returns None)
        validator: Function that takes float and returns bool for validation
    
    Returns:
        The validated float value, or None if allow_none and input is empty
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if allow_none and user_input == "":
                return None
            
            value = float(user_input)
            
            if validator is not None and not validator(value):
                print(f"Invalid value. Please try again.")
                continue
            
            return value
            
        except ValueError:
            print(error_msg)


def get_int_input(prompt: str,
                 error_msg: str = "Invalid input. Please enter an integer.",
                 allow_none: bool = False,
                 min_val: Optional[int] = None,
                 max_val: Optional[int] = None) -> Optional[int]:
    """
    Safely get an integer input from the user with validation.
    
    Args:
        prompt: The prompt to display to the user
        error_msg: Error message for invalid input
        allow_none: Whether to allow empty input (returns None)
        min_val: Minimum allowed value (inclusive)
        max_val: Maximum allowed value (inclusive)
    
    Returns:
        The validated integer value, or None if allow_none and input is empty
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            if allow_none and user_input == "":
                return None
            
            value = int(user_input)
            
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            
            return value
            
        except ValueError:
            print(error_msg)


def get_string_input(prompt: str,
                    allow_empty: bool = False,
                    validator: Optional[Callable[[str], bool]] = None) -> str:
    """
    Safely get a string input from the user.
    
    Args:
        prompt: The prompt to display to the user
        allow_empty: Whether to allow empty string
        validator: Function that takes string and returns bool for validation
    
    Returns:
        The validated string value
    """
    while True:
        value = input(prompt).strip()
        
        if not allow_empty and value == "":
            print("Input cannot be empty. Please try again.")
            continue
        
        if validator is not None and not validator(value):
            print("Invalid input format. Please try again.")
            continue
        
        return value


def get_continue_choice() -> bool:
    """
    Ask user if they want to continue.
    
    Returns:
        True if user wants to continue, False otherwise
    """
    while True:
        choice = input("\nDo you want to continue? (y/n): ").lower().strip()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("Please enter 'y' or 'n'")