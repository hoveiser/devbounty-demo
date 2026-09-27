"""Small math helpers."""


def sum_range(n: int) -> int:
    """Return the sum of all integers from 0 to n inclusive."""
    total = 0
    for i in range(0, n + 1):
        total += i
    return total
