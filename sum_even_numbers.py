"""Utilities for summing the even numbers in a collection."""

from typing import Iterable


def sum_even_numbers(numbers: Iterable[float]) -> float:
    """Return the sum of the even numbers in ``numbers``.

    Args:
        numbers: An iterable of numbers (ints or floats).

    Returns:
        The sum of every even value; ``0`` when none are even.

    Examples:
        >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_even_numbers([1, 3, 5])
        0
        >>> sum_even_numbers([-4, -3, 0, 7])
        -4
    """
    return sum(number for number in numbers if number % 2 == 0)


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {sample}")
    print(f"Sum of even numbers: {sum_even_numbers(sample)}")
