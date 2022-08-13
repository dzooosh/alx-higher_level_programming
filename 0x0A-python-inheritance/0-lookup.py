#!/usr/bin/python3
""" List all attributes and methods of an object class"""

def lookup(obj):
    """Returns a list of available fields and methods"""
    return (dir(obj))
