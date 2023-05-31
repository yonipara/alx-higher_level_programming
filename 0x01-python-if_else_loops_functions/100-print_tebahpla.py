#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
x = 122
for i in range(1, 27):
    if x % 2 == 0:
        print("{}".format(chr(x)), end="")
    else x % 2 != 0:
        y = x - 32
        print("{}".format(chr(y)), end="")
    x -= 1
