#!/usr/bin/python3

"""appends a string at the end of a text"""


def append_write(filename="", text=""):
    """appends a strings to the end of UTF-8 text.

    Args:
        filename (str): the name of the file to append to.
        text (str): The string to append to the file
    Returns:
        The number of the characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
