try:
    # num = int(input("Enter a number: "))
    # result = 10 / num
    # print(result)
    print("ex1 finish")
except ValueError:
    # You can have more than one statment
    print("You must enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


def print_upper(text):
    try:
        print(text.upper())
    except AttributeError:
        print("Invalid input: expected a string, got NoneType or other.")
print_upper(None)

try:
    with open("nonexistent.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")


class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

try:
    set_age(-5)
except ValueError as e:
    print("Error:", e)
except InvalidAgeError as e:
    print("Age error:", e)
except Exception as e:
    print("Exception:", e)


try:
    file_name = "data.txt"
    f = open(file_name, "r")
    content = f.read()
    if not content:
        raise ValueError("File is empty.")
except FileNotFoundError:
    print("Error: File does not exist.")
except ValueError as ve:
    print("Error:", ve)
except TypeError:
    print("Error: Invalid operation on file.")
except Exception as e:
    print("General error:", e)
finally:
    try:
        f.close()
        print("File closed successfully.")
    except Exception:
        print("File was never opened, so nothing to close.")


try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid integer.")
else:
    print("Good job! You entered:", number)

