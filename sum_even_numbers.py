"""Utility for summing the even numbers in a sequence."""

from typing import Iterable


def sum_even_numbers(numbers: Iterable[float]) -> float:
    """Return the sum of the even numbers in ``numbers``.

    Values that are not evenly divisible by 2 are ignored, as are odd
    numbers. An empty input (or one with no even numbers) returns 0.

    >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even_numbers([1, 3, 5])
    0
    >>> sum_even_numbers([])
    0
    >>> sum_even_numbers([-2, -1, 0, 7])
    -2
    """
    return sum(number for number in numbers if number % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
