#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    new_list = my_list[:]
    if idx >= 0 and idx < len(new_list):
        new_list[idx] = element
    return (new_list)
