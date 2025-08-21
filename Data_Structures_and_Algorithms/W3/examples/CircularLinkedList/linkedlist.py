from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data): # O(n)
        #     head
        # insert_at_start(5)
        # self.head = None
        # [5] -> None
        # self.head -> [5] -> None
        # insert_at_start(7)
        # [7] -> [5] -> None
        # self.head -> [7] -> [5] -> None
        new_node = Node(data)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.head.next = self.head
            return
        while temp.next is not self.head:
            temp = temp.next
        new_node.next = self.head
        self.head = new_node
        temp.next = self.head 

    def __str__(self):
        if self.head is None:
            return
        temp = self.head
        list_nodes = ""
        while True:
            list_nodes += "[" + str(temp.data)  + "] -> "
            temp = temp.next
            if temp == self.head:
                break
        return list_nodes

    def length(self): # O(n)
        count = 0
        current = self.head
        while True:
            current = current.next
            if current is self.head:
                break
            count += 1
        return count


