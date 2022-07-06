#!/usr/bin/python3

# function that returns a new dict with all values multiplied by 2
def multiply_by_2(a_dictionary):
    a_dict = a_dictionary.copy()

    for i in a_dict.keys():
        a_dict[i] *= 2

    return (a_dict)
