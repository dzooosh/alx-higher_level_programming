#!/usr/bin/python3

# function that returns a new dict with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dict = dict(map(lambda x: x[1] * 2), a_dictionary.items())
    return new_dict
