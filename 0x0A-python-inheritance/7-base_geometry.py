#!/usr/bin/python3

"""Definition of a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an int.
        Args:
            name (str): The name of the param.
            value (int): The parameter.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is negative.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
