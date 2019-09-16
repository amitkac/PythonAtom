#  here we create a wrapper with and without arguments
#  rather than repetitive code--with one with argument and other
# without argument --we will use partial

from functools import wraps, partial

# wrapper with and without arguments


def PrintName(prefix="", *, func=None):
    # def
    if func is None:
        return partial(PrintName, prefix=prefix)

    #  wrap is used to exchange metadata between functions
    @wraps(func)
    def pn(*args, **kwargs):
        print(prefix + func.__name__)
        return func(*args, **kwargs)
    return pn
