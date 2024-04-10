#!/usr/bin/python3
"""Definition of an int addition function."""

def add_integer(a, b=98):
    """Returns the int addition of a and b.
	Floats are casted to ints before addition is performed.
	TypeError: If a or b is a non-int and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
