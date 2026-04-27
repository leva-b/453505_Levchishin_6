"""
Main execution for Task 3 (sin x series, statistics, plotting).
Lab 4, Task 3, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import os
from .series import SinSeries
from .statistics import SequenceStats
from .plotter import plot_comparison
from .utils import (
    safe_positive_float, safe_float_input, safe_int_input,
    generate_x_range
)

def run():
    print("\n=== TASK 3: SIN(X) SERIES EXPANSION (Variant 6) ===\n")
    
    # --- Input parameters ---
    print("Enter range of x values (in radians):")
    x_start = safe_float_input("Start x: ")
    x_end = safe_float_input("End x: ")
    num_points = safe_int_input("Number of points (≥2): ", 2)
    eps = safe_positive_float("Precision (epsilon) for series (e.g., 1e-6): ")
    
    # --- Generate x values ---
    x_vals = generate_x_range(x_start, x_end, num_points)
    print(f"Computed {len(x_vals)} x values from {x_start:.3f} to {x_end:.3f}")
    
    # --- Compute series ---
    series = SinSeries(eps=eps, max_iter=100)
    table = series.compute_table(x_vals)
    
    print("\n--- Results (first 5 points) ---")
    for row in table[:5]:
        print(f"x = {row['x']:.4f}, approx = {row['approx']:.6f}, exact = {row['exact']:.6f}, terms = {row['terms']}")
    if len(table) > 5:
        print("...")
    
    approx_values = [row['approx'] for row in table]
    stats = SequenceStats(approx_values)
    
    print("\n--- Statistical analysis of sin(x) approximations ---")
    print(f"Arithmetic mean: {stats.arithmetic_mean():.6f}")
    print(f"Median: {stats.median():.6f}")
    print(f"Mode: {stats.mode()}")
    print(f"Variance (sample): {stats.variance(sample=True):.6f}")
    print(f"Standard deviation (sample): {stats.std_dev(sample=True):.6f}")
    
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    plot_path = os.path.join(data_dir, "sin_plot.png")
    
    plot_comparison(table, plot_path, title=f"Sin(x) Approximation (eps={eps:.1e})")
    
    results_path = os.path.join(data_dir, "results.txt")
    with open(results_path, 'w', encoding='utf-8') as f:
        f.write("=== TASK 3 RESULTS (Variant 6) ===\n")
        f.write(f"x range: [{x_start}, {x_end}], points: {num_points}, eps: {eps}\n\n")
        f.write("x\tapprox\texact\tabs_error\tterms\n")
        for row in table:
            f.write(f"{row['x']:.4f}\t{row['approx']:.6f}\t{row['exact']:.6f}\t{row['abs_error']:.2e}\t{row['terms']}\n")
        f.write("\n--- Statistics of approx values ---\n")
        f.write(f"Mean: {stats.arithmetic_mean():.6f}\n")
        f.write(f"Median: {stats.median():.6f}\n")
        f.write(f"Mode: {stats.mode()}\n")
        f.write(f"Variance: {stats.variance():.6f}\n")
        f.write(f"Std Dev: {stats.std_dev():.6f}\n")
    
    print(f"\nDetailed results saved to: {results_path}")
    print("Task 3 completed.")

if __name__ == "__main__":
    run()