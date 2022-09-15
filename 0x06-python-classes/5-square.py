#!/usr/bin/python3

"""defines a class square"""


class Square:
    """reps a square"""

    def __init__(self, size):
        """initialize a new square.

        Args:
            size (int): The size of the new square."""
        self.size = size

    @property
    def size(self):
        """get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with the # character"""
        for a in range(0, self.__size):
            [print("#", end="") for b in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
