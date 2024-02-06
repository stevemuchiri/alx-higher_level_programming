#!/usr/bin/python3

import math

class MagicClass:
    """
    Represents a magic class that calculates the area and circumference of a circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """
        Getter method for the radius.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Setter method for the radius.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('radius must be a number')
        self.__radius = value

    def area(self):
        """
        Calculates the area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.
        """
        return 2 * math.pi * self.__radius
