import math
from node import Node


class HashTable:
    def __init__(self, size=7, threshold=0.7):
        self.size = size
        self.threshold = threshold
        self.count = 0
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def load_factor(self):
        return self.count / self.size

    def is_prime(self, x):
        y = int(math.sqrt(x))
        for i in range(2, y):
            if x % i == 0:
                return False
        return True

    def find_next_prime(self):
        double_size = 2 * self.size
        while not self.is_prime(double_size):
            double_size += 1
        return double_size

    def rehash(self):
        old_table = self.table
        self.size = self.find_next_prime()
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            if node is not None:
                self.insert(node.key, node.value)

    def insert(self, key, value):
        self.count += 1
        if self.load_factor() >= self.threshold:
            self.rehash()
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            if self.table[indx] is None:
                self.table[indx] = Node(key, value)
                return
            indx = (indx + 1) % self.size
            probe += 1

    def delete(self, key):
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            node = self.table[indx]
            if node and node.key == key:
                self.table[indx] = None
                self.count -= 1
                return True
            indx = (indx + 1) % self.size
            probe += 1
        return False

    def search(self, key):
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            node = self.table[indx]
            if node and node.key == key:
                return node
            indx = (indx + 1) % self.size
            probe += 1
        return None
