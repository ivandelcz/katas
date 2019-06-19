#!/usr/bin/env python


def multiple_of_three(number):
    return number % 3 == 0


def divisible_number(number):
    if multiple_of_three(number):
        return 'fizz'
    elif number == 5 or number == 10 or number == 20:
        return 'buzz'
    else:
        return str(number)
