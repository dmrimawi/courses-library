class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"This dog name is {self.name}")


if __name__ == "__main__":
    my_dog = Dog("rex")
    other_dog = Dog("Boby")
    print(f"The my_dog name is {my_dog.name}")
    print(f"The other_dog name is {other_dog.name}")
    my_dog.bark()
