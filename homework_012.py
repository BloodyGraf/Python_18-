import unittest

class Calculator:
    def summ(self, x, y):
        return x + y

    def minus(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def devine(self, x, y):
        return x / y

class TestStringMethods(unittest.TestCase):
    def test_devine_zero(self):
        Calc = Calculator()
        with self.assertRaises(Exception):
            Calc.devine(1, 0)

    def test_string(self):
        Calc = Calculator()
        with self.assertRaises(Exception):
            Calc.summ(1, 'a')

    def test_ok(self):
        Calc = Calculator()
        self.assertEqual(Calc.summ(1, 2), 3)

    def test_empty_symbol(self):
        Calc = Calculator()
        with self.assertRaises(Exception):
            Calc.devine(1, '')

unittest.main()