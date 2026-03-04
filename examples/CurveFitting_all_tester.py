"""
Funcspinner: Automated Model Selection & Economic Analysis Engine
================================================================

DESCRIPTION:
    This script is a diagnostic "spinner" that fetches real-world economic 
    data and attempts to fit over 40 different mathematical models to it. 
    It compares models using R-squared, Standard Error, AIC, and Residual 
    Norms to identify the best mathematical representation of the data.

HOW TO USE:
    1. Ensure 'funcspinner.py' is in the same directory or installed via pip.
    2. Install dependencies: pip install numpy pandas scipy matplotlib
    3. Run this script directly: python fit_all_models.py
    4. The script will fetch the Trading Economics dataset, perform the 
       matrix fit, and output a ranked leaderboard to the console.
    5. A matplotlib window will open showing the raw data vs. the top-ranked model.

AUTHOR: Stephen Joseph (@sjosephnyc1987)
LICENSE: GNU GPL v3.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import funcspinner as fs  # Your modernized library

# --- Configuration ---
DATA_URL = 'https://raw.githubusercontent.com/sjosephnyc1987/datasets/main/TradingEconimicsWorldDataMarch2022.csv'
MAX_EVALS = 500000  # High limit for complex economic data

def run_hybrid_analysis():
    # 1. Data Acquisition
    try:
        df = pd.read_csv(DATA_URL)
        # Focus on Inflation vs Jobless (The Phillips Curve Relationship)
        pdf = df[['Inflation rate', 'Jobless rate']].dropna()
        x = pdf['Inflation rate'].values
        y = pdf['Jobless rate'].values
    except Exception as e:
        print(f"Critcal Error: Could not load dataset. {e}")
        return

    print("\n" + "="*60)
    print("  FUNCSPINNER MATRIX: RANKING OBJECTIVE FUNCTIONS")
    print("="*60 + "\n")

    models = fs.get_all_functions()
    results_list = []

    # 2. The "Spin" Loop
    for name, func in models.items():
        try:
            # Determine number of parameters dynamically
            num_params = func.__code__.co_argcount - 1
            
            # Perform fit using Stephen's high maxfev logic
            popt, _ = curve_fit(func, x, y, maxfev=MAX_EVALS)
            
            # Predict and Calculate Metrics
            y_pred = func(x, *popt)
            residuals = y - y_pred
            ss_res = np.sum(residuals**2)
            ss_tot = np.sum((y - np.mean(y))**2)
            
            # --- Scoring ---
            r2 = 1 - (ss_res / ss_tot)
            std_error = np.sqrt(ss_res / len(y))
            # AIC penalizes for extra parameters to prevent overfitting
            aic = len(y) * np.log(ss_res/len(y)) + 2 * (num_params + 1)
            # Linalg Norm tracks the "magnitude" of the model's predictions
            norm_val = np.linalg.norm(y_pred)

            results_list.append({
                'Model': name, 
                'R2': round(r2, 4), 
                'AIC': round(aic, 2), 
                'Std_Error': round(std_error, 4),
                'Norm': round(norm_val, 2)
            })

        except Exception:
            # Skip models that fail to converge for this specific dataset
            continue

    # 3. Create Leaderboard (Sorted by Std Error as in your original version)
    results_df = pd.DataFrame(results_list).sort_values(by='Std_Error')
    
    print(results_df.to_string(index=False))
    print("\n" + "="*60)

    # 4. Visualization
    if not results_df.empty:
        best_name = results_df.iloc[0]['Model']
        best_func = fs.get_function(best_name)
        
        # Re-fit the winner for a smooth plot line
        popt_final, _ = curve_fit(best_func, x, y, maxfev=MAX_EVALS)
        x_smooth = np.linspace(x.min(), x.max(), 300)
        y_smooth = best_func(x_smooth, *popt_final)

        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, alpha=0.4, label='Actual Data (Inflation/Jobless)', color='teal')
        plt.plot(x_smooth, y_smooth, color='red', linewidth=2.5, 
                 label=f'Best Fit: {best_name} (R²={results_df.iloc[0]["R2"]})')
        
        plt.title(f"Funcspinner Leaderboard: Best Model - {best_name}")
        plt.xlabel("Inflation Rate (%)")
        plt.ylabel("Jobless Rate (%)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    run_hybrid_analysis()
