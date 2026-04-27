"""
Input validation and helper functions for Task 4.
Lab 4, Task 4.
Developer: Ivan Leuchyshyn
Date: 2026-04-25
"""

def safe_float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    """Read a float with optional min/max bounds."""
    while True:
        try:
            val = float(input(prompt).strip())
            if min_val is not None and val <= min_val:
                print(f"Value must be greater than {min_val}. Try again.")
                continue
            if max_val is not None and val >= max_val:
                print(f"Value must be less than {max_val}. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid number. Please enter a valid floating-point number.")

def safe_string_input(prompt: str, allow_empty: bool = False) -> str:
    """Read a non-empty string (unless allowed)."""
    while True:
        val = input(prompt).strip()
        if val or allow_empty:
            return val
        print("Input cannot be empty. Please try again.")

def get_color_name() -> str:
    """Ask user for a color name (matplotlib recognized). Provide hint."""
    print("\nAvailable colors: 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange', 'purple', 'brown', 'pink', 'gray', 'black'")
    print("You can also use HTML hex codes like '#FF5733'.")
    while True:
        color = safe_string_input("Enter fill color: ")
        return color

def get_rhombus_parameters() -> tuple:
    """Get side, angle, color, and label from user."""
    print("\n--- Enter rhombus parameters ---")
    side = safe_float_input("Side length a (positive): ", min_val=0)
    angle = safe_float_input("Acute angle in degrees (0 < angle < 90): ", min_val=0, max_val=90)
    color = get_color_name()
    label = safe_string_input("Text label to display on the figure (e.g., 'My Rhombus'): ", allow_empty=False)
    return side, angle, color, label