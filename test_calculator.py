import time

import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"

# pip install pytest
# option 1- run the tests : play
# option 2- run the tests
#         in the Terminal : pytest .
# add test sub
# add test mul
# add test div