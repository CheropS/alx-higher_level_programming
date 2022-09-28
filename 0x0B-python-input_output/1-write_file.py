#!/usr/bin/python3

"""writes a string to txt and returns character"""


def write_file(filename="", text=""):
    """return the no of line in a text file"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
