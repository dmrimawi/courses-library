from hash import HashTable

# Given an array of integers and a target T, determine whether there exist two indices i ≠ j such
# that a[i] + a[j] = T.
def exercise_1(array, t):
    print("exercise 1")
    ht = HashTable()
    for i in range(len(array)):
        node = ht.search(t - array[i])
        if node:
            print(f"Found indicies {node.value}: {node.key} and {i}: {array[i]}")
            break
        ht.insert(array[i], i)

# Given a string s, find the first character with frequency 1 when scanning left to right.
def exercise_2(st):
    print("exercise 2")
    ch_dict = {}
    for ch in st:
        if ch_dict.get(ch) is None:
            ch_dict[ch] = 0
        ch_dict[ch] += 1
    for ch in st:
        if ch_dict[ch] == 1:
            print(ch)
            break

# Given a list A, determine if any value appears at least twice.
def exercise_3(array):
    print("exercise 3")
    count_dict = {}
    for ch in array:
        if count_dict.get(ch) is None:
            count_dict[ch] = 0
        count_dict[ch] += 1
    for ch in count_dict.keys():
        if count_dict[ch] > 1:
            print(ch)

# ht = HashTable(size=7, threshold=0.7)
# for k, v in [(50, 'A'), (700, 'B'), (76, 'C'), (85, 'D'), (92, 'E')]:
#     ht.insert(k, v)
# print('92 ->', ht.search(92))
# print(ht.table)
# ht.delete(76)
# print('76 ->', ht.search(76))
# print(ht.table)

array = [2, 3, 9, 12, 11, 1]
t = 20
exercise_1(array, t)

exercise_2("hello world!")
exercise_2("llo world!")
exercise_2("lloworld!")


array = [1, 2, 3, 1, 2, 3, 1, 5, 6, 6]
exercise_3(array)
