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
