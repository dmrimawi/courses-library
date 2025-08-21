class Course:
    def __init__(self, title, students=[]):
        self.title = title
        self.students = students

    def enroll(self, sts):
        self.students.append(sts)

    def get_info(self):
        students = ""
        for student in self.students:
            students = f"{students}{student.get_info()}\n"
        return f"Course {self.title}, registered students are: {students}"
