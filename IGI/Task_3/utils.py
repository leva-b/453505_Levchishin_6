"""
Input validation and helper functions for Task 3.
Lab 4, Task 3.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

def safe_float_input(prompt: str, allow_negative: bool = True) -> float:
    """Read a float with validation."""
    while True:
        try:
            val = float(input(prompt).strip())
            if not allow_negative and val < 0:
                print("Value must be non-negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid number. Please enter a valid floating-point number.")

def safe_int_input(prompt: str, min_val: int = 1) -> int:
    """Read an integer with bounds."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val < min_val:
                print(f"Value must be at least {min_val}. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Please enter an integer.")

def safe_positive_float(prompt: str) -> float:
    """Read a positive float (e.g., eps)."""
    while True:
        val = safe_float_input(prompt, allow_negative=False)
        if val > 0:
            return val
        print("Value must be > 0.")

def generate_x_range(start: float, end: float, num_points: int) -> list:
    """Generate list of x values from start to end inclusive, num_points steps."""
    if num_points < 2:
        return [start]
    step = (end - start) / (num_points - 1)
    return [start + i * step for i in range(num_points)]