"""Utility for summing the even numbers in a sequence."""

from typing import Iterable

_NUMERIC_TYPES = (int, float)


def sum_even_numbers(numbers: Iterable[float]) -> int:
    """Return the sum of the even numbers in ``numbers``.

    Every element is validated before it is used, so a bad value produces a
    clear error naming its position instead of a confusing failure deeper in
    the loop. Floats are accepted only when they hold a whole number
    (``4.0`` is even, ``4.5`` has no parity at all).

    Args:
        numbers: An iterable of whole numbers (``int``, or ``float`` with no
            fractional part).

    Returns:
        The sum of every even value, as an ``int``; 0 when none are even.

    Raises:
        TypeError: If ``numbers`` is not an iterable of numbers, or is a
            string (iterating one yields characters, which is never intended).
        ValueError: If an element is a number but not a whole one, such as
            ``4.5``, ``float("nan")`` or ``float("inf")``.
    """
    if isinstance(numbers, (str, bytes, bytearray)):
        raise TypeError(
            f"expected an iterable of numbers, got {type(numbers).__name__}: {numbers!r}"
        )
    try:
        iterator = iter(numbers)
    except TypeError:
        raise TypeError(
            f"expected an iterable of numbers, got {type(numbers).__name__}: {numbers!r}"
        ) from None

    total = 0
    for index, number in enumerate(iterator):
        # bool is a subclass of int, but True/False are not measurements.
        if isinstance(number, bool) or not isinstance(number, _NUMERIC_TYPES):
            raise TypeError(
                f"element {index} is not a number: {number!r} "
                f"(type {type(number).__name__})"
            )
        if isinstance(number, float):
            if not number.is_integer():
                raise ValueError(
                    f"element {index} is not a whole number, so it has no parity: {number!r}"
                )
            number = int(number)
        if number % 2 == 0:
            total += number
    return total


if __name__ == "__main__":
    print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12
    print(sum_even_numbers([-4, -3, 0, 7]))      # -4
    print(sum_even_numbers([1, 3, 5]))           # 0
    print(sum_even_numbers([]))                  # 0
    print(sum_even_numbers([2.0, 3.0, 8]))       # 10

    for bad in ([1, "a"], [1, None], [1, 4.5], "246", 42, [1, True]):
        try:
            sum_even_numbers(bad)
        except (TypeError, ValueError) as error:
            print(f"{type(error).__name__}: {error}")
