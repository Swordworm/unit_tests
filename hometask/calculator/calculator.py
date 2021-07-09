""" Home task calculator module """
from math import sqrt
from typing import Any


class Calculator:
    """ Calculator implementation """
    def add(self, x: int, y: int) -> int:
        """ Add to attributes to each other """
        self.is_number(x)
        self.is_number(y)
        return x + y

    def subtract(self, x: int, y: int) -> int:
        """ Subtract one attribute from another """
        self.is_number(x)
        self.is_number(y)
        return x - y

    def divide(self, x: int, y: int) -> float:
        """ Divide x attribute on y """
        self.is_number(x)
        self.is_number(y)
        return x / y

    def multiply(self, x: int, y: int) -> int:
        """ Multiply x attribute on y """
        self.is_number(x)
        self.is_number(y)
        return x * y

    def mod(self, x: int, y: int) -> int:
        """ Take mod of one attribute from another """
        self.is_number(x)
        self.is_number(y)
        return x % y

    def power(self, x: int, y: int) -> int:
        """ Raise attributes x to a power y """
        self.is_number(x)
        self.is_number(y)
        return x ** y

    def root(self, x: int) -> float:
        """ Take a root from attributes """
        self.is_number(x)
        return sqrt(x)

    def is_number(self, value):
        """ Raises TypeError if parameter is not an instance of int """
        if not isinstance(value, int):
            raise TypeError
