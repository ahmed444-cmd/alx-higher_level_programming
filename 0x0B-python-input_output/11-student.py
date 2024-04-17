#!/usr/bin/python3
"""
    def class Student
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
            to_json - dictionary of Student instance.
            reload_from_json - replaces a;; attributes of Stud instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            dictionary of Student.
            Args:
                attr (list): attribute names.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
            replaces all attributes of the Stud.
            Args:
                json (dictionary): reload data.
        """
        for key, value in json.items():
            self.__setattr__(key, value)
