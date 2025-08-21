import os
from utils.file_handler import read_file, write_file
from models.students import Student
from models.course import Course


STUDENT_FILE = os.path.join("data", "students.txt")

class Main:
    def menu(self):
        """
        print the main menu
        """
        print("What is your choice:")
        print("""
            1. Show all students
            2. Show all classes
            3. Show students in class (should ask if ranked or not)
            4. Register a new student
            5. Create new class
            6. Save and exit
              """)
        ch = input("You choice: ")
        try:
            ch = int(ch)
            return ch
        except ValueError:
            print("You have to enter a number")
        return -1

    def load_students(self):
        students = []
        lines_in_students_file = read_file(STUDENT_FILE)
        for line in lines_in_students_file:
            student_data = line.strip().split(",")
            id = student_data[0]
            name = student_data[1]
            year = int(student_data[2])
            scores = student_data[3].split("|")
            stud = Student(id, name, year, scores)
            students.append(stud)
        return students

    def get_students_by_id(self, ids, students):
        studs = []
        for id in ids:
            for stud in students:
                if id == stud.id:
                    studs.append(stud)
                    break
        return studs

    def load_courses(self, students):
        courses = []
        lines_in_courses_file = read_file(os.path.join("data", "courses.txt"))
        for line in lines_in_courses_file:
            course_data = line.strip().split(",")
            id = course_data[0]
            name = course_data[1]
            ids = course_data[2].split("|")
            print(ids)
            studs = self.get_students_by_id(ids, students)
            course = Course(id, name, studs)
            courses.append(course)
        return courses

    def show_all_students(self, students):
        for stud in students:
            stud.introduce()

    def show_all_courses(self, courses):
        for course in courses:
            course.print_class()

    def get_class_by_id(self, courses, id):
        for course in courses:
            if course.id == id:
                return course

    def get_students_data_for_file(self, students):
        out = ""
        for stud in students:
            scores = "|".join(stud.scores)
            line = f"{stud.id},{stud.name},{stud.year_of_birth},{scores}"
            out = f"{out}\n{line}"
        return out

    def run(self):
        students = self.load_students()
        courses = self.load_courses(students)
        ch = self.menu()
        while True:
            if ch == 1:
                self.show_all_students(students)
            elif ch == 2:
                self.show_all_courses(courses)
            elif ch == 3:
                rank = input("Enter 1 for ranked list, and 0 for normal print: ")
                if rank == "1":
                    rank = True
                else:
                    rank = False
                self.show_all_courses(courses)
                class_id = input("Enter class id: ")
                course = self.get_class_by_id(courses, class_id)
                course.show_students(rank=rank)
            elif ch == 6:
                data = self.get_students_data_for_file(students)
                write_file(STUDENT_FILE, data=data)
                break
            ch = self.menu()


if __name__ == "__main__":
    main = Main()
    main.run()
