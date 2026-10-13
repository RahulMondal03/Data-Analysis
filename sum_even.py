def sum_even(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Raises ``TypeError`` if any element is not an integer. Booleans are
    rejected even though ``bool`` is a subclass of ``int``.

    >>> sum_even([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even([-4, -3, 0, 7])
    -4
    >>> sum_even([1, 3, 5])
    0
    >>> sum_even([])
    0
    >>> sum_even([2, 4.0])
    Traceback (most recent call last):
    ...
    TypeError: element at index 1 is not an integer: 4.0 (float)
    >>> sum_even([2, "4"])
    Traceback (most recent call last):
    ...
    TypeError: element at index 1 is not an integer: '4' (str)
    >>> sum_even([True, 2])
    Traceback (most recent call last):
    ...
    TypeError: element at index 0 is not an integer: True (bool)
    """
    for i, n in enumerate(numbers):
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError(
                f"element at index {i} is not an integer: {n!r} ({type(n).__name__})"
            )
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
