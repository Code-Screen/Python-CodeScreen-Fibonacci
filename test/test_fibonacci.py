import pytest

from fib.fibonacci import FibonacciCalculator

_calculator= FibonacciCalculator()

@pytest.fixture
def calculator_setup():
    return _calculator

def test_1(calculator_setup):
    assert calculator_setup.calculate(0) == 0
 
def test_2(calculator_setup):
    assert calculator_setup.calculate(5) == 5

def test_3(calculator_setup):
    assert calculator_setup.calculate(20) == 6765

def test_4(calculator_setup):
    assert calculator_setup.calculate(25) == 75025