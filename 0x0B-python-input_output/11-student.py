#!/usr/bin/python3

"""defines a class student"""


class Student:
    """represents a class student"""

    def __init__(self, first_name, last_name, age):
        """initializes a new student

        Args:
            first_name (str): The first name of the student
            last_name (str): last name
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dict rep of the student

        If attrs is a list of strings, rep only those attributes
        included in the list

        Args:
            attrs(list): (optional) the attributes to represent
            """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attributes of student

        Args:
            json (dict): the key/value pairs to replace attributes with
        """
        for k, v in json.items():
            setattr(self, k, v)
