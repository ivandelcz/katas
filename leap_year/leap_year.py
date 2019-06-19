#!/usr/bin/env python
import sys


def is_divisible_by_number(year, number):
    return year % number == 0


def is_leap_year(year):
    if is_divisible_by_number(year, 4):
        if not is_divisible_by_number(year, 100):
            return True
        elif is_divisible_by_number(year, 400):
            return True

    return False


if __name__ == "__main__":
    print(is_leap_year(int(sys.argv[1])))
