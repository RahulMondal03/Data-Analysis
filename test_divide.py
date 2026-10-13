"""Tests for :func:`divide.divide`."""

import pytest

from divide import divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (7, 2, 3.5),
        (-9, 3, -3.0),
        (0, 5, 0.0),
        (1.5, 0.5, 3.0),
    ],
    ids=["whole", "fractional-result", "negative", "zero-dividend", "floats"],
)
def test_divides(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("b", [0, 0.0, -0.0], ids=["int", "float", "negative-float"])
def test_zero_divisor_raises_value_error(b):
    with pytest.raises(ValueError, match="by zero"):
        divide(10, b)


def test_zero_divisor_does_not_raise_zero_division_error():
    with pytest.raises(ValueError) as info:
        divide(10, 0)
    assert not isinstance(info.value, ZeroDivisionError)
    assert str(info.value) == "cannot divide 10 by zero"
