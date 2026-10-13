"""A division helper that fails clearly on a zero divisor."""

from typing import Union

Number = Union[int, float]


def divide(a: Number, b: Number) -> float:
    """Return ``a / b``.

    A plain ``a / b`` with ``b == 0`` raises ``ZeroDivisionError`` from deep
    inside whatever calculation called it. This helper checks the divisor
    first and raises a ``ValueError`` that names the bad input instead.

    Args:
        a: The dividend.
        b: The divisor; must not be zero.

    Returns:
        The quotient ``a / b``.

    Raises:
        ValueError: If ``b`` is zero (``0``, ``0.0`` or ``-0.0``).

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(-9, 3)
        -3.0
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ValueError: cannot divide 10 by zero
    """
    if b == 0:
        raise ValueError(f"cannot divide {a!r} by zero")
    return a / b


if __name__ == "__main__":
    print(f"divide(10, 2) = {divide(10, 2)}")
    try:
        divide(10, 0)
    except ValueError as error:
        print(f"divide(10, 0) raises: {error}")
