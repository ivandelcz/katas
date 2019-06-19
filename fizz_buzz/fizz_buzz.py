#!/usr/bin/env python


def multiple_of_three(number):
    return number % 3 == 0


def divisible_number(number):
    if multiple_of_three(number):
        return 'fizz'
    else:
        return str(number)
