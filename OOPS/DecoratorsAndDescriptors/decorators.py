
# function within a function
# can use arguments and keyword arguments (*args,**kwargs)
# decorator is a function that creates a wrapper around another function
# wrappers add some additional functionality to existing code

from functools import wraps


def printName(func):
    # func is the function to be wrapped
    #  this function takes a function as an input and returns a function back

    @wraps(func)
    # wraps is used to exchange metadata between functions
    def pn(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return pn


@printName('**')
def add2Num(x, y):
    return x+y


print(add2Num(2, 4))


def addOne(myfunc):
    # def addOneIn(x):
    def addOneIn(*args, **kwargs):
        print("adding one")
        return myfunc(*args, **kwargs)+1
    return addOneIn


@addOne
def subThree(x):
    return x-3


print(subThree(5))
# result = addOne(subThree)  # this is a function as return value is a function
# print(result(5))   # the return value is the addOneIn function
