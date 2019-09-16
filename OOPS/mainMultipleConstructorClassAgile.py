import multipleConstructorClassAgile as mc
import math


def main():
    # -----------initial example --1
    # print("Center of ring is", mc.Ring.center)  # default class variable
    #
    # r = mc.Ring(price=8.0)
    # print("radius:{0},cost:{1},area={2:0.2f},perimeter={3:0.2f}"
    #       .format(r.radius, r.cost(), r.area(), r.perimeter()))
    #
    # x = mc.Ring(price=18.0, radius=2.0)
    # print("radius:{0},cost:{1},area={2:0.2f},perimeter={3:0.2f}"
    #       .format(x.radius, x.cost(), x.area(), x.perimeter()))
    #
    # # using new constructor diameter
    # print()
    # d = mc.Ring.from_diameter(diameter=24, price=100)
    # # position of parameter matters a lot---in calling the function
    # print(d.radius)
    # print("radius: {0}, cost: {1}, area={2: 0.2f},perimeter={3: 0.2f}"
    #       .format(d.radius, d.cost(), d.area(), d.perimeter()))
    #
    # x = mc.Ring()
    # print("radius:{0},cost:{1},area={2:0.2f},perimeter={3:0.2f}"
    #       .format(x.radius, x.cost(), x.area(), x.perimeter()))

    # ---------example 2
    B = mc.Box.from_diameter(diameter=12, price=100.0)
    print("calculated area is", B.areaFromPerim())
    print("actual area is", (math.pi*(12**2))/4)
    print(" Actual cost is", 100*B.quantity)
    print("calculated cost is", B.cost())
    # the issue here is the perimeter gets updated in class
    # Box updates perimeter->Ring class gets updated ->area updated with this newPerimeter
    # to avoid --> create copies and use it in class, so that the child class don't
    # modify it--use _perimeter=perimeter


if __name__ == "__main__":
    main()
