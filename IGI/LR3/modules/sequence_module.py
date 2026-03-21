"""
Module: sequence_module.py
Description: Task 2 - Sequence processing (average until zero)
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""
from typing import Tuple, Optional

def average_until_zero() -> Tuple[float, int]:
    """
    Task 2, Variant 6: Calculate average of integers until zero is entered.
    
    Returns:
        Tuple of (average, count of numbers processed)
    """
    total = 0
    count = 0
    
    print("\nEnter integers one by one. Enter 0 to stop.")
    print("The program will calculate the arithmetic mean of entered numbers.\n")
    
    while True:
        try:
            num = int(input(f"Number {count + 1} (0 to stop): "))
            
            if num == 0:
                break
            
            total += num
            count += 1
            print(f"  Added {num}, Sum: {total}, Count: {count}")
            
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    if count == 0:
        return 0.0, 0
    else:
        average = total / count
        return average, count


def process_sequence() -> Tuple[Optional[float], str]:
    """
    Process sequence according to variant.
    
    Args:
        variant: Task variant number (1-30)
    
    Returns:
        Tuple of (result, description)
    """
    average, count = average_until_zero()
        
    if count == 0:
        return None, "\nNo numbers were entered (only zero)."
        
    return average, f"\n--- RESULTS ---\n" \
                    f"Sum of numbers: {average * count:.0f}\n" \
                    f"Count of numbers: {count}\n" \
                    f"Arithmetic mean: {average:.4f}"