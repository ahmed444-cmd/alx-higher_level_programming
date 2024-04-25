#!/usr/bin/python3
"""
Definition of a base model class.
"""
import json
import csv
import turtle

class Base:
    """
    Represention of the base model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
