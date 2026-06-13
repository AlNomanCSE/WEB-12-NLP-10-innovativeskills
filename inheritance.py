class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.__class__.__name__} ({self.name})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    # Method Overriding
    def eat(self):
        print(f"{self.name} is eating dog food")

    def bark(self):
        print(f"{self.name} ({self.breed}):Woof!")


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor = indoor

    # Method Overriding
    def eat(self):
        print(f"{self.name} is eating cat food")

    def meow(self):
        print(f"{self.name}:meow!")


dog = Dog("Bruno", 2, "Labrador")
cat = Cat("lao", 1)
# print(dog)
# print(cat)

dog.bark()
cat.meow()


# 1.Multilevel
# 2.Multiple


cat.eat()
