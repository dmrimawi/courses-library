from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_start(self, data): # O(1)
        #     head
        # insert_at_start(5)
        # self.head = None
        # [5] -> None
        # self.head -> [5] -> None
        # insert_at_start(7)
        # [7] -> [5] -> None
        # self.head -> [7] -> [5] -> None
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data): # O(n)
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def insert_at_index(self, data, index): # O(n)
        # insert_at_index(8, 1)
        # self.head -> [7] -> [5] -> None
        # self.head -> [7] -> [8] -> [5] -> None
        self.size += 1
        if index == 0:
            self.insert_at_start(data)
            return
        count = 0
        current = self.head
        while current is not None and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += f"[{temp.data}]->"
            temp = temp.next
        result += "None"
        return result

    def length(self): # O(n)
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def get_size(self):
        return self.size

    def delete_from_start(self): # O(1)
        if self.head is not None:
            self.head = self.head.next
            self.size -= 1

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.size -= 1
            return 
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.size -= 1

    def delete_by_key(self, key): # O(n)
        if self.head is None:
            return
        if self.head.next is None:
            if self.head.data == key:
                self.head = None
                self.size -= 1
            return
        if self.head.data == key:
            self.delete_from_start()
            return
        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def search(self, key): # O(n)
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False
