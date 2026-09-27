from math_utils import sum_range


def test_sum_range_zero():
    assert sum_range(0) == 0


def test_sum_range_four():
    assert sum_range(4) == 10


def test_sum_range_ten():
    assert sum_range(10) == 55
