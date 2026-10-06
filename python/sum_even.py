"""Utility for summing the even numbers in a list."""

from numbers import Integral


def sum_even_numbers(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Every element must be an integer (``int`` or another integral type such
    as ``numpy.int64``). Booleans are rejected even though ``bool`` subclasses
    ``int``, and floats are rejected even when they are whole numbers.

    Raises:
        TypeError: if any element is not an integer.

    >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even_numbers([-4, -3, 0, 7])
    -4
    >>> sum_even_numbers([])
    0
    >>> sum_even_numbers([2, 4.0])
    Traceback (most recent call last):
        ...
    TypeError: element at index 1 is not an integer: 4.0 (float)
    >>> sum_even_numbers([2, "4"])
    Traceback (most recent call last):
        ...
    TypeError: element at index 1 is not an integer: '4' (str)
    >>> sum_even_numbers([True, 2])
    Traceback (most recent call last):
        ...
    TypeError: element at index 0 is not an integer: True (bool)
    """
    total = 0
    for index, n in enumerate(numbers):
        if isinstance(n, bool) or not isinstance(n, Integral):
            raise TypeError(
                f"element at index {index} is not an integer: "
                f"{n!r} ({type(n).__name__})"
            )
        if n % 2 == 0:
            total += n
    return total


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
