#!/usr/bin/python3
"""Defines an int add func."""


def add_integer(a, b=98):
    """Return the int add of a & b.

    Float args are transformed to ints before the addition.

    Raises:
        TypeError: If  a or b is a non-int & non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
