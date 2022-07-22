#!/usr/bin/python3
""" Adds two 2 integers """


def add_integer(a, b=98):
    """ adds two integers together
    checks if they have data types: int or float
    Args:
        a - value number 1
        b - value number 2 with a default of 98. This means
            if only one value is given, it is automatically added
            with 98

    Returns:
        TypeError raised if a or b is not int or fload
        An Integer: the sum total of a and b
    """
    try:
        total = 0
        a = int(a)
        b = int(b)
        total = a + b
        return total
    except TypeError as te:
        print("a must be an integer or b must be an integer")
