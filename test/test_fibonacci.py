import unittest

from fib.fibonacci import calculate

class FibonacciTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(calculate(0), 0)

    def test_2(self):
        self.assertEqual(calculate(5), 5)

    def test_3(self):
        self.assertEqual(calculate(20), 6765)

    def test_4(self):
        self.assertEqual(calculate(25), 75025)
