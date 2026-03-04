"""
Funcspinner: Simple Model Visualizer & Exporter
==============================================

DESCRIPTION:
    This script allows a user to select a specific objective function from 
    the Funcspinner library, visualize its univariate shape, and export 
    the plot as a PNG image for documentation.

HOW TO USE:
    1. Ensure 'funcspinner.py' is in your Python path.
    2. Set 'function_name' (e.g., 'polyRatio44', 'gompertz').
    3. Run: python simple_curve_fitting.py
    4. The script prints source code, shows the plot, and saves 'model_[name].png'.

AUTHOR: Stephen Joseph (@sjosephnyc1987)
LICENSE: GNU GPL v3.0
"""

import numpy as np
import matplotlib.pyplot as plt
import inspect
import os
import funcspinner as fs 

# --- Configuration ---
function_name = "polyRatio44" 
x_start = -10
x_end = 10
default_param_value = 1.2

def visualize_and_save():
    print(f"\n--- INITIALIZING VISUALIZATION: {function_name} ---")

    # 1. Retrieve the function object
    try:
        objective_function = fs.get_function(function_name)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # 2. Inspect and Print Source Code
    print("\n[FUNCTION SOURCE CODE]")
    print("-" * 30)
    print(inspect.getsource(objective_function))
    print("-" * 30)

    # 3. Determine Parameter Count Cleanly
    sig = inspect.signature(objective_function)
    num_params = len(sig.parameters) - 1
    params = [default_param_value] * num_params

    # 4. Generate Data Points
    x = np.linspace(x_start, x_end, 500)
    
    try:
        y = objective_function(x, *params)
    except Exception as e:
        print(f"Calculation Error: {e}")
        return

    # 5. Plotting
    plt.figure(figsize=(10, 6))
    plt.axhline(0, color='pink', linewidth=1, alpha=0.5)
    plt.axvline(0, color='pink', linewidth=1, alpha=0.5)
    
    plt.plot(x, y, '--', color='green', label=f'Model behavior (params={default_param_value})')
    
    plt.title(f"Univariate Behavior: {function_name}")
    plt.xlabel("x")
    plt.ylabel(f"f(x)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='best')
    
    # --- SAVE FEATURE ---
    filename = f"model_{function_name}.png"
    plt.savefig(filename, dpi=300)
    print(f"\nSUCCESS: Plot saved as {os.path.abspath(filename)}")
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    visualize_and_save()
