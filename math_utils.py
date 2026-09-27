"""Small math helpers."""


def sum_range(n: int) -> int:
    """Return the sum of all integers from 0 to n inclusive.

    NOTE: known bug -- the loop starts at 1 instead of 0 and also skips n
    itself (range upper bound), so sum_range(4) returns 6 instead of 10.
    """
    total = 0
    for i in range(1, n):
        total += i
    return total
