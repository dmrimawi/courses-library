class Animal:
    def speak(self):
        print("Animal speaks")
    

class Dog(Animal):
    def bark(self):
        print("Dog barks")
# Usage
d = Dog()
d.speak()
d.bark()
