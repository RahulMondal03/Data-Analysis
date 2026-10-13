def sum_even(numbers):
    """Return the sum of the even numbers in ``numbers``.

    >>> sum_even([1, 2, 3, 4, 5, 6])
    12
    >>> sum_even([-4, -3, 0, 7])
    -4
    >>> sum_even([1, 3, 5])
    0
    >>> sum_even([])
    0
    """
    return sum(n for n in numbers if n % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
