#!/usr/bin/python3
""" module and base of all other classes """

import json


class Base():
    """ BaseClass of all other classes """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiator """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON of a dictionary """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file """
        temp = []
        if list_objs is None or len(list_objs) is 0:
            pass
        else:
            for i in list_objs:
                temp.append(cls.to_dictionary(i))
        x = cls.to_json_string(temp)
        with open("{}.json".format(cls.__name__),
                  mode='w', encoding='utf-8') as f:
            f.write(x)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of a json string """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes of the dict """
        if cls.__name__ is "Rectangle":
            temp = cls(6, 9)
        if cls.__name__ is "Square":
            temp = cls(6)
        temp.update(**dictionary)

        return temp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        temp = []
        with open("{}.json".format(cls.__name__), "r", encoding='utf-8') as f:
            temp = cls.from_json_string(f.read())
        for i in range(len(temp)):
            temp[i] = cls.create(**temp[i])
        return temp