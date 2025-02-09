import time
from webbrowser import Error

# testabile

import pytest
from pyexpat import ExpatError

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

def test_calculator_minus_small():
    # Arrange
    a: int = 10
    b: int = 10
    expected: int = 0

    # Act
    actual: int = calculator.minus(a, b)

    # Assert
    assert expected == actual, "small numbers minus"

def test_calculator_multiply_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 1.0

    # Act
    actual: float = calculator.multiply(a, b)

    # Assert
    assert expected == actual, "small numbers multiply"

def test_calculator_div_small():
    # Arrange
    a: int = 10
    b: float = 0.1
    expected: float = 100

    # Act
    actual: float = calculator.divide(a, b)

    # Assert
    assert expected == actual, "small numbers div"

# False positive
def test_calculator_div_by_zero1():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    try:
        # next line should raise an error
        calculator.divide(a, b)

        # if we got here it's incorrect
        # the test should fail!
        # since we expected ZeroDivisionError
        # to occur
        assert False, "should raise ZeroDivisionError"

    except ZeroDivisionError as e:
        # this is the good scenario
        # an error has occurred
        # test should pass successfully
        assert True


# False positive
def test_calculator_div_by_zero2():
    # Arrange
    a: int = 10
    b: float = 0

    # Act
    # this means
    # if ZeroDivisionError will happen
    #    test will pass successfully
    #    if not- test will fail
    with pytest.raises(Exception) as ex:
        calculator.divide(a, b)

def test_check_error_happned():
    with pytest.raises(IndexError) as ex:
        calculator.make_error()

# sending input value to a functions during test
# extra feature , *bonus
def test_calculator_hello(monkeypatch):

    # black box
    monkeypatch.setattr('builtins.input', lambda _: "danny1")

    expected = "hello danny"
    result = calculator.say_hello()

    assert expected == result

