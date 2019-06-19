from leap_year import is_divisible_by_number, is_leap_year


def test_1996_is_divisible_by_4():
    assert is_divisible_by_number(1996, 4)


def test_1996_is_not_divisible_by_100():
    assert not is_divisible_by_number(1996, 100)


def test_1996_is_divisible_by_400():
    assert not is_divisible_by_number(1996, 400)


def test_1996_is_leap_year():
    assert is_leap_year(1996)


def test_2000_is_leap_year():
    assert is_leap_year(2000)
