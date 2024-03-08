#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if (not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(num, int) for num in value) or
        not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints a square of #s of a given size"""
        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for x in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")

            for j in range(self.__size):
                print("#", end="")
            print()
