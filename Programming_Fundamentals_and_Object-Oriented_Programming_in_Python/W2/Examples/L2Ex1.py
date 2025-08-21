
# Values:  1,2,3,4,5,6
# Indicies:
#      0  1  2  3  4  5
arr = [1, 2, 3, 4, 5, 6]
print(arr[0])
l = ["abc", "def"]
l[1] = "xyz"
print(l[1])

# In Python, array size is dynamic
l_1 = [1, "abc", [1,2,3]]
print(l_1[2])

# Functions
# Append
l2 = [1,2,3]
l2.append(4)
print(l2)
# remove
l2.remove(3)
print(l2)
# sort
l2.sort(reverse=True)
print(l2)

l2.clear()
print(l2)
