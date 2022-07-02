#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    lst = my_list.copy()
    if idx < 0:
        return lst
    if idx >= len(my_list):
        return lst
    lst[idx] = element
    return lst
