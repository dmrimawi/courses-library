from models.human import Human


class Student(Human):
    def __init__(self, id, name, year_of_birth, scores=[]):
        super().__init__(name, year_of_birth)
        self.id = id
        self.scores = scores

    def get_scores_avg(self):
        summation = 0
        for score in self.scores:
            summation += float(score)
        avg = -1
        try:
            avg = summation / len(self.scores)
        except ZeroDivisionError:
            print(f"There are not scores for this student {self.id}")
        return avg

    def introduce(self):
        print(f"My name is: {self.name}")
        age = 2025 - self.year_of_birth
        print(f"My age is {age}")
        avg = self.get_scores_avg()
        print(f"My student id is {self.id}, and my average is {avg}")
        print("-" * 30)

    def add_score(self, score):
        self.scores.append(score)

