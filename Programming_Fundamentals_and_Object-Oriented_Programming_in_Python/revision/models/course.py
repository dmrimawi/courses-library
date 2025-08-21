

class Course:
    def __init__(self, id, name, students=[]):
        self.id = id
        self.name = name
        self.students = students

    def __print_not_ranked(self):
        for student in self.students:
            student.introduce()

    def __print_ranked(self):
        for i in range(len(self.students)):
            for j in range(i, len(self.students)):
                if self.students[i].get_scores_avg() < self.students[j].get_scores_avg():
                    stud = self.students[i]
                    self.students[i] = self.students[j]
                    self.students[j] = stud
        self.__print_not_ranked()

    def show_students(self, rank=False):
        if not rank:
            self.__print_not_ranked()
        else:
            self.__print_ranked()

    def print_class(self):
        print(f"Class id: {self.id}, class name is {self.name}")
        print("-" * 30)