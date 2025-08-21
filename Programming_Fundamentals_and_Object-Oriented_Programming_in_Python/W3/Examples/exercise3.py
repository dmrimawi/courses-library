def statistics(arr):
    max = min = arr[0]
    pos = neg = 0
    for num in arr:
        if max < num:
            max = num
        if min > num:
            min = num
        if num < 0:
            neg += 1
        else:
            pos += 1
    print(f"Max: {max}, min: {min}, pos: {pos}, neg: {neg}")
    with open("out.txt", "w") as f:
        f.write(f"Max: {max}, min: {min}, pos: {pos}, neg: {neg}")
        f.close()

arr = []
for i in range(10):
    arr.append(int(input(f"Enter num{i}: ")))

statistics(arr)
