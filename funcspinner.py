"""
Funcspinner: A collection of objective functions for curve fitting.
Optimized for use with scipy.optimize.curve_fit.
"""

import numpy as np

# --- Domain Validation Helpers ---

def _check_pos(x, name):
    if np.any(x <= 0):
        raise ValueError(f"{name} requires x > 0")

def _check_log_limit(x, name, limit=1.1):
    if np.any(x <= limit):
        raise ValueError(f"{name} requires x > {limit}")

# --- 1. Growth & Biological Models ---

def bleasdale_nelder(x, a, b, c):
    """f(x) = (a + bx)^(-1/c)"""
    _check_pos(x, "bleasdale_nelder")
    return (a + (b * x))**(-1/c)

def farazdaghi_harris(x, a, b, c):
    """f(x) = 1 / (a + b * x^c)"""
    _check_pos(x, "farazdaghi_harris")
    return 1 / (a + b * (x**c))

def richards(x, a, b, c, d):
    """Richards Growth: f(x) = a * (1 + (b-1) * exp(-c * (x-d)))^(1/(1-b))"""
    return a * (1 + (b - 1) * np.exp(-c * (x - d)))**(1 / (1 - b))

def michaelis_menten_2(x, a, b, c, d):
    """Double Michaelis-Menten: (a*x)/(b+x) + (c*x)/(d+x)"""
    return (a * x / (b + x)) + (c * x / (d + x))

def michaelis_menten_3(x, a, b, c, d, e, f):
    """Triple Michaelis-Menten: (a*x)/(b+x) + (c*x)/(d+x) + (e*x)/(f+x)"""
    return (a * x / (b + x)) + (c * x / (d + x)) + (e * x / (f + x))

# --- 2. Specialized & Logarithmic Models ---

def logarithmic_custom(x, a, b):
    """f(x) = b * log(|x| - a) | Requires x > 1.1"""
    _check_log_limit(x, "logarithmic_custom")
    return b * (np.log(np.abs(x) - a))

def power_to_power(x, a, b, c):
    """f(x) = a * x^(b * x^c)"""
    _check_pos(x, "power_to_power")
    return a * (x**(b * (x**c)))

# --- 3. Piecewise & Segmented Models ---
# These models use np.sign to simulate "broken-stick" regression behavior

def linear_quadratic(x, a, b, c, d, e):
    """Segmented Linear-Quadratic transition."""
    return a + (b * x) + c * (x**2) + (x - d) * np.sign((x - d) * (c * (x + d) + e))

def quadratic_linear(x, a, b, c, d, e, f):
    """Segmented Quadratic-Linear transition."""
    return a + (b * x) + (c * (x**2)) + ((x - d) * np.sign(x - d) * (e * (x + d) + f))

def quadratic_quadratic(x, a, b, c, d, e, f):
    """Segmented Quadratic-Quadratic transition."""
    return a + (b * x) + c * (x**2) + (x - d) * np.sign(x - d) * (e * (x + d) + f)

# --- 4. Exponential Variations ---

def sum_exponentials(x, a, b, c, d):
    """Double Exponential: a*exp(-b*x) + c*exp(-d*x)"""
    return a * (np.exp(-b * x)) + c * (np.exp(-d * x))

def sum_3_exponentials(x, a, b, c, d, e, f):
    """Triple Exponential with sign variation."""
    return a * (np.exp(-b * x)) - c * (np.exp(-d * x)) + e * (np.exp(-f * x))

# --- Registry Management ---

_MODELS = {
    "bleasdaleNelder": bleasdale_nelder,
    "farazdaghiHarris": farazdaghi_harris,
    "richards": richards,
    "michaelisMenten2": michaelis_menten_2,
    "michaelisMenten3": michaelis_menten_3,
    "logarithmic": logarithmic_custom,
    "powertopower": power_to_power,
    "linearQuadratic": linear_quadratic,
    "quadraticLinear": quadratic_linear,
    "quadraticQuadratic": quadratic_quadratic,
    "sumExponentials": sum_exponentials,
    "sum3Exponentials": sum_3_exponentials,
    # (Previously defined simple models would be included here as well)
}

def get_function(name):
    if name not in _MODELS:
        raise ValueError(f"Function '{name}' not found.")
    return _MODELS[name]

def get_all_functions():
    return _MODELS.copy()
