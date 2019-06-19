#!/usr/bin/env python


def nth_fibonacci(position):
    if position == 0 or position == 1:
        return position
    else:
        return nth_fibonacci(position - 1) + nth_fibonacci(position - 2)
