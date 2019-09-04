class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        new_node.next = self.head

    def print_list(self):
        curr = self.head
        while curr.next is not self.head:
            print(curr.data)
            curr = curr.next
        print(curr.data)
c = circular()
c.append(10)
c.append(15)
c.append(20)
c.print_list()

