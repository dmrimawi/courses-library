class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    # def __hello(self):
    #     print("This is a private method")


class Student(Person):
    def __init__(self, name, student_id):
        # Person.__init__(name)
        super().__init__(name) # Calling constructor of the parent class
        self.student_id = student_id

    def show_id(self):
        print(f"My ID is {self.student_id}.")

    def greet(self):
        super().greet() # Calling method from the parent class
        print("I am also a student.")
        # super().__hello()


s = Student("Alice", "S123")
s.greet() # Accessing parent method
s.show_id() # Accessing subclass method
print(s.name) # Accessing data member from parent class
