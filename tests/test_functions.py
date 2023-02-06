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
    # Zero power
    assert power(2, 0) == 1

    # Zero number and power
    try:
        assert power(0, 0)
    except ValueError:
        assert True
    else:
        assert False

    # Positive number and positive power
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(2, 4) == 16
    assert power(2, 7) == 128

    # Positive number and negative power
    assert power(2, -1) == 0.5
    assert power(2, -2) == 0.25
    assert power(2, -3) == 0.125
    assert power(2, -4) == 0.0625
    assert power(2, -7) == 0.0078125

    # Negative number and positive power
    assert power(-2, 1) == -2
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
    assert power(-2, 4) == 16
    assert power(-2, 7) == -128

    # Negative number and negative power
    assert power(-2, -1) == -0.5
    assert power(-2, -2) == 0.25
    assert power(-2, -3) == -0.125
    assert power(-2, -4) == 0.0625
    assert power(-2, -7) == -0.0078125

def test_power_positive_validation() -> None:
    try:
        assert power_positive(2, -1)
        assert power_positive(2, -2)
        assert power_positive(2, -3)
        assert power_positive(2, -4)
        assert power_positive(2, -7)
    except ValueError:
        assert True
    else:
        assert False

def test_power_negative_validation() -> None:
    try:
        assert power_negative(2, 1)
        assert power_negative(2, 2)
        assert power_negative(2, 3)
        assert power_negative(2, 4)
        assert power_negative(2, 7)
    except ValueError:
        assert True
    else:
        assert False