import unittest
from calculator import sum, subtraction


class TestCalculator(unittest.TestCase):
    def test_5_and_5_returns_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_minus_5_and_5_returns_0(self):
        self.assertEqual(sum(-5, 5), 0)

    def test_sum_multiple_inputs(self):
        x_y_outputs = (
            (5, 5, 10),
            (-5, 5, 0),
            (1.5, 1.5, 3.0),
            (-20, -10, -30),
            (0, 0, 0),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(sum(x, y), output)

    def test_sum_x_is_not_int_or_float_raises_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('2', 2)

    def test_sum_y_is_not_int_or_float_raises_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum(2, '2')

    def test_subtraction_multiple_inputs(self):
        x_y_outputs = (
            (10, 5, 5),
            (5, 10, -5),
            (-5, -10, 5),
            (2.5, 1.5, 1.0)
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(subtraction(x, y), output)

    def test_subtraction_x_not_int_or_float_raises_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtraction('2', 2)

    def test_subtraction_y_not_int_or_float_raises_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtraction(2, '2')


unittest.main(verbosity=2)
