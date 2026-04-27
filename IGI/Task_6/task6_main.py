"""
Main execution for Task 6 (Pandas, variant 6).
Lab 4, Task 6.
Developer: Ivan Leuchyshyn
Date: 2026-04-27
"""

import os
import pandas as pd
from .auto_analyzer import CarDataAnalyzer
from .utils import safe_bool_input

def save_results(analyzer, results_text: str, filepath: str):
    """Save analysis results to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=== TASK 6 RESULTS (Variant 6) ===\n")
        f.write(results_text)
        if analyzer.data is not None:
            f.write("\n\nFirst 5 rows of dataset:\n")
            f.write(analyzer.data.head().to_string())
        f.write("\n\n--- create_car_features_df() ---\n")
        f.write(analyzer.create_car_features_df().to_string())

def run():
    print("\n=== TASK 6: PANDAS AUTOMOBILE ANALYSIS (Variant 6) ===\n")
    
    analyzer = CarDataAnalyzer()
    
    response = safe_bool_input("Load the Automobile dataset from UCI? (y/n): ")
    if response:
        analyzer.load_data()
        if analyzer.data is None:
            print("Failed to load data. Exiting Task 6.")
            return
        print(f"Dataset loaded: {analyzer.data.shape[0]} rows, {analyzer.data.shape[1]} columns")
    else:
        print("Proceeding without main dataset. Only demonstration tasks will run.")
    
    print("\n--- Variant-specific tasks ---")
    car_features = analyzer.create_car_features_df()
    print("create_car_features_df():\n", car_features)
    
    if analyzer.data is not None:
        avg_price = analyzer.average_price_max_cylinders()
        print(f"\nAverage price of cars with max cylinders: {avg_price}")
        
        ratio = analyzer.mpg_ratio_expensive_to_cheap()
        print(f"Ratio of average city-mpg (expensive/cheap): {ratio}")
        
        engine_series = analyzer.data['engine-size'].dropna()
        avg_engine_size = engine_series.mean()
        print(f"Average engine size (Volume proxy): {avg_engine_size:.2f}")
    else:
        avg_price = ratio = avg_engine_size = None
    
    analyzer.demo_series_and_dataframe()
    
    results_lines = []
    results_lines.append("1. car_features DataFrame:")
    results_lines.append(car_features.to_string())
    if analyzer.data is not None:
        results_lines.append(f"\n2. Average price of cars with max cylinders: {avg_price}")
        results_lines.append(f"3. Ratio of city-mpg (expensive/cheap quartiles): {ratio}")
        results_lines.append(f"4. Average engine size (Volume series mean): {avg_engine_size:.2f}")
    else:
        results_lines.append("\nMain dataset not loaded, statistics unavailable.")
    
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    results_path = os.path.join(data_dir, "results.txt")
    save_results(analyzer, "\n".join(results_lines), results_path)
    print(f"\nResults saved to: {results_path}")
    
    again = safe_bool_input("\nDo you want to run again with potential different dataset? (y/n): ")
    if again:
        run()
    else:
        print("Exiting Task 6.")

if __name__ == "__main__":
    run()