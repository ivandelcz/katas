from fizz_buzz import divisible_number


def test_for_number_1_return_as_string():
    result = divisible_number(1)

    assert result == '1'


def test_for_number_2_return_as_string():
    result = divisible_number(2)

    assert result == '2'


def test_for_number_4_return_as_string():
    result = divisible_number(4)

    assert result == '4'


def test_for_number_3_return_fizz():
    result = divisible_number(3)

    assert result == 'fizz'


def test_for_number_6_return_fizz():
    result = divisible_number(6)

    assert result == 'fizz'


def test_for_number_9_return_fizz():
    result = divisible_number(9)

    assert result == 'fizz'


def test_for_number_5_return_buzz():
    result = divisible_number(5)

    assert result == 'buzz'

