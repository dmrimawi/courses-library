from heap_class import Heap

def heap_sort(a):
    h = Heap(a)
    result = []
    while len(h) > 0:
        result.append(h.pop())
    return result

h = Heap(arr = [22, 13, 17, 11, 6, 7, 3, 5])
print(h.data)
h.push(4)
print(h.data)
print(h.pop())
print(h.data)

a = [50, 12, 70, 15, 1, 33, 0]
print(heap_sort(a)) # O(n logn)



