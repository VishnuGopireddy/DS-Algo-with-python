class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class btree:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            self.head = Node(data)

