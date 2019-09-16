# x = 9


class Add(object):
    # class variable
    x = 20

    def __init__(self, x):
        self.x = x

    def addMethod(self, y):
        return self.x+y

        # class method--as convention we need to use cls

    @classmethod
    def addClass(self, y):
        return self.x+y

    # static method takes variable defined in main function
    # static doesn't take anything from self

    @staticmethod
    def addStatic(x, y):
        return x+y
