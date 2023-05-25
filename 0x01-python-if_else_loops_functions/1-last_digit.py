#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = (number * -1) % 10
    digit = -digit
    print("Last digit of {} is {} and is".format(number, digit), end="")
    if digit < 6 and not 0:
        print("less than 6 and not 0")
else:
    last_digit = number % 10
    if last_digit > 5:
        print("Last digit of {} is {} and is ".format(number, last_digit), end="")
        print("greater than 5")
    elif last_digit  == 0:
        print("Last digit of {} is {} and is 0".format(number, last_digit))
    elif last_digit < 6 and not 0:
        print("Last digit of {} is {} and is".format(number, last_digit), end="")
        print("less than 6 and not 0")
