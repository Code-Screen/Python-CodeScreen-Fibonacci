import unittest

from fib.fibonacci import calculate

class FibonacciHiddenTest(unittest.TestCase):

    def test_hidden_1(self):
        self.assertEqual(calculate(14), 377)

    def test_hidden_2(self):
        self.assertEqual(calculate(15), 610)

    def test_hidden_3(self):
        self.assertEqual(calculate(18), 2584)

    def test_hidden_4(self):
        self.assertEqual(calculate(19), 4181)
