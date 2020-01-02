import pytest

from fib.fibonacci import FibonacciCalculator

_calculator= FibonacciCalculator()

@pytest.fixture
def calculator_setup():
    return _calculator

def test_hidden_1(calculator_setup):
    assert calculator_setup.calculate(14) == 377
 
def test_hidden_2(calculator_setup):
    assert calculator_setup.calculate(15) == 610

def test_hidden_3(calculator_setup):
    assert calculator_setup.calculate(18) == 2584

def test_hidden_4(calculator_setup):
    assert calculator_setup.calculate(19) == 4181