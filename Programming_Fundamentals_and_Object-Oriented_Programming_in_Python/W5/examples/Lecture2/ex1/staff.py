class Staff:
    def __init__(self, department, salary):
        self.department = department
        self.salary = salary

    def display_staff_info(self):
        print(f"This staff member is working in the {self.department} department")
        print(f"The salary of this staff is: {self.salary}")
