#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    j = -1
    for i in my_list:
        print("{:d}".format(my_list[j]))
        j -= 1
