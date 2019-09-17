from arabic_to_roman import to_roman


def test_convert_one():
    result = to_roman(1)

    assert result == "I"


def test_convert_two():
    result = to_roman(2)

    assert result == "II"


def test_convert_three():
    result = to_roman(3)

    assert result == "III"


# def test_convert_four():
#     result = to_roman(4)

#     assert result == "IV"


def test_convert_five():
    result = to_roman(5)

    assert result == "V"


def test_convert_six():
    result = to_roman(6)

    assert result == "VI"


def test_convert_ten():
    result = to_roman(10)

    assert result == "X"


def test_convert_eighteen():
    result = to_roman(18)

    assert result == "XVIII"


def test_convert_four():
    result = to_roman(4)

    assert result == "IV"


def test_convert_fourty_four():
    result = to_roman(44)

    assert result == "LXIV"
