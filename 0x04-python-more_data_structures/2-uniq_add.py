#!/usr/bin/python3

# function that adds all unique integers in a list \
#        ( only once for each integer)
# convert list to a set to remove duplicates elements
# add up each elements
# return the total

def uniq_add(my_list=[]):
    total = 0
    new_set = set(my_list)
    for i in new_set:
        total += i
    return total
