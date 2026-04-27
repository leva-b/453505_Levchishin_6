"""
Input validation for matrix dimensions.
Lab 4, Task 5.
Developer: Ivan Leuchyshyn
Date: 2026-04-25
"""

def safe_int_input(prompt: str, min_val: int = 1) -> int:
    """Read a positive integer with validation."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val < min_val:
                print(f"Value must be at least {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Please enter an integer.")