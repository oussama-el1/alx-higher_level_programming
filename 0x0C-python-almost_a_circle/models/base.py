#!/usr/bin/python3
"""Module for base class here."""

class Base:
    """the strucure of the class."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor."""
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects