def sum(a: int, b: int) -> int:
    """Return the sum of two integers"""

    return a + b


def sum_all(*args: int) -> int:
    """Sum all passed arguments"""

    total = 0

    for arg in args:
        total += arg

    return total
