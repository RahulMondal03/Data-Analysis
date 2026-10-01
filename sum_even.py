def sum_even(numbers):
    """Return the sum of the even numbers in ``numbers``.

    Non-integer values (e.g. 2.5) are ignored; floats with an integral
    value (e.g. 4.0) are treated as even. Booleans are skipped.
    """
    return sum(
        n for n in numbers
        if not isinstance(n, bool)
        and isinstance(n, (int, float))
        and n % 2 == 0
    )


if __name__ == "__main__":
    assert sum_even([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even([]) == 0
    assert sum_even([1, 3, 5]) == 0
    assert sum_even([-2, -3, 4]) == 2
    assert sum_even([2.5, 4.0, 7]) == 4.0
    print("All tests passed.")
