#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces an element with a new one """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
