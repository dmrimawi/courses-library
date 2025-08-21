from course import Course
from student import Student

mhmd = Student("Mohammad", 123)
suad = Student("Suad", 124)

prog = Course("Programming")
math = Course("Mathmatics", [mhmd])

prog.enroll(suad)
math.enroll(suad)

print(mhmd.get_info())
print("_"*50)
print(prog.get_info())
print("_"*50)
print(math.get_info())
