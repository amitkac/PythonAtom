# write a debug decorator that wraps the functions
#  and prints the function name

# here we are using decorator with an argument **
#  to use decorator with an argument, we wrap it in another function as below
#  here PrintName is wrapper with argument

from functools import wraps


def printName(prefix=""):
    def addPrefix(func):
        # func is the function to be wrapped
        msg = prefix+func.__name__
        @wraps(func)
        def pn(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return pn
    return addPrefix
