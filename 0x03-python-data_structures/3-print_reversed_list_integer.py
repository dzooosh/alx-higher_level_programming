#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ prints all integer of a list in reversed order
    i = len(my_list) - 1
    while (i >= 0):
       print("{:d}".format(my_list[i]))
       i -= 1
"""
    for i in range((len(my_list) - 1), -1, -1):
        print("{:d}".format(my_list[i]))
