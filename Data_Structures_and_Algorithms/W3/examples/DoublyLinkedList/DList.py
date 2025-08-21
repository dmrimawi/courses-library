from node import Node

class DList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data): # 0
        new_node = Node(data) #  None <- [0] -> None
        if self.head is not None: # None <- [1] <-> [2] <-> [3] -> None
            self.head.prev = new_node # (None <- [0] -> None)  <- [1] <-> [2] <-> [3] -> None
            new_node.next = self.head # (None <- [0] ->  <- [1] <-> [2] <-> [3] -> None
        self.head = new_node # None <- [0] <-> [1] <-> [2] <-> [3] -> None
    

