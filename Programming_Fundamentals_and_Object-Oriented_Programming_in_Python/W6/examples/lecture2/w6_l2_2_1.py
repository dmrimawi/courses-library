try:
    x = input("Enter num1: ")
    y = input("Enter num2: ")
    a = int(x)
    b = int(y)
    r = a / b
    print(r)
except ValueError:
    print("Both values must be numbers")
except ZeroDivisionError:
    print("The second number cannot be zero")
except TypeError as e:
    print("Type error: ", e)
except KeyboardInterrupt:
    print("Process has been killed")
finally:
    print("Goodbye!")
