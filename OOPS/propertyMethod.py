'''
property decorator is used to
->type checking : whether it is int or float or string
->validation or updation with setter method
 '''
import math


class Ring(object):
    center = 0.0

    def __init__(self, radius=2.0, price=5.0, quantity=3):
        self.radius = radius
        self.price = price
        self.quantity = quantity

    @property
    def radius(self):   # the name has to be same with the variable defined
        # return self._radius
        return self.diameter/2.0
        # can return different name--here we use diameter

    @radius.setter  # here we are setting to check the type
    def radius(self, val):  # checking that the value for radius is int or float
        if not isinstance(val, (float, int)):
            raise TypeError("Expected float or int")
        # self._radius = float(val)
        self.diameter = 2*float(val)

    # multiple constructor
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2.0
        return cls(radius)

    def area(self):
        p = self.__perimeter()
        r = p/(2*math.pi)
        return math.pi*r**2

    def perimeter(self):
        return 2*math.pi*self.radius

    # make a local copy
    __perimeter = perimeter
