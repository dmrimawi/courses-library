from Stack import Stack


# We have a limited resources environment with 256 empty slots in array called
# mem, how we can create a stack using this array without the need
# to create new variables

# mem = [0] * 256

# def push(data):
#     mem[mem[0] + 1] = data
#     mem[0] = mem[0] + 1


# def pop():
#     if mem[0] != 0:
#         mem[0] -= 1
#         return mem[mem[0] + 1]
#     return 0

# # Application 3: Recursion

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

def factorial(n):
    call_stack = Stack()
    result = 1
    while n >= 1:
        print(f"Push: {n}")
        call_stack.push(n)
        n -= 1
    while not call_stack.is_empty():
        x = call_stack.pop()
        print(f"POP: {x}")
        result *= x
    return result
# Example usage:
print(factorial(5)) # Output: 120

# Application 2: JVM
# memory_stack = Stack()

# def call_method(fun):
#     memory_stack.push(fun)
#     print(f"Calling method {fun}")

# def return_from_fun():
#     if not memory_stack.is_empty():
#         fun = memory_stack.pop()
#         print(f"Method {fun} finished")


# method1 = "main 26"
# method2 = "is_empty 23"
# method3 = "is_full 30"

# """
# def main():
#     if is_empty
#     .....

# x  = 5
# main()
# y = 10
# a = is_empty()
# if a:
#     b = is_full()
# """
# call_method(method1)
# call_method(method2)
# return_from_fun()
# return_from_fun()


# Application 1: Undo/Redo
# redo_stack = Stack()
# undo_stack = Stack()

# def perform_action(action):
#     undo_stack.push(action)
#     redo_stack.clear()
#     print(f"Perform action: {action}")

# def undo():
#     if not undo_stack.is_empty():
#         last_action = undo_stack.pop()
#         redo_stack.push(last_action)
#         print(f"Undo action: {last_action}")

# def redo():
#     if not redo_stack.is_empty():
#         last_action = redo_stack.pop()
#         undo_stack.push(last_action)
#         print(f"Redo action: {last_action}")


# action1 = "1 * 2"
# action2 = "2 * 3"
# perform_action(action1)
# perform_action(action2)

# undo()
# undo()
# redo()

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)

# print(s.pop())
# print(s.peak())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
