#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return None
    max_int = reduce(lambda a, b: a if a > b else b, my_list)
    return max_int
