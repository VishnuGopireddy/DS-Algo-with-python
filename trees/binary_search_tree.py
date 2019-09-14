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

    def delete(self,data):
        parent, child = self.get_parent1(data)
        print(parent.data, child.data)
        #case 1 = leaf
        if child.left == None and child.right == None:
            if data > parent.data:
                parent.right = None
            else:
                parent.left = None
        #case 2 = single child
        elif child.left == None or child.right == None:
            if data > parent.data:
                if child.left:
                    parent.right = child.left
                else:
                    parent.right = child.right

            else:
                if child.left:
                    parent.left = child.left
                else:
                    parent.left = child.right
        else:
            #case3 --> node with two children
            current = self.get_min_right(child)
            self.delete(current.data)
            print('-->',current.data)
            if data > parent.data:
                parent.right = current
            elif data < parent.data:
                parent.left = current
            else:
                self.root = current

            current.left, current.right = child.left, child.right

    def get_min_right(self,current):

        while current.left != None or current.right != None:
            if current.right:
                current = current.right
            elif current.left:
                current = current.left
        return current


    def get_parent1(self,data):
        if self.root.data == data:
            return self.root,self.root
        else:
            parent,child = self.root, self.root
            while child.data != data:
                if child.data > data:
                    parent = child
                    child = child.left
                elif child.data < data:
                    parent = child
                    child = child.right

            return parent,child

    def get_parent(self,parent,child):
        if parent:
            if parent.left and parent.left.data == child:
                return parent,child
            if parent.right and parent.right.data == child:
                return parent,child
            else:
                return self.get_parent(parent.left,child) or self.get_parent(parent.right,child)

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

    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.data)
            self.inorder(start.right)
        return


bst = BST()
bst.insert(5)

bst.insert(2)
bst.insert(15)
bst.insert(20)
bst.insert(8)
bst.insert(18)
#print("Pre-order is :")
#bst.preorder(bst.root)
#print("Inorder is :")
#bst.inorder(bst.root)
bst.find(50)
bst.delete(5)

#print(bst.root.right.right.left.data)
bst.preorder(bst.root)