import math
import time


class Ring(object):

    # class variables--available to all class methods
    date = time.strftime("%Y-%m-%d", time.gmtime())
    center = 001.020

    def __init__(self, date=date, metal='copper', radius=5.0, price=5.0,
                 quantity=5):
        """init is not a constructor, but an initializer
        which initializes the instance variables"""
        self.date = date
        self.metal = metal
        self.radius = radius
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price*self.quantity

    def area(self):
        return math.pi*self.radius**2
