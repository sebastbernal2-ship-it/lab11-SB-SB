# https://github.com/sebastbernal2-ship-it/lab11-SB-
# Partner 1: Sebastian Bernal-Orta
# Partner 2: Sebastian Bernal-Orta

import math

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
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Input must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# --- Autograder-required short function names ---

def mul(a, b):
    return multiply(a, b)

def div(a, b):
    return divide(a, b)

def exp(a, b):
    return exponent(a, b)
