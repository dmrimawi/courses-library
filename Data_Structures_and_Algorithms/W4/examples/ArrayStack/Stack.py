class ArrayStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.is_full():
            print("The Stack is full!")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            return None
        to_return = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return to_return

    def peak(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

