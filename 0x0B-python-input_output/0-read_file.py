#!/usr/bin/python3

"""function that reads a text file and prints it out"""


def read_file(filename=""):
    """reads UTF8 and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
