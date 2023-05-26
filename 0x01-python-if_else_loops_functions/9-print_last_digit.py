#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """Print the last digit of a number"""
    if number < 0:
        digit = (number * -1) % 10
        print("{}".format(digit), end="")
        return digit
    else:
        digit = number % 10
        print("{}".format(digit), end="")
        return digit
