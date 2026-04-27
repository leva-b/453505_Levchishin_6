"""
Main execution for Task 5 (NumPy, variant 6).
Lab 4, Task 5.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

import os
import numpy as np
from .numpy_operations import MatrixAnalyzer
from .utils import safe_int_input

def save_matrix_and_result(matrix_analyzer, sum_abs, np_std, form_std, filepath):
    """Save matrix and results to a text file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=== TASK 5 RESULTS (Variant 6) ===\n")
        f.write(f"Matrix shape: {matrix_analyzer.shape}\n")
        f.write("Generated matrix:\n")
        np.savetxt(f, matrix_analyzer.matrix, fmt='%d', delimiter='\t')
        
        negative_odd = matrix_analyzer.get_negative_odd_elements()
        f.write(f"\nNegative odd elements: {negative_odd.tolist()}\n")
        f.write(f"Count of negative odd elements: {len(negative_odd)}\n")
        f.write(f"Sum of absolute values of negative odd elements: {sum_abs}\n")
        
        if len(negative_odd) <= 1:
            f.write(f"Standard deviation: Not enough elements (need at least 2)\n")
        else:
            f.write(f"Standard deviation (NumPy): {np_std:.4f} (rounded: {np_std:.2f})\n")
            f.write(f"Standard deviation (formula): {form_std:.4f} (rounded: {form_std:.2f})\n")
            f.write(f"Methods agree: {np.isclose(np_std, form_std, rtol=1e-9)}\n")

def run():
    print("\n=== TASK 5: NUMPY MATRIX ANALYSIS (Variant 6) ===\n")
    
    while True:
        rows = safe_int_input("Enter number of rows (n): ", min_val=1)
        cols = safe_int_input("Enter number of columns (m): ", min_val=1)
        
        analyzer = MatrixAnalyzer(rows, cols, low=-50, high=51)   
        print(f"\nGenerated random integer matrix of shape {analyzer.shape}:")
        print(analyzer.matrix)
        
        analyzer.demonstrate_indexing_slicing()
        analyzer.demonstrate_ufuncs()
        
        negative_odd = analyzer.get_negative_odd_elements()
        print(f"\nNegative odd elements: {negative_odd.tolist()}")
        print(f"Count of negative odd elements: {len(negative_odd)}")
        
        if len(negative_odd) == 0:
            print("\nNo negative odd elements found in the matrix.")
            sum_abs = 0
            np_std = form_std = 0.0
            print(f"Sum of absolute values: {sum_abs}")
            print("Standard deviation: Not applicable (no elements found)")
        elif len(negative_odd) == 1:
            sum_abs = analyzer.sum_of_abs_negative_odd()
            print(f"\nSum of absolute values of negative odd elements: {sum_abs}")
            print("Standard deviation: Cannot compute with only 1 element (need at least 2)")
            np_std = form_std = 0.0
        else:
            sum_abs = analyzer.sum_of_abs_negative_odd()
            np_std, form_std, _ = analyzer.compare_std()
            print(f"\nSum of absolute values of negative odd elements: {sum_abs}")
            print(f"Standard deviation (NumPy): {np_std:.4f}, rounded: {np_std:.2f}")
            print(f"Standard deviation (formula): {form_std:.4f}, rounded: {form_std:.2f}")
        
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(data_dir, exist_ok=True)
        results_path = os.path.join(data_dir, "results.txt")
        save_matrix_and_result(analyzer, sum_abs, np_std, form_std, results_path)
        print(f"\nResults saved to: {results_path}")
        
        again = input("\nDo you want to generate another matrix? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting Task 5.")
            break

if __name__ == "__main__":
    run()