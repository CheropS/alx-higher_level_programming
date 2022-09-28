#!/usr/bin/python3

"""writes a string to txt and returns character"""


def write_file(filename="", text=""):
    """write a string to a UTF-8 textfile

    Args:
        filename (str): the name of the file
        text (str): The text to write to the file
    Returns:
        The no of characters to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
