# Compare two numbers and print the greater..
"""
    AND
    x y | result
    T T | T
    F T | F
    T F | F
    F F | F

    OR
    x y | result
    T T | T
    F T | T
    T F | T
    F F | F
"""
# Start
# Ask the user to enter the num1
# Input num1
num1 = int(input("enter num1 "))
# Ask the user to enter the num2
# Input num2
num2 = int(input("enter num2 "))
# if num1 > num2 then
if (num1 > num2):
#   print num1 is the greater
    print(f"{num1} is greater")
# else
else:
#   print num2 is the greater
    print(f"{num2} is greater")
# end if
# end
