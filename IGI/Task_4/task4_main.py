"""
Main logic for Task 4 – Rhombus drawing.
Lab 4, Task 4, Variant 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-25
"""

import os
from .figures import Color, Rhombus
from .plotter import draw_and_save_rhombus
from .utils import get_rhombus_parameters, safe_float_input, safe_string_input

def run():
    print("\n=== TASK 4: RHOMBUS CONSTRUCTION (Variant 6) ===\n")
    
    while True:
        # Get parameters from user
        side, angle_deg, color_name, label = get_rhombus_parameters()
        
        # Create objects
        color = Color(color_name)
        rhombus = Rhombus(side, angle_deg, color)
        
        # Display figure info
        print("\n" + rhombus.get_info())
        
        # Prepare save path inside task4/data/
        data_dir = os.path.join(os.path.dirname(__file__), "data")
        os.makedirs(data_dir, exist_ok=True)
        save_path = os.path.join(data_dir, "rhombus.png")
        
        # Draw and save
        draw_and_save_rhombus(rhombus, label, save_path, show=True)
        
        
        again = input("\nDo you want to draw another rhombus? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting Task 4.")
            break

if __name__ == "__main__":
    run()