"""Utility for summing the even numbers in a list."""


def sum_even_numbers(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Args:
        numbers: An iterable of numbers (ints or floats).

    Returns:
        The sum of every value that divides evenly by 2. Returns 0 when the
        input contains no even numbers.

    Raises:
        TypeError: If a value is not a number.
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
