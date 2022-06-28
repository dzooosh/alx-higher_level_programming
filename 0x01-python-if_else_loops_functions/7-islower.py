#!/usr/bin/python3
# islower: A function that checks for lower character
# c: parameter to check
# Returns: True or False on confirmation

def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False
