class ArrayQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full!")
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peak(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def __str__(self):
        print(self.queue)
        st = ""
        indx = self.front
        count = 0
        while count < self.capacity:
            st += f"[{self.queue[indx]}] -> "
            count += 1
            indx = (indx + 1) % self.capacity
        return st