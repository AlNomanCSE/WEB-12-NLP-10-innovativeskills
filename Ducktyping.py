class Dog:
    def sound(self):
        return "Woof!"


class Cat:
    def sound(self):
        return "Meow!"


class Guitar:
    def sound(self):
        return "Strum!"


def make_sound(xyz):
    print(xyz.sound())


make_sound(Dog())
make_sound(Cat())
