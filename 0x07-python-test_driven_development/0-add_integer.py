#!/usr/bin/python3
""" Returns Addition of two integers"""

def add_integer(a, b=98):
    """
    add_integer: adds 2 integers
    
    a: 1st integer/float
    b: 2nd integer/float (with default value of 98)
    Raise TypeError if a or b is not an integer

    return: the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = 0
    result = int(a) + int(b)
    return result
