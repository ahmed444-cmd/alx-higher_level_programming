#!/usr/bin/python3
"""
    def  class Student
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): f-name.
            last_name (str): l-name.
            age (int): age.
        Methods:
            __init__ - init the Student instance.
            to_json - dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary of Student.
        """
        return self.__dict__
