#!/usr/bin/python3

"""defines a function that writes an onject to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
