def sum_even(numbers):
    """Return the sum of the even integers in ``numbers``.

    Raises:
        TypeError: if ``numbers`` is not a list or tuple, or if any element
            is not an integer (floats, strings, None and booleans are
            rejected).
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(
            f"numbers must be a list or tuple, got {type(numbers).__name__}"
        )

    for index, n in enumerate(numbers):
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError(
                f"element at index {index} must be an integer, "
                f"got {type(n).__name__}: {n!r}"
            )

    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    assert sum_even([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even([]) == 0
    assert sum_even([1, 3, 5]) == 0
    assert sum_even([-2, -3, 4]) == 2
    assert sum_even((2, 4)) == 6

    for bad in ([1, 2.5], [2, "4"], [None], [True, 2], "1234", 42, None):
        try:
            sum_even(bad)
        except TypeError:
            pass
        else:
            raise AssertionError(f"expected TypeError for {bad!r}")

    print("All tests passed.")
