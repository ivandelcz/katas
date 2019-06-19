from nth_fibonacci import nth_fibonacci


def test_first_fibonacci_number_is_0():
    result = nth_fibonacci(0)

    assert result == 0


def test_second_fibonacci_number_is_1():
    result = nth_fibonacci(1)

    assert result == 1


def test_third_fibonacci_number_is_1():
    result = nth_fibonacci(2)

    assert result == 1


def test_fouth_fibonacci_number_is_2():
    result = nth_fibonacci(3)

    assert result == 2


def test_fifth_fibonacci_number_is_3():
    result = nth_fibonacci(4)

    assert result == 3
