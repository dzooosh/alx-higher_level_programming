#!/usr/bin/python3
# isupper: A function that prints strings in upper character
# str: string to change
# Returns: capitalized string

def uppercase(str):
    upcase = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 123):
           letter = chr(ord(i) - 32)
        upcase += letter
    return upcase
