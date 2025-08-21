# Print even numbers up to a user-defined number N
n = int(input("Enter the number N: "))

for i in range(0, n, 2):
    print(i)

print("_" * 60)

for i in range(n):
    if i % 2 == 0:
        print(i)

