"""Utility for summing the even numbers in a list."""


def sum_even_numbers(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Works with ints and floats: whole-number floats such as 4.0 count as even,
    while fractional values such as 3.5 are skipped.

    >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even_numbers([-4, -3, 0, 7])
    -4
    >>> sum_even_numbers([])
    0
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
