from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    def __str__(self):
        return f'Area: {self.calculate_area()}, Perimerter: {self.calculate_perimeter()}'

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return self.__radius ** 2 * pi

    def calculate_perimeter(self):
        return 2 * self.__radius * pi


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


sh = [
    # Shape(),
    Circle(5),
    Rectangle(2, 3)
]


def print_shape(s: Shape):
    print(s)


[print_shape(s) for s in sh]
