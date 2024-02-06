#!/usr/bin/python3
"""
Defines a Square class
"""


class Square:
    """
    Represents a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position
        """
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or type(value[1]) is not int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
