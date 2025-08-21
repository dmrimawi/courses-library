# define func_name(params):
#   Block
def greet():
    print("Hello!, welcome to Python")

# ق(س) = س2
# 4

greet()
greet()
greet()
greet()

# Types of fucntions 4:
# 1) No parameters, and no return

def say_hello():
    print("Hello!")
say_hello()

# 2) No return
def say_hello_to(name):
    print("Hello, ", name)
say_hello_to("Dia")

# 3) no param
def sum_two_nums():
    x = 5
    y = 5
    s = x + y
    return s

print(sum_two_nums())
result = sum_two_nums()
print(result)

# 4) with param and return
def sum_two_numbers(x, y):
    return x + y

x = 5
y = 5
print(sum_two_numbers(x, y))

