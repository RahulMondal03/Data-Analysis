def sum_even_numbers(numbers):
    """Return the sum of the even numbers in `numbers`.

    Non-integral values (e.g. 2.5) are never even and are skipped.
    Returns 0 for an empty list or a list with no even numbers.
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([]) == 0
    assert sum_even_numbers([1, 3, 5]) == 0
    assert sum_even_numbers([-4, -3, 0, 7, 10]) == 6
    assert sum_even_numbers([2.0, 2.5, 4]) == 6
    print("All checks passed.")
