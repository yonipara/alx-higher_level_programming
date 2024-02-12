#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    for j in my_list:
         return list(map(lambda x: True if x % 2 == 0 else False, my_list)) 
