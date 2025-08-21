from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self._insert(node.left, data) # Simple left-first insertion
            # For complete insertion we can use Queues to track the children

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search(node.left, target) or self._search(node.right, target)

    def search(self, target):
        return self._search(self.root, target)

    def _delete(self, root, key):
        if root is None:
            return None
        if root.data == key:
            # Case 1: Node with no child
            if not root.left and not root.right:
                return None
            # Case 2: Node with only one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Case 3: Node with two children - replace with inorder successor
            succ_parent = root
            succ = root.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            if succ_parent != root:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
            root.data = succ.data
            return root
        root.left = self._delete(root.left, key)
        root.right = self._delete(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end=' ')
            self._inorder(node.right)

    def inorder(self):
        self._inorder(self.root)