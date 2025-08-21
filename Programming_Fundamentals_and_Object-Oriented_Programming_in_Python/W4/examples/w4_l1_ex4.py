class Calculator:
    # def description(self, x, y):
    #     print(f"description1: {x} and {y}")

    def description(self, y):
        print(f"description2: {y}")

    def add(self, datatype, *args):
        if datatype == "int":
            result = 0
            for number in args:
                result += number
            return result
        elif datatype == "string":
            st = ""
            for s in args:
                st = f"{st} {s}"
            return st

calc = Calculator()
print(calc.add("int", 1, 2)) # Output: 3
print(calc.add("int", 1, 2, 3, 4, 5)) # Output: 15
print(calc.add("string", "hi", "bye")) # Output: 15

print(calc.description(1))
# print(calc.description(1, 2))
