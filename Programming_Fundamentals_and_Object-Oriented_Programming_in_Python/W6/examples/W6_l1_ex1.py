# abs_cls1 (abs_method1)

# abs_cls2 (abs_method2) extends abs_cls1 -> has the choice to implement or not

# cls3 extends abs_cls1 -> must implement all abstract methods in abs_cls1, and any other abstract class (multi level)
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        self.name = ""

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        return "Animals are living organisms that move and make sounds."


class Dog(Animal): # classes and abstract classes: Dog extends Animal -> in interfaces: Dog implments Animal
    def make_sound(self):
        print("Bark")

    def move(self):
        print("Walk!")

class Cat(Animal):
    def make_sound(self):
        print("Mew")

    def move(self):
        print("Walk!")


d = Dog()
c = Cat()

d.make_sound()
c.make_sound()

