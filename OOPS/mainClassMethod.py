import classMethod as cm


def main():
    # x = 20
    m = cm.Add(x=4)  # initializing the class with x
    print("normal method:", m.addMethod(y=9))

    print("class method:", m.addClass(y=5))

    print("static method:", m.addStatic(x=7, y=3))


if __name__ == "__main__":
    main()
