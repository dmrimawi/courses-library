# Search for a specific value in a list.
l = [20, 13, 15, 62, 100, 14]

num = int(input("Enter the number you are searching for: "))
if num in l:
    print("Success!")
    print(l.index(num))
else:
    print(f"{num} does not exist")

print("_" * 60)
flag = False
for i in range(len(l)):
    if l[i] == num:
        print(f"{num} is at index {i}")
        flag = True
        break
if flag == False: # not flag, flag == 0
    print(f"{num} does not exist")
