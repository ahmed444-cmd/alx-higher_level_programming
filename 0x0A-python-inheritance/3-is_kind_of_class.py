#!/usr/bin/python3

"""Definition of a class & inherit class-checking funct."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherit instance of a clss.
    Args:
        obj (any): The object.
        a_class (type): The class to match.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
