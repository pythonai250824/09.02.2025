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
# run the tests : play, pytest .
# add test sub
# add test mul
# add test div