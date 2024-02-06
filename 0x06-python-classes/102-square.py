#!/usr/bin/python3

class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size
        """
        self.size = size

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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal in area
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal in area
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if one square is smaller than the other in area
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if one square is smaller or equal to the other in area
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if one square is greater than the other in area
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if one square is greater or equal to the other in area
        """
        return self.area() >= other.area()
