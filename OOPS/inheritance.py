# creating an object Animal


class Animal(object):
    # class variables
    test = 0.2

    def __init__(self, name, species, test=test):
        self.name = name
        self.species = species
        self.test = test

    def sound(self):
        print("meow")

# inheriting the animal class

# also called as child class


class petAnimal(Animal):

    def petSize(self):
        print("small")

    # we can also override the function of parent
    # --can override sound

    def sound(self):
        print("overridden meow")
