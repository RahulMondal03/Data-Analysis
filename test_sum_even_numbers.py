"""Tests for sum_even_numbers."""

import unittest
from fractions import Fraction

from sum_even_numbers import sum_even_numbers


class SumEvenNumbersTest(unittest.TestCase):
    def test_sums_only_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)

    def test_handles_negatives_and_zero(self):
        self.assertEqual(sum_even_numbers([-4, -3, 0, 7]), -4)

    def test_returns_zero_when_no_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 3, 5]), 0)

    def test_returns_zero_for_empty_input(self):
        self.assertEqual(sum_even_numbers([]), 0)

    def test_accepts_any_iterable(self):
        self.assertEqual(sum_even_numbers(range(1, 11)), 30)
        self.assertEqual(sum_even_numbers((2, 3, 4)), 6)

    def test_accepts_whole_valued_floats_as_integers(self):
        self.assertEqual(sum_even_numbers([2, 4.0]), 6)
        self.assertEqual(sum_even_numbers([Fraction(4, 2)]), 2)

    def test_rejects_fractional_numbers(self):
        with self.assertRaisesRegex(ValueError, "index 1 is not an integer"):
            sum_even_numbers([1, 3.5])
        with self.assertRaises(ValueError):
            sum_even_numbers([Fraction(1, 2)])

    def test_rejects_non_finite_numbers(self):
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "not a finite number"):
                    sum_even_numbers([2, value])

    def test_rejects_non_numeric_items(self):
        for value in ("2", None, [4], {}, 2 + 0j):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "is not a number"):
                    sum_even_numbers([1, value])

    def test_rejects_booleans(self):
        with self.assertRaisesRegex(TypeError, "is a bool"):
            sum_even_numbers([2, True])

    def test_rejects_non_iterable_argument(self):
        for value in (42, None, object()):
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError, "expected an iterable"):
                    sum_even_numbers(value)

    def test_rejects_string_argument(self):
        with self.assertRaisesRegex(TypeError, "expected an iterable"):
            sum_even_numbers("24")

    def test_error_names_the_offending_index(self):
        with self.assertRaisesRegex(TypeError, "index 2"):
            sum_even_numbers([1, 2, "x"])


if __name__ == "__main__":
    unittest.main()
