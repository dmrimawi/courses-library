# Find and print the smallest number in a list.
arr = []
for i in range(5):
    arr.append(int(input(f"Enter value {i}: ")))
minimum = arr[0]
for i in range(1, 5):
    if minimum > arr[i]:
        minimum = arr[i]
print(minimum)

print(min(arr))
