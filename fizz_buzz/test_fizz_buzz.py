from fizz_buzz import divisible_number


def test_for_number_1_return_as_string():
    result = divisible_number(1)

    assert result == '1'