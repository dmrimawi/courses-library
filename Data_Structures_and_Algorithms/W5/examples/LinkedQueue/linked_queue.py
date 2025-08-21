from node import Node


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        if self.rear is None:
            return True
        return False

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        
    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def __len__(self):
        return self.size
    
    def __str__(self):
        st = ""
        current = self.front
        while current is not None:
            st += f"[{current.value}] -> "
            current = current.next
        st += "None"
        return st