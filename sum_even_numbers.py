"""Utility for summing the even numbers in a sequence."""

from typing import Iterable


def sum_even_numbers(numbers: Iterable[float]) -> float:
    """Return the sum of the even numbers in ``numbers``.

    Args:
        numbers: An iterable of numbers (ints or floats).

    Returns:
        The sum of every even value; 0 when none are even.

    Raises:
        TypeError: If an element is not a number.
    """
    total = 0
    for number in numbers:
        if isinstance(number, bool) or not isinstance(number, (int, float)):
            raise TypeError(f"expected a number, got {type(number).__name__}: {number!r}")
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
    print(sum_even_numbers([-4, -3, 0, 7]))      # -4
    print(sum_even_numbers([1, 3, 5]))           # 0
    print(sum_even_numbers([]))                  # 0
