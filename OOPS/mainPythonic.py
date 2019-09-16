

from pythonic import Ring
from inheritance import petAnimal


def main():
    # # --begin pythonic---
    print("center of Ring is at:{} ".format(Ring.center))
    r = Ring(price=10.0)
    print(r.__dict__)
    print("radius:{0}, cost:{1},price:{2}".format(r.radius, r.cost(),
                                                  r.price))
    # its updated for the instance created with r
    print("center of Ring after update is at:{} ".format(Ring.center))
    # --end pythonic

    # ---begin inheritance
    p = petAnimal("cat", "kitty", test=99)
    p.petSize()
    p.sound()
    print(p.test, p.name, p.test)
    k = petAnimal("doggo", "taruntala")
    print(k.test, k.name, k.test)


if __name__ == "__main__":
    main()
