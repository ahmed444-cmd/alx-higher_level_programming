#!/usr/bin/python3

"""Definition of an object attrib lookup funct."""


def lookup(obj):
    """Returns a list of an object's attribs."""
    return (dir(obj))

0x0A-python-inheritance/1-my_list.py

#!/usr/bin/python3

"""Definition of an inherited lst clss MyList."""


class MyList(list):
    """Sorted printing for the built-in lit clss."""

    def print_sorted(self):
        """Prints a lst in ascending order."""
        print(sorted(self))
