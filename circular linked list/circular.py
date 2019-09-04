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

    def delete_item(self,item):
        if self.head == None:
            return False
        else:
            curr = self.head
            prev = curr
            while curr.next != self.head:
                if curr.data == item:
                    prev.next = curr.next
                    prev = curr
                    curr = curr.next
                else:
                    prev = curr
                    curr = curr.next
        return True

c = circular()
c.append(10)
c.append(15)
c.append(20)
c.append(35)
c.append(40)
c.append(50)
c.delete_item(35)
c.print_list()

