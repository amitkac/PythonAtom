from propertyMethod import Ring


def main():
    d = Ring.from_diameter(diameter=20)
    print("radius:{0}, perimeter:{1:0.2f},area:{2:0.2f}"
          .format(d.radius, d.perimeter(), d.area()))

    d.radius = 2.0
    print("radius:{0}, perimeter:{1:0.2f},area:{2:0.2f}"
          .format(d.radius, d.perimeter(), d.area()))

    # type checking with property setter
    # d.radius = "henlo"
    print(d.__dict__)


if __name__ == "__main__":
    main()
