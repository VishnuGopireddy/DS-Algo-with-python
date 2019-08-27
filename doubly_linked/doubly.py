class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class double_linked:
    def __init__(self):
        self.head = None

    def append(self,item):
        if self.head is None:
            self.head = Node(item)

        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(item)

    def insert_begin(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


d = double_linked()
d.append(1)
d.append(2)
d.append(10)
d.insert_begin(0)
d.print_list()