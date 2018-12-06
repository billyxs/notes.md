# Circle exercise
# https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/
# https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/solution/

from math import pi


class Circle:
    """
    My solution - Circle class
    Doing all the circle stuff

    Didn't need the posted solution. This covered all the needs.
    """

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return pi * self.radius**2

    @radius.setter
    def radius(self, radius):
        if radius < 1:
            raise ValueError("Radius cannot be negative")
        self.__radius = radius

    @diameter.setter
    def diameter(self, diameter=2):
        self.radius = diameter/2

    @area.setter
    def area(self, area):
        raise AttributeError("cannot set area")


