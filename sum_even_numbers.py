"""Utilities for summing the even numbers in a collection."""

import math
from typing import Iterable, Union

Number = Union[int, float]


def sum_even_numbers(numbers: Iterable[Number], *, strict: bool = True) -> int:
    """Return the sum of the even numbers in ``numbers``.

    Only whole numbers have a parity, so each value must be an ``int`` or a
    ``float`` holding a whole number (``4.0`` counts, ``4.5`` does not).
    ``bool`` is rejected even though it subclasses ``int``: summing ``True``
    is almost always a mistake rather than an intent.

    Args:
        numbers: An iterable of numbers.
        strict: When ``True`` (the default), an invalid value raises. When
            ``False``, invalid values are skipped and the valid ones are
            still summed.

    Returns:
        The sum of every even value, as an ``int``; ``0`` when none are even.

    Raises:
        TypeError: If ``numbers`` is not iterable (a string counts as not
            iterable here, since iterating one yields characters), or -- in
            strict mode -- if it contains a value that is not a real number.
        ValueError: In strict mode, if it contains a number that is not whole
            (a fractional float, infinity, or NaN).

    Examples:
        >>> sum_even_numbers([1, 2, 3, 4, 5, 6])
        12
        >>> sum_even_numbers([1, 3, 5])
        0
        >>> sum_even_numbers([-4, -3, 0, 7])
        -4
        >>> sum_even_numbers([2.0, 3.0, 4.0])
        6
        >>> sum_even_numbers([2, "four", 6])
        Traceback (most recent call last):
            ...
        TypeError: numbers[1] must be an int or float, got str: 'four'
        >>> sum_even_numbers([2, 4.5, 6])
        Traceback (most recent call last):
            ...
        ValueError: numbers[1] must be a whole number, got 4.5
        >>> sum_even_numbers([2, "four", 4.5, 6], strict=False)
        8
        >>> sum_even_numbers("246")
        Traceback (most recent call last):
            ...
        TypeError: numbers must be an iterable of numbers, not a str
    """
    if isinstance(numbers, (str, bytes, bytearray)):
        raise TypeError(
            f"numbers must be an iterable of numbers, not a "
            f"{type(numbers).__name__}"
        )

    try:
        pairs = enumerate(numbers)
    except TypeError:
        raise TypeError(
            f"numbers must be iterable, got {type(numbers).__name__}"
        ) from None

    total = 0
    for index, value in pairs:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            if strict:
                raise TypeError(
                    f"numbers[{index}] must be an int or float, "
                    f"got {type(value).__name__}: {value!r}"
                )
            continue

        if isinstance(value, float):
            if not math.isfinite(value) or not value.is_integer():
                if strict:
                    raise ValueError(
                        f"numbers[{index}] must be a whole number, got {value!r}"
                    )
                continue
            value = int(value)

        if value % 2 == 0:
            total += value

    return total


if __name__ == "__main__":
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Numbers: {sample}")
    print(f"Sum of even numbers: {sum_even_numbers(sample)}")

    messy = [2, "four", None, 4.5, 6.0]
    print(f"\nMessy input: {messy}")
    print(f"Skipping invalid values: {sum_even_numbers(messy, strict=False)}")
    try:
        sum_even_numbers(messy)
    except TypeError as error:
        print(f"Strict mode raises: {error}")
