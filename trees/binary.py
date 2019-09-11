class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)


    def preorder(self,start):
        if start:
            print(start.value)
            self.preorder(start.left)
            self.preorder(start.right)
        return

    def postorder(self,start):
        if start:
            self.postorder(start.left)
            self.postorder(start.right)
            print(start.value)
        return

    def inorder(self,start):
        if start:
            self.inorder(start.left)
            print(start.value)
            self.inorder(start.right)
    def levelorder(self,start):
        if start is None:
            return
        q = []
        q.append(start)
        while len(q) > 0:
            node = q.pop(0)
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    def height(self,start):
        h = 0
        if start == None:
            return h
        else:
            return max(self.height(start.left) + 1,self.height(start.right) + 1)

'''
                10
               /   \
            15      8
           / \        \            
         20   30       50 
                         \
                          150
'''
from queue import Queue
b = BinaryTree(10)
b.root.left = Node(15)
b.root.right = Node(8)
b.root.left.left = Node(20)
b.root.left.right = Node(30)
b.root.right.right = Node(50)
b.root.right.right.right = Node(150)

print("Pre-order is :",end=' ')
b.preorder(b.root)

print("In-order is :",end=' ')
b.inorder(b.root)

print("Post-order is :",end=' ')
b.postorder(b.root)

print("Level order is :",end=' ')
b.levelorder(b.root)

print("Height of tree is :",end=' ')
print("height is",b.height(b.root))
