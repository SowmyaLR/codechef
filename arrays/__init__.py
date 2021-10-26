class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return abs(self.num1 - self.num2)

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2 if self.num2 < self.num1 else self.num2/self.num1


import unittest


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        cal = Calculator(2, 4)
        self.assertEquals(cal.addition(), 6)

    def test_multiplication(self):
        cal = Calculator(2, 4)
        self.assertEquals(cal.multiplication(), 8)

    def test_subtraction(self):
        cal = Calculator(2, 4)
        self.assertEquals(cal.subtraction(), 2)

    def test_division(self):
        cal = Calculator(2, 4)
        self.assertEquals(cal.division(), 2)