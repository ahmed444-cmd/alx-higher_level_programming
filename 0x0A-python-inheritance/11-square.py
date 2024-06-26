#!/usr/bin/python3
"""
    definition of a class Square from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square from Rectangle
        Attributes:
            size (int): size of square
        Methods:
            __init__ - def the square
    """
    def __init__(self, size):
        """
            def Square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Returns area of square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__,
                                    self.__size, self.__size))
