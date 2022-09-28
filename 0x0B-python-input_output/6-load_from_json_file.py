#!/usr/bin/python3

"""function that loads an object from json file"""
import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename) as f:
        return json.load(f)
