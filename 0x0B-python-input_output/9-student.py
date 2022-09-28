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

    def to_json(self):
        """get a dict rep of the student"""
        return self.__dict__
