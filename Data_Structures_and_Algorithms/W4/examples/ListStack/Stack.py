from Node import Node


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        to_return = self.top.data
        self.top = self.top.next
        return to_return

    def peak(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None # In C/C++ we have to free the memory
