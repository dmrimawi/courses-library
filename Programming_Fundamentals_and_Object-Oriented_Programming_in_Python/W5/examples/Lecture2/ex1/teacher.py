from person import Person
from staff import Staff


class Teacher(Person, Staff):
    def __init__(self, name, age, employee_id, subjects, department, salary):
        super().__init__(name, age)
        # super().__init__(department, salary)
        self.department = department
        self.salary = salary
        self.employee_id = employee_id
        self.subjects = subjects
    
    def teach(self):
        print("I teach the following subjects:")
        for sub in self.subjects:
            print(sub)

    def introduce(self):
        super().introduce()
        super().display_staff_info()
        self.teach()

