"""
Funcspinner: Specific Model Analysis & Subset Testing
=====================================================

DESCRIPTION:
    An example workflow for applying a single Funcspinner model to real-world 
    economic data. It performs a full-dataset fit, calculates statistical 
    accuracy (R², Std Error), and repeats the process on a data subset 
    (Testing Mode) to evaluate model stability.

HOW TO USE:
    1. Set 'FUNCTION_NAME' to your desired model (e.g., 'polyRatio44').
    2. Run the script: python example_funcspinner.py
    3. View the console output for optimized parameters and the generated 
       comparison plot.

AUTHOR: Stephen Joseph (@sjosephnyc1987)
LICENSE: GNU GPL v3.0
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import inspect
import funcspinner as fs

# --- Configuration ---
DATA_URL = 'https://raw.githubusercontent.com/sjosephnyc1987/datasets/main/TradingEconimicsWorldDataMarch2022.csv'
FUNCTION_NAME = "polyRatio44"
MAX_EVALS = 500000

def calculate_metrics(y_true, y_pred):
    """Calculates Standard Error and R-squared."""
    residuals = y_true - y_pred
    rss = np.sum(residuals**2)
    std_err = np.sqrt(rss / len(y_true))
    
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    r_squared = 1 - (rss / ss_tot)
    return std_err, r_squared

def run_example():
    # 1. Data Acquisition
    print(f"Fetching data from: {DATA_URL}...")
    df = pd.read_csv(DATA_URL)
    pdf = df[['Inflation rate', 'Jobless rate']].dropna()
    x_full = pdf['Inflation rate'].values
    y_full = pdf['Jobless rate'].values

    # 2. Get Objective Function
    obj_func = fs.get_function(FUNCTION_NAME)
    print("\n" + "-"*30)
    print(f"Model: {FUNCTION_NAME}")
    print(inspect.getsource(obj_func))
    print("-"*30)

    # 3. Fit Model to Full Dataset
    popt, _ = curve_fit(obj_func, x_full, y_full, maxfev=MAX_EVALS)
    
    # Calculate performance
    y_pred_full = obj_func(x_full, *popt)
    std_err, r2 = calculate_metrics(y_full, y_pred_full)

    # Print Results
    coeffs = list("abcdefghijk")
    print(f"\n--- Full Fit: {FUNCTION_NAME} ---")
    for i, val in enumerate(popt):
        print(f"{coeffs[i]} = {val:.6f}")
    print(f"Standard Error: {std_err:.4f}")
    print(f"R-Squared: {r2:.4f}")

    # 4. Testing Mode (Subset Analysis: Inflation > 2)
    print("\n" + "*"*10 + " ENTERING TESTING MODE (Inflation > 2) " + "*"*10)
    pdf_test = pdf[pdf['Inflation rate'] > 2]
    x_test = pdf_test['Inflation rate'].values
    y_test = pdf_test['Jobless rate'].values

    popt_test, _ = curve_fit(obj_func, x_test, y_test, maxfev=MAX_EVALS)
    y_pred_test = obj_func(x_test, *popt_test)
    std_err_t, r2_t = calculate_metrics(y_test, y_pred_test)

    print(f"Subset samples: {len(x_test)}")
    print(f"Subset Std Error: {std_err_t:.4f}")
    print(f"Subset R-Squared: {r2_t:.4f}")

    # 5. Visualization
    plt.figure(figsize=(12, 6))
    
    # Plot 1: Raw Data and Full Fit
    plt.scatter(x_full, y_full, color='gray', alpha=0.3, label='Raw Data')
    
    # Generate smooth line for fit
    x_mono = np.linspace(x_full.min(), x_full.max(), 500)
    plt.plot(x_mono, obj_func(x_mono, *popt), 'r--', linewidth=2, label='Full Fit')
    
    # Plot 2: Test Subset Fit
    x_mono_test = np.linspace(x_test.min(), x_test.max(), 500)
    plt.plot(x_mono_test, obj_func(x_mono_test, *popt_test), 'g:', linewidth=2, label='Subset Fit (Inf > 2)')

    plt.xlabel("Inflation Rate (%)")
    plt.ylabel("Jobless Rate (%)")
    plt.title(f"Funcspinner Analysis: {FUNCTION_NAME}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    run_example()





