#!/usr/bin/python3
# isupper: A function that prints strings in upper character
# str: string to change
# Returns: capitalized string


def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
