# we will call the debugger decorator that prints the function name

# from debugEx import printName
from debugEx2 import PrintName


def main():
    @PrintName(prefix="+-")
    # very important to give the argument else the wrapper will not work
    def add2Num(x, y):
        ''' adds two number'''
        return x+y

    @PrintName
    # same wrapper but without argument-- all thanks to partial
    def mul2Num(x, y):
        ''' multiply 2 num'''
        return x*y

    print(add2Num(2, 4))
    print(mul2Num(2, 4))


if __name__ == '__main__':
    main()
