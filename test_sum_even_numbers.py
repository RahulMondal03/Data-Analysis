"""Tests for :func:`sum_even_numbers.sum_even_numbers`."""

import math

import pytest

from sum_even_numbers import sum_even_numbers


class TestValidInput:
    """Cases where every value is a whole number, so nothing is rejected."""

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1, 2, 3, 4, 5, 6], 12),
            ([2, 4, 6], 12),
            ([10], 10),
            ([1, 2, 2, 3, 4, 4], 12),
        ],
        ids=["mixed", "all-even", "single-even", "with-duplicates"],
    )
    def test_normal_lists(self, numbers, expected):
        assert sum_even_numbers(numbers) == expected

    def test_empty_list_is_zero(self):
        assert sum_even_numbers([]) == 0

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([1, 3, 5], 0),
            ([7], 0),
            ([-1, -3, 9, 11], 0),
        ],
        ids=["odds", "single-odd", "negative-odds"],
    )
    def test_all_odd_input_is_zero(self, numbers, expected):
        assert sum_even_numbers(numbers) == expected

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([-4, -3, 0, 7], -4),
            ([0], 0),
            ([0, 1, 2], 2),
            ([-2, -4, -6], -12),
            ([-2, 2], 0),
            ([-5, -3, -1], 0),
        ],
        ids=[
            "negatives-and-zero",
            "zero-alone",
            "zero-is-even",
            "all-negative-even",
            "negatives-cancel",
            "all-negative-odd",
        ],
    )
    def test_negatives_and_zero(self, numbers, expected):
        assert sum_even_numbers(numbers) == expected

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([2.0, 3.0, 4.0], 6),
            ([-4.0, 0.0, 5.0], -4),
        ],
        ids=["positive-whole-floats", "negative-whole-floats"],
    )
    def test_whole_valued_floats_are_accepted(self, numbers, expected):
        """A float holding a whole number has a parity, so it counts."""
        assert sum_even_numbers(numbers) == expected

    def test_result_is_an_int_even_for_float_input(self):
        result = sum_even_numbers([2.0, 4.0])
        assert result == 6
        assert isinstance(result, int)

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            (range(1, 11), 30),
            ((1, 2, 3, 4), 6),
            ({1, 2, 3, 4}, 6),
            (iter([1, 2, 3, 4]), 6),
        ],
        ids=["range", "tuple", "set", "generator"],
    )
    def test_accepts_any_iterable(self, numbers, expected):
        assert sum_even_numbers(numbers) == expected


class TestRejectsNonIterableArgument:
    """The argument itself must be an iterable of numbers."""

    @pytest.mark.parametrize(
        "argument",
        [42, 4.0, None, object()],
        ids=["int", "float", "none", "object"],
    )
    def test_non_iterable_argument_raises_type_error(self, argument):
        with pytest.raises(TypeError, match="numbers must be iterable"):
            sum_even_numbers(argument)

    @pytest.mark.parametrize(
        "argument",
        ["246", b"246", bytearray(b"246")],
        ids=["str", "bytes", "bytearray"],
    )
    def test_string_like_argument_raises_type_error(self, argument):
        """Strings are iterable, so they are rejected explicitly rather than
        being summed character by character."""
        with pytest.raises(TypeError, match="must be an iterable of numbers"):
            sum_even_numbers(argument)

    def test_string_argument_error_names_its_type(self):
        with pytest.raises(TypeError) as info:
            sum_even_numbers("246")
        assert "not a str" in str(info.value)


class TestRejectsNonNumericValues:
    """Values that are not real numbers raise ``TypeError``."""

    @pytest.mark.parametrize(
        "value, type_name",
        [
            ("four", "str"),
            (None, "NoneType"),
            (2 + 3j, "complex"),
            ([4], "list"),
            ({"n": 4}, "dict"),
        ],
        ids=["str", "none", "complex", "list", "dict"],
    )
    def test_non_numeric_value_raises_type_error(self, value, type_name):
        with pytest.raises(TypeError) as info:
            sum_even_numbers([2, value, 6])
        message = str(info.value)
        assert "numbers[1] must be an int or float" in message
        assert f"got {type_name}" in message

    @pytest.mark.parametrize(
        "value",
        [True, False],
        ids=["true", "false"],
    )
    def test_bool_is_rejected(self, value):
        """``bool`` subclasses ``int``, but summing it is a mistake, not intent."""
        with pytest.raises(TypeError, match="numbers\\[1\\] must be an int or float"):
            sum_even_numbers([2, value])

    def test_error_names_the_offending_index(self):
        with pytest.raises(TypeError, match="numbers\\[3\\]"):
            sum_even_numbers([2, 4, 6, "eight"])


class TestRejectsNonWholeNumbers:
    """Numbers without a parity raise ``ValueError``."""

    @pytest.mark.parametrize(
        "value",
        [4.5, -0.5, 1e-3],
        ids=["positive-fraction", "negative-fraction", "tiny-fraction"],
    )
    def test_fractional_float_raises_value_error(self, value):
        with pytest.raises(ValueError) as info:
            sum_even_numbers([2, value, 6])
        assert "numbers[1] must be a whole number" in str(info.value)

    @pytest.mark.parametrize(
        "value",
        [math.inf, -math.inf, math.nan],
        ids=["inf", "negative-inf", "nan"],
    )
    def test_non_finite_float_raises_value_error(self, value):
        with pytest.raises(ValueError, match="must be a whole number"):
            sum_even_numbers([2, value])

    def test_value_error_names_the_offending_index(self):
        with pytest.raises(ValueError, match="numbers\\[2\\]"):
            sum_even_numbers([2, 4, 6.5])


class TestStrictMode:
    """``strict=False`` skips invalid values instead of raising."""

    def test_lenient_mode_skips_invalid_values(self):
        assert sum_even_numbers([2, "four", 4.5, 6], strict=False) == 8

    def test_lenient_mode_skips_bools_and_non_finite_floats(self):
        assert sum_even_numbers([2, True, math.nan, math.inf, 4], strict=False) == 6

    def test_lenient_mode_returns_zero_when_everything_is_invalid(self):
        assert sum_even_numbers(["a", None, 1.5], strict=False) == 0

    def test_strict_is_the_default(self):
        with pytest.raises(TypeError):
            sum_even_numbers([2, "four"])

    def test_strict_true_matches_the_default(self):
        assert sum_even_numbers([1, 2, 3, 4], strict=True) == 6

    def test_strict_is_keyword_only(self):
        with pytest.raises(TypeError):
            sum_even_numbers([1, 2], False)

    def test_lenient_mode_still_rejects_a_non_iterable_argument(self):
        """``strict`` governs the values, not the argument itself."""
        with pytest.raises(TypeError, match="numbers must be iterable"):
            sum_even_numbers(42, strict=False)
