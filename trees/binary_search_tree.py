class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)


    def _insert(self,curr,data):
        if data < curr.data:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert(curr.left,data)
        elif data > curr.data:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(curr.right,data)
        else:
            print("Value is already present in the tree")

    def find(self,data):
        is_found = False
        if self.root.data is None:
            print("Tree is empty")
            is_found = False
        else:
            is_found = self._find(data,self.root)

        if is_found:
            print("value is present")
        else:
            print("value is not present")


    def _find(self,data,curr):
        if curr.data == data:
            return True
        elif data < curr.data and curr.left:
            return self._find(data,curr.left)

        elif data > curr.data and curr.right:
            return self._find(data, curr.right)

    def preorder(self,start):
        if start:
            print(start.data)
            self.preorder(start.left)
            self.preorder(start.right)
        return

bst = BST()
bst.insert(5)
bst.insert(2)
bst.insert(15)
bst.insert(20)
bst.insert(8)
bst.insert(18)
bst.preorder(bst.root)
bst.find(5)