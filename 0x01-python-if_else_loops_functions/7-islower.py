#!/usr/bin/python3
# 7-islower.py


def islower(c):
    c = ord(c)
    if c < 97 or c > 122:
        return False
    else:
        return True
