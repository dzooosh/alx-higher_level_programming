#!/usr/bin/python3

# function that replaces all occurences of an element by another in a new list
def search_replace(my_list, search, replace):
    # create a new list to return
    new_list = []
    # loop through the list to identify the search then replace
    for i in my_list:
        # check if search value is present for the replace to take place
        if search == i:
            i == replace
            new_list.append(i)
        else:
            new_list.append(i)
    return new_list
