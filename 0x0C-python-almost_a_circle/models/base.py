#!/usr/bin/python3
"""Module for base class here."""
from json import dumps, loads
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file."""
        if list_objs:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """JKVAJKAKC."""
        if json_string is None or not json_string:
            return "[]"
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """HHshDKJKJDAJ."""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1,10)
        elif cls is Square:
            new = Square(7)
        else:
            new = None
        new.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**dic) for dic in cls.from_json_string(f.read())]