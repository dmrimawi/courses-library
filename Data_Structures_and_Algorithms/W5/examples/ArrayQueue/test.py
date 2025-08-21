from array_queue import ArrayQueue


q = ArrayQueue(capacity=4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q)
