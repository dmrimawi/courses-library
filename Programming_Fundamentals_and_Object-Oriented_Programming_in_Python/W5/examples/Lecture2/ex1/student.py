from person import Person


class Student(Person):
    def __init__(self, student_id, major, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def study(self):
        print(f"My major is {self.major}")

    def introduce(self):
        super().introduce()
        print(f"My student ID is: {self.student_id}")
        self.study()
