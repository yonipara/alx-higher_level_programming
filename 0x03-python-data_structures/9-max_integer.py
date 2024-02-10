#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return None
    max_int = my_list[0]
    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int
