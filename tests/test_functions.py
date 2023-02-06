import sys
import os
import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(
        __file__), os.path.pardir)) + '/src'
)
from my_math.functions import *


def test_factorial() -> None:
    try:
        factorial(-1)
    except ValueError:
        assert True
    else:
        assert False

    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_power() -> None:
    # Zero
    assert power(2, 0) == 1
    try:
        assert power(0, 0)
    except ValueError:
        assert True
    else:
        assert False

    # Positive
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(2, 4) == 16
    assert power(2, 7) == 128

    # Negative
    assert power(2, -1) == 0.5
    assert power(2, -2) == 0.25
    assert power(2, -3) == 0.125
    assert power(2, -4) == 0.0625
    assert power(2, -7) == 0.0078125
