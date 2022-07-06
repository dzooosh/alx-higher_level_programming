#!/usr/bin/python3

# function that returns a set of all elements present in only one set
# join the two sets using union method
# return the resulting set

def only_diff_elements(set_1, set_2):
    new_set = set_1.union(set_2)
    return new_set
