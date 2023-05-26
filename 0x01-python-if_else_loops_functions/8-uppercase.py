#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = ord(char) - 32
            print("{}".format(chr(char)), end="")
        else:
            print("{}".format(char), end="")
    print()
