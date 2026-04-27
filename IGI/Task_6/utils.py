"""
Shared utilities for Task 6.
Lab 4, Task 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

def safe_bool_input(prompt: str) -> bool:
    """Ask yes/no question, return True for yes, False for no."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes', '1', 'true'):
            return True
        if answer in ('n', 'no', '0', 'false'):
            return False
        print("Please answer yes (y) or no (n).")