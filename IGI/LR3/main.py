"""
Module: main.py
Description: Main program for laboratory work No. 3
Lab: Laboratory Work No. 3
Version: 1.0
Author: Ivan Leuchyshyn
Date: 2026-03-21
"""

import sys
import math
from typing import Optional

from modules.common.input_utils import (
    get_float_input,
    get_string_input,
    get_continue_choice,
)

from modules.common.init_methods import (
    get_initialization_method,
    initialize_sequence
)

from modules.common.decorators import log_execution

from modules.series_module import (
    calculate_sin_series,
    get_math_value,
    get_eps_input,
    format_result
)
from modules.sequence_module import process_sequence
from modules.text_module import analyze_text
from modules.advanced_text_module import analyze_advanced_text, PREDEFINED_TEXT
from modules.list_module import process_list


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*70)
    print("LABORATORY WORK No. 3")
    print("Topic: Standard Data Types, Collections, Functions, Modules")
    print("Author: Ivan Leuchyshyn")
    print("Date: 2026-03-21")
    print("="*70)


def task1_series_calculation() -> None:
    """Task 1: Calculate sin(x) using series expansion."""
    print("\n" + "="*60)
    print("TASK 1: Power Series Expansion - sin(x)")
    print("sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...")
    print("="*60)
    
    while True:
        x = get_float_input(
            "\nEnter x in radians (or press Enter to return to menu): ",
            allow_none=True
        )
        
        if x is None:
            break
        
        eps = get_eps_input()
        
        print(f"\nCalculating sin({x:.6f}) with eps = {eps}...")
        
        series_result, n_terms, error = calculate_sin_series(x, eps)
        math_result = get_math_value(x)
        
        if error:
            print(f"\nWarning: {error}")
        
        print(format_result(x, series_result, n_terms, math_result, eps))
        
        if not get_continue_choice():
            break


def task2_sequence_processing() -> None:
    """Task 2: Process sequence of numbers."""
    print("\n" + "="*60)
    print("TASK 2: Sequence Processing")
    print("Variant 6: Arithmetic mean of numbers until zero")
    print("="*60)
    
    result, description = process_sequence()
    print(description)


def task3_text_analysis() -> None:
    """Task 3: Basic text analysis."""
    print("\n" + "="*60)
    print("TASK 3: Text Analysis")
    print("Variant 6: Count non-whitespace characters")
    print("="*60)
    
    text = get_string_input("\nEnter text to analyze: ")
    result = analyze_text(text)
    print(f"\n{result['description']}")


def task4_advanced_text_analysis() -> None:
    """Task 4: Advanced text analysis with predefined string."""
    print("\n" + "="*60)
    print("TASK 4: Advanced Text Analysis")
    print("Variant 6: Words ending with vowel, average length, every 5th word")
    print("="*60)
    
    print(f"\nAnalyzing predefined text:")
    print(f"{PREDEFINED_TEXT}")
    
    result = analyze_advanced_text()
    print(result['description'])


def task5_list_processing() -> None:
    """Task 5: List processing."""
    print("\n" + "="*60)
    print("TASK 5: List Processing")
    print("Variant 6: Max modulus index and sum after first positive")
    print("="*60)
    
    method = get_initialization_method()
    if method == 'quit':
        return
    
    sequence = initialize_sequence(method)
    
    if not sequence:
        print("No values to process.")
        return
    
    print(f"\nSequence ({len(sequence)} elements):")
    if len(sequence) <= 20:
        print(f"  {sequence}")
    else:
        print(f"  {sequence[:10]} ... {sequence[-5:]}")
    
    result, description = process_list(sequence)
    print(description)

def main() -> None:
    """Main menu."""
    display_welcome()
    
    while True:
        print("\n" + "-"*50)
        print("MAIN MENU:")
        print("  1. Task 1: Series Expansion (sin(x)) - needs epsilon")
        print("  2. Task 2: Sequence Processing (arithmetic mean)")
        print("  3. Task 3: Text Analysis (non-whitespace characters)")
        print("  4. Task 4: Advanced Text Analysis (vowels, average, every 5th)")
        print("  5. Task 5: List Processing (max modulus, sum after first positive)")
        print("  6. Exit")
        print("-"*50)
        
        choice = input("\nSelect task (1-6): ").strip()
        
        if choice == '1':
            task1_series_calculation()
        elif choice == '2':
            task2_sequence_processing()
        elif choice == '3':
            task3_text_analysis()
        elif choice == '4':
            task4_advanced_text_analysis()
        elif choice == '5':
            task5_list_processing()
        elif choice == '6':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

@log_execution
def decorated_task1_example() -> None:
    """Example of Task 1 with decorator."""
    x = math.pi / 6
    eps = 0.0001
    result, n, error = calculate_sin_series(x, eps)
    if result:
        print(f"sin({x:.4f}) ≈ {result:.8f} using {n} terms")
    else:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()