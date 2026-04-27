"""
Plotting functions for geometric figures using matplotlib.
Lab 4, Task 4.
Developer: Ivan Leuchyshyn
Date: 2026-04-25
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import os

def draw_and_save_rhombus(rhombus, text_label: str, save_path: str, show: bool = True):
    """
    Draw the rhombus, fill with its color, add a text label, and save/show.
    """
    vertices = rhombus.get_vertices()
    color_name = rhombus.color.name
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    polygon = Polygon(vertices, closed=True, facecolor=color_name, edgecolor='black', linewidth=1.5, alpha=0.7)
    ax.add_patch(polygon)
    
    all_x = [v[0] for v in vertices]
    all_y = [v[1] for v in vertices]
    margin = max(abs(max(all_x)), abs(max(all_y))) * 0.2
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    ax.set_aspect('equal')
    
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    
    ax.text(0, max(all_y) + margin/2, text_label, ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_title(f"Rhombus (side={rhombus.side:.2f}, angle={rhombus.acute_angle_deg:.1f}°)")
    ax.grid(True, alpha=0.3)
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Figure saved to {save_path}")
    
    if show:
        plt.show()
    else:
        plt.close()