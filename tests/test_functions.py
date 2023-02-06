import sys
import os
import pytest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(
        __file__), os.path.pardir)) + '/src'
)

from my_math.functions import *

def test_factorial() -> None:
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800
