class Heap:
    def __init__(self, arr=[]):
        self.data = []
        if len(arr) > 0:
            self.data = arr
            self.build_heap()

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def root_indx(self, index):
        return (index - 1) // 2

    def heapify_down(self, index):
        length = len(self.data)
        while True:
            left = self.left_child(index)
            right = self.right_child(index)
            small = index
            if left < length and self.data[left] < self.data[small]:
                small = left
            if right < length and self.data[right] < self.data[small]:
                small = right
            if small == index:
                break
            self.data[index], self.data[small] = self.data[small], self.data[index]
            index = small

    def heapify_up(self, index):
        while index > 0:
            parent = self.root_indx(index)
            if self.data[index] < self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def build_heap(self):
        last_internal_index = (len(self.data) - 2) // 2
        for i in range(last_internal_index, -1, -1):
            self.heapify_down(i)

    def push(self, val):
        self.data.append(val)
        self.heapify_up(len(self.data) - 1)

    def pop(self):
        if len(self.data) > 0:
            self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
            min_value = self.data.pop()
            if len(self.data) > 0:
                self.heapify_down(0)
            return min_value
        return None

    def peek(self):
        if len(self.data) > 0:
            return self.data[0]
        return None

    def __len__(self):
        return len(self.data)
