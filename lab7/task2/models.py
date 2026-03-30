class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def speak(self):
        return "sound"

    def move(self):
        return "moving"

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.habitat


class Dog(Animal):
    def __init__(self, name, age, habitat, breed):
        super().__init__(name, age, habitat)
        self.breed = breed

    def speak(self):
        return "woof"

    def fetch(self):
        return self.name + " runs"


class Cat(Animal):
    def __init__(self, name, age, habitat, color):
        super().__init__(name, age, habitat)
        self.color = color

    def speak(self):
        return "meow"

    def climb(self):
        return self.name + " climbs"