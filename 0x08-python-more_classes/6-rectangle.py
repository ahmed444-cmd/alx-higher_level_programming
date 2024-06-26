#!/usr/bin/python3
"""Definition of a Rectangle class.
"""


class Rectangle:
    """Rectangle class with width and height.
    Attributes:
        number_of_instances: number of Rectangle instances,
        increments with every instantitation,
        decrements with every deletion
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance,with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    def __repr__(self):
        """Return a string representation of a Rectangle instance
        that is able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """width of a Rectangle instance
        Args:
            value: value of the width, must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance
        Returns:
            Area of the the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of a Rectangle instance
        Returns:
            Perimeter of rectangle, by(height + width) given
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
