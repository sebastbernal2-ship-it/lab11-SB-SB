import unittest
import calculator
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-3, 5), 2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(-8, -2), -6)
        self.assertEqual(calculator.subtract(2, 7), -5)
    ##########################

    ######## Partner 1

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-4, 2), -8)
        self.assertEqual(calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(-6, 3), -2)
        self.assertAlmostEqual(calculator.divide(7, 2), 3.5)
    ##########################

    ######## Partner 2

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.logarithm(5, 25), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)
    ##########################

    ######## Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(6, 8), 10)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(2), 2 ** 0.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)
    ##########################

if __name__ == '__main__':
    unittest.main()





# Do not touch this
if __name__ == "__main__":
    unittest.main()