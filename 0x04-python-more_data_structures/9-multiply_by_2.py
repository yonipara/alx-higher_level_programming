#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {key: a_dictionary[key] * 2 for key in a_dictionary}
    return new_dict
