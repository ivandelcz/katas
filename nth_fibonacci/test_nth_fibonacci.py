from nth_fibonacci import nth_fibonacci


def test_first_fibonacci_number_is_0():
    result = nth_fibonacci(0)

    assert result == 0


def test_second_fibonacci_number_is_1():
    result = nth_fibonacci(1)

    assert result == 1
