lines = []
with open("data.txt", "r") as f:
    lines = f.readlines()
    f.close()
print(lines)

s = 0
count = 0
for line in lines:
    if line != "\n":
        grade = float(line)
        s = s + grade
        count = count + 1

avg = s / count

print(f"The count is {count}, and the length is {len(lines)}")
print(f"Average is: {avg}")
