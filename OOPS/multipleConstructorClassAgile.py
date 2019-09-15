import math
import time


class Ring(object):
    # class variables

    date = time.strftime("%Y-%m-%d", time.gmtime())
    center = 0.0

    # initializing
    def __init__(self, radius=10, price=4.2, date=date, metal="defMetal",
                 quantity=10):
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity

# now we have a team that works with diameter rather than  radius
# for agility , we will use class method to create a multiple constructor
# so that they can work with diameter

    @classmethod
    def from_diameter(cls, diameter, price):
        radius = diameter/2  # changing radius to diameter
        price = price*0.5
        # ew = cls(radius)  # , price)
        return cls(radius, price)  # return radius for diameter

    def cost(self):
        return self.price*self.quantity

    def area(self):
        return math.pi*self.radius**2

    def areaFromPerim(self):
        # p = self.perimeter()
        p = self.__perimeter()  # we created a local copy so that we don't use
        # the updated parameter that was overridden by Box child class
        r = p/(2*math.pi)
        return math.pi*r**2

    def perimeter(self):
        return 2.0*math.pi*self.radius

    # _perimeter = perimeter  # here is where we create a local class copy
    __perimeter = perimeter
    # we can also use _ _ to make it store local copy : _ _ can have same name
    # in
    # both classes


class Box(Ring):

    """override the perimeter method"""

    def perimeter(self):
        # using twice the perimeter
        newPerimeter = Ring.perimeter(self)*2.0
        return newPerimeter

    # we can also save the updated perimeter here with same  name
    # while using _ _
    __perimeter = perimeter
