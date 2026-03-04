# Funcspinner 🌀

**A Comprehensive Objective Function Library for Curve Fitting**

`funcspinner` is a collection of mathematical models designed for regression analysis and curve fitting. It is optimized for use with `scipy.optimize.curve_fit` and leverages NumPy for high-performance vectorized processing.

## Features

* **Growth Models:** Gompertz, Richards, Weibull, and Bleasdale-Nelder.
* **Biological Kinetics:** Multiple Michaelis-Menten variations and Saturation Growth.
* **Segmented Regression:** Piecewise "broken-stick" models (Linear-Quadratic, etc.).
* **Specialized Models:** Power-to-power, double/triple exponentials, and logarithmic variations.
* **Standardized API:** All functions use the format `f(x, a, b, ...)` for seamless integration with SciPy.

## Installation

You can install `funcspinner` directly from GitHub (until it is on PyPI):

```bash
pip install git+https://github.com/sjosephnyc1987/funcspinner.git

```

## Quick Start

```python
import numpy as np
from scipy.optimize import curve_fit
from funcspinner import get_function

# 1. Prepare your data
x_data = np.linspace(1, 10, 50)
y_data = 2.5 * (x_data**1.5) + np.random.normal(0, 1, 50)

# 2. Get a model by name
model = get_function("richards")

# 3. Fit the model
popt, pcov = curve_fit(model, x_data, y_data)

print(f"Optimized parameters: {popt}")

```

## Available Models

You can retrieve a dictionary of all available functions using:

```python
from funcspinner import get_all_functions
print(get_all_functions().keys())

```

## License

This project is licensed under the **GNU General Public License v3 (GPL-3.0)**. See the LICENSE file for details.

## Author

**Stephen Joseph** (@sjosephnyc1987)

---

### Next Steps

1. **Local Testing:** Run `pip install -e .` in your root directory to install it in "editable" mode and test your imports.
2. **Upload to PyPI:** Would you like me to walk you through the steps of using **Twine** to upload this so people can just run `pip install funcspinner` without the GitHub link?
