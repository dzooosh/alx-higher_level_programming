#!/usr/bin/python3
# isupper: A function that prints strings in upper character
# str: string to change
# Returns: capitalized string

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            leta = chr(ord(i) - 32)
        print("{}".format(leta), end="")
    print("")
