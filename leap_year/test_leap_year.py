from leap_year import is_divisible_by_4, is_divisible_by_100


def test_1996_is_divisible_by_four():
    assert is_divisible_by_4(1996)


def test_1996_is_not_divisible_by_100():
    assert not is_divisible_by_100(1996)
