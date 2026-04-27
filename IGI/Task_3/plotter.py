"""
Plotting functions using matplotlib.
Lab 4, Task 3.
Developer: Ivan Leuchyshyn
Date: 2026-04-26
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict

def plot_comparison(table: List[Dict], save_path: str, title: str = "Sin(x) Approximation"):
    """
    Plot approximate (series) and exact (math.sin) functions.
    table: list of dict with keys 'x', 'approx', 'exact'
    save_path: full path to save PNG file
    """
    if not table:
        print("No data to plot.")
        return
    
    x_vals = [row['x'] for row in table]
    approx_vals = [row['approx'] for row in table]
    exact_vals = [row['exact'] for row in table]
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(x_vals, approx_vals, 'ro-', label="Series approximation", markersize=4, linewidth=1.5)
    
    x_fine = np.linspace(min(x_vals), max(x_vals), 300)
    exact_fine = np.sin(x_fine)
    plt.plot(x_fine, exact_fine, 'b-', label="math.sin(x)", linewidth=2)
    
    plt.xlabel("x (radians)", fontsize=12)
    plt.ylabel("sin(x)", fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend(loc="best")
    plt.grid(True, alpha=0.3)
    
    errors = [abs(row['approx'] - row['exact']) for row in table]
    max_err_idx = errors.index(max(errors))
    x_max_err = table[max_err_idx]['x']
    y_approx = table[max_err_idx]['approx']
    y_exact = table[max_err_idx]['exact']
    
    plt.annotate(f'Max error ≈ {max(errors):.2e}',
                 xy=(x_max_err, y_approx),
                 xytext=(x_max_err + 0.3, y_approx - 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9)
    
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Plot saved to {save_path}")
    plt.show()