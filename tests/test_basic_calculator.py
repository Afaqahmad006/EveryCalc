
import unittest

from basic_calculator import calculate


class TestBasicCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(8, "+", 2), 10)

    def test_subtraction(self):
        self.assertEqual(calculate(8, "-", 2), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(8, "*", 2), 16)

    def test_division(self):
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_percentage(self):
        self.assertEqual(calculate(200, "%", 10), 20)

    def test_power(self):
        self.assertEqual(calculate(2, "^", 3), 8)

    def test_square_root(self):
        self.assertEqual(calculate(25, "sqrt"), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(8, "/", 0)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            calculate(-4, "sqrt")

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(8, "?", 2)


if __name__ == "__main__":
    unittest.main()

