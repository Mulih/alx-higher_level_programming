#!/usr/bin/python3

"""Defines a file-appending fnction."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (Str): The string to append to the file.
    Return:
        The number of characters appended.
    """
    with open(filename="", encoding="UTF8") as f:
        return f.write(text)
