# This is a test script that is used 
# to verify that all functions are working correctly and handling edge cases (like negative numbers in positive-only domains),
# ------------------------------------------


import numpy as np
import pytest
import funcspinner as fs

def test_linear_output():
    """Verify simple linear calculation."""
    x = np.array([1, 2, 3])
    # a=1, b=2 -> 1 + 2*x
    result = fs.simple_linear(x, 1, 2)
    expected = np.array([3, 5, 7])
    np.testing.assert_array_equal(result, expected)

def test_domain_error():
    """Ensure functions raise ValueError for invalid x values."""
    x_invalid = np.array([-1, 0, 1])
    with pytest.raises(ValueError):
        fs.simple_power(x_invalid, 1, 1)

def test_segmented_models():
    """Test if segmented models return valid numeric arrays."""
    x = np.linspace(0, 10, 50)
    # Testing quadratic_linear transition
    result = fs.quadratic_linear(x, 1, 1, 0.5, 5, 0.2, 0.1)
    assert result.shape == (50,)
    assert not np.isnan(result).any()

def test_registry_access():
    """Ensure the dictionary lookup works."""
    model = fs.get_function("michaelisMenten3")
    assert callable(model)
    
if __name__ == "__main__":
    # Manual verification if not using pytest
    print("Running manual verification...")
    test_linear_output()
    print("Linear check: PASSED")
    try:
        test_domain_error()
        print("Domain validation: PASSED")
    except Exception as e:
        print(f"Domain validation: FAILED ({e})")
