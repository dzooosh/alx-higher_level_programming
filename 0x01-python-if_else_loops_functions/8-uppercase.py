#!/usr/bin/python3
# isupper: A function that checks for upper character
# c: parameter to check
# Returns: True or False on confirmation

def isupper(c):
    if ord(c) in range(65, 91):
        return True
    else:
        return False
