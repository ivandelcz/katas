#!/usr/bin/env python


def multiple_of_three_and_five(number):
    return number % 3 == 0 and number % 5 == 0


def multiple_of_three(number):
    return number % 3 == 0


def multiple_of_five(number):
    return number % 5 == 0


def divisible_number(number):
    if multiple_of_three_and_five(number):
        return 'fizzbuzz'
    elif multiple_of_three(number):
        return 'fizz'
    elif multiple_of_five(number):
        return 'buzz'
    else:
        return str(number)
