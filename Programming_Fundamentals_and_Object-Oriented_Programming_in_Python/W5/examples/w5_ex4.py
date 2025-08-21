class Grandparent:
    def house(self):
        print("Grandparent's house")
    def method(self):
        print("Grandparent")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")
    def method(self):
        print("parent")

class Child(Parent):
    def bike(self):
        print("Child's bike")
    def method(self):
        super().method()
        print("child")

c = Child()
c.house()
c.car()
c.bike()
c.method()
