"""Utility for summing the even numbers in a list."""

import math
from numbers import Integral, Real


def _as_integer(value, index):
    """Return ``value`` as an ``int``, rejecting anything that is not one.

    Whole-valued floats such as ``4.0`` are accepted and converted, since they
    represent integers; fractional values such as ``3.5`` are not.

    Args:
        value: The value to validate.
        index: Position of the value in the input, used in error messages.

    Returns:
        The value as an ``int``.

    Raises:
        TypeError: If the value is not a real number.
        ValueError: If the value is a real number but not a finite integer.
    """
    # bool is a subclass of int, but True/False are not numbers a caller means
    # to sum, so they are rejected rather than silently counted as 1 and 0.
    if isinstance(value, bool):
        raise TypeError(f"item at index {index} is a bool, not a number: {value!r}")
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        if not math.isfinite(value):
            raise ValueError(f"item at index {index} is not a finite number: {value!r}")
        if value != int(value):
            raise ValueError(f"item at index {index} is not an integer: {value!r}")
        return int(value)
    raise TypeError(
        f"item at index {index} is not a number: {value!r} "
        f"(type {type(value).__name__})"
    )


def sum_even_numbers(numbers):
    """Return the sum of the even integers in ``numbers``.

    Args:
        numbers: An iterable of integers. Whole-valued floats (``4.0``) are
            accepted; fractional values (``3.5``) are not.

    Returns:
        The sum, as an ``int``, of every value that divides evenly by 2.
        Returns 0 when the input is empty or contains no even numbers.

    Raises:
        TypeError: If ``numbers`` is not an iterable, or if any item is not a
            real number.
        ValueError: If any item is a real number but not a finite integer.
    """
    # Strings are iterable, so without this check "24" would be reported as two
    # bad items rather than one bad argument.
    if isinstance(numbers, (str, bytes, bytearray)):
        raise TypeError(
            f"expected an iterable of integers, got {type(numbers).__name__}: {numbers!r}"
        )
    try:
        items = enumerate(numbers)
    except TypeError:
        raise TypeError(
            f"expected an iterable of integers, got {type(numbers).__name__}: {numbers!r}"
        ) from None

    total = 0
    for index, value in items:
        number = _as_integer(value, index)
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
    print(sum_even_numbers([-4, -3, 0, 7]))      # -4
    print(sum_even_numbers([1, 3, 5]))           # 0
    print(sum_even_numbers([]))                  # 0
    print(sum_even_numbers([2, 4.0]))            # 6

    for bad in ([1, "2"], [1, None], [1, 3.5], [1, float("nan")], [True], 42, "24"):
        try:
            sum_even_numbers(bad)
        except (TypeError, ValueError) as error:
            print(f"{bad!r} -> {type(error).__name__}: {error}")
