#!/usr/bin/python3
'''Definition class Rectangle.'''
from models.base import Base


class Rectangle(Base):
    '''Represents a Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes a new Rectangle.

        Args:
           width (int): The width of rectangle.
           height (int): The height of rectangle.
           x (int): The x coordinate of rectangle.
           y (int): The y coordinate of rectangle.
           id (int): The identity of rectangle.
        Raises:
           TypeError: If the input is not an integer.
           ValueError: If width/height is <= 0.
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Setter/Getter the width of rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Setter/Getter the height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Setter/Getter the x coordinates of rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Setter/Getter the y coordinates of rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculates the area of the rectangle.'''
        return self.width * self.height

    def display(self):
        '''Displays the rectangle using #.'''
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        '''Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>. format'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''Update an argument to each attribute.

        Args:
           *args (ints): new attribute value.
               - 1st argument represent id attr.
               - 2nd argument represent width attr.
               - 3rd argument represent height attr.
               - 4th argument represent x attr.
               - 5th argument represent y attr.
            **kwargs (dict): A double points to a dictionary.
        '''
        if args and len(args) != 0:
            argument = 0
            for arg in args:
                if argument == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif argument == 1:
                    self.width = arg
                elif argument == 2:
                    self.height = arg
                elif argument == 3:
                    self.x = arg
                elif argument == 4:
                    self.y = arg
                argument += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Returns the dictionary of a Rectangle.'''
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
