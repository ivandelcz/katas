#!/usr/bin/env python
import sys


def nth_fibonacci(position):
    if position == 0 or position == 1:
        return position
    else:
        return nth_fibonacci(position - 1) + nth_fibonacci(position - 2)


if __name__ == "__main__":
    print(nth_fibonacci(int(sys.argv[1])))
