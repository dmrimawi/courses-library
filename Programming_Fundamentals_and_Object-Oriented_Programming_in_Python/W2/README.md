# Week 2 – Introduction to Python

**Authors.** Diaeddin Rimawi ([dmrimawi@gmail.com](mailto:dmrimawi@gmail.com)), Refat Othman ([ref3tothman@gmail.com](mailto:ref3tothman@gmail.com))

---

## Lecture 1: Introduction to Python & Sequential Programming

### Lecture Goals

* Familiarize students with the Python programming environment.
* Understand the basic structure and syntax of a Python program.
* Learn how to perform sequential operations using variables, input/output, and conditionals.
* Develop foundational skills for writing basic Python programs involving decisions.

### Topic 1: Installing Python and VS Code

* **What is Python?**
  Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data analysis, AI, automation, and education. Python emphasizes code readability and has a large, supportive community.
* **Install Python from [python.org](https://www.python.org/).**
  Guide students to download and install the latest version. Emphasize adding Python to the system PATH.
* **Install and configure VS Code with Python extension.**
  Introduce VS Code as a lightweight editor. Show how to install the Python extension and configure the interpreter. Mention syntax highlighting, IntelliSense, and debugging.
* **Run a sample file:**

```python
print("Hello, world!")
```

Explain how the interpreter processes code line by line.

### Topic 2: Run a Simple Program + Errors

* **Structure of a simple program.** Sequential execution, indentation, syntax rules.
* **Syntax errors:**

```python
print("Hello"  # missing closing parenthesis
x == 5         # comparison without context
```

* **Runtime errors:**

```python
x = int("abc")  # ValueError
y = 1 / 0       # ZeroDivisionError
```

Encourage reading error messages carefully.

### Topic 3: Sequential Programming

* **Variables and data types.** Introduce `int`, `float`, `str`. Emphasize dynamic typing.
* **Input and output:**

```python
name = input("Enter your name: ")
print("Hello", name)
```

* **Basic calculations:**

```python
a = float(input("Enter a: "))
b = float(input("Enter b: "))
print("Sum:", a + b)
```

**Exercises:**

* Read two numbers and calculate their sum and average.
* Convert Celsius to Fahrenheit: `F = C * 9/5 + 32`
* Calculate the perimeter of a rectangle: `2 × (length + width)`

### Topic 4: If Statements

* **Overview.** Using `if`, `if-else`, `if-elif-else`.
* **Conditions and operators.**

  * Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
  * Logical: `and`, `or`, `not`
  * Identity: `is`
  * Membership: `in`
* **Example:**

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C or below")
```

**Exercises:**

* Compare two numbers and print the greater.
* Check if a character is inside a string.
* Create a login system:

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
```

---

## Lecture 2: Arrays and Loops

### Lecture Goals

* Learn to define and manipulate collections using arrays (lists).
* Understand and apply iteration with `for` and `while` loops.
* Combine lists and loops to solve common problems.

### Topic 1: Arrays (Lists)

* **Introduction to lists:**

```python
nums = [1, 2, 3]
names = ["Ali", "Sara"]
mixed = [42, "Hello", 3.14]
```

* **Accessing and modifying:**

```python
print(nums[0])
nums[1] = 20
print(nums)
```

* **Iterating:**

```python
for name in names:
    print("Hello", name)
```

* **User input to fill list:**

```python
arr = []
for i in range(3):
    arr.append(int(input("Enter number: ")))
```

* **Common operations:**

```python
print(len(arr))
arr.append(99)
arr.remove(99)
arr.sort()
print("Sara" in names)
```

### Topic 2: Loops

* **For loop basics:**

```python
for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)
```

* **While loop basics:**

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

* **Combining loops with arrays:**

```python
arr = [5, 3, 8]
for value in arr:
    print(value)
```

* **Input validation:**

```python
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")
```

**Exercises:**

* Print even numbers up to a user-defined number N.
* Generate multiplication table for a given number.
* Search for a specific value in a list.
* Find and print the smallest number in a list.
* Find the maximum value in a list.
* Compute the sum of all list elements.
* Count how many numbers are positive or negative.
* Print the list in reverse order.
