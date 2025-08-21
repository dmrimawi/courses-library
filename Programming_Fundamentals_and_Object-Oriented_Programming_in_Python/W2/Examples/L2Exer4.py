"""
Compute the sum of all list elements.
Count how many numbers are positive or negative.
Keep reading numbers from user until -1 is entered
"""
summation = 0
postivies = 0
negatives = 0

arr = []

num = int(input("Enter a number: "))
while num != -1:
    arr.append(num)
    num = int(input("Enter a number: "))

for n in arr:
    summation = summation + n
    if n < 0:
        negatives = negatives + 1
    else:
        postivies = postivies + 1

print(f"Sum: {summation}")
print(f"Neg: {negatives}")
print(f"Pos: {postivies}")
# x = 2
# match x:
#     case 2: 
#         print("hello")
#     case 6:
#         print("World!")


