#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for i in range(10):
    for j in range(10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
            break

        if i < j:
            print("{}{}, ".format(i, j), end="")
            continue
