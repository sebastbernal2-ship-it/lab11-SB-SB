"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

def square_root(a):
    if a < 0:
        raise ValueError("Input must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero!")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm!")
    return math.log(b, a)

def exponent(a, b): 
    return a**b

import unittest
import calculator

def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-4, 2), -8)
        self.assertEqual(calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(-10, 2), -5)
        self.assertAlmostEqual(calculator.divide(5, 2), 2.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_hypotenuse(self):
        # Hypotenuse of sides 3, 4 is 5
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(6, 8), 10)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(2), 2 ** 0.5)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

if __name__ == "__main__":
    unittest.main()