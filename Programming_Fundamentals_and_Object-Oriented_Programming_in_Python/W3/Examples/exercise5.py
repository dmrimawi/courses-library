# stop: 
# 5^3
# 5 * 5 * 5 * 1
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

def menu():
    print("Select your choice:")
    print("1) square")
    print("2) power")
    print("3) exit")
    ch = int(input())
    p = 2
    if ch == 2:
        p = int(input("Enter the power: "))
    return ch, p

a = int(input("Enter the number: "))
ch, b = menu()
if ch != 3:
    result = power(a, b)
    print(f"The power of {a}^{b} is: {result}")


