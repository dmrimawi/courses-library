# Create a function to sort an array
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                x = arr[i]
                arr[i] = arr[j]
                arr[j] = x
                # arr[i], arr[j] = arr[j], arr[i]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
numbers = bubble_sort(numbers)
print(numbers)

