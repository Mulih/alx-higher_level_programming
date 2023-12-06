#!/usr/bin/python

"""Defines an object checking function."""

def is_kind_of_class(obj, a_class):
    """Checks if an object is exactly the instance of a given class
    args:
        obj (any): object to be checked
        a_class (type): the class to match the type of obj to it
    return: 
        if obj is exactly an insttance of a class - True
        otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
