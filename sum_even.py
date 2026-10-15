def sum_even_numbers(numbers):
    """Return the sum of the even integers in `numbers`.

    Returns 0 for an empty list or a list with no even numbers.

    Raises:
        TypeError: if `numbers` is not a list or tuple, or if any element
            is not an integer. Booleans and floats (even whole-number ones
            like 2.0) are rejected.
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"Expected a list of integers, got {type(numbers).__name__}")

    for i, n in enumerate(numbers):
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError(
                f"Element at index {i} is not an integer: {n!r} ({type(n).__name__})"
            )

    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([1, 3, 5]) == 0
    assert sum_even_numbers([-4, -3, 0, 7, 10]) == 6
    assert sum_even_numbers((2, 4)) == 6

    for bad in ([1, 2.5], [2.0, 4], [1, "2"], [True, 2], [None], "246", 42, None):
        try:
            sum_even_numbers(bad)
        except TypeError:
            pass
        else:
            raise AssertionError(f"Expected TypeError for {bad!r}")

    print("All checks passed.")
