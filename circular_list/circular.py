class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_list:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
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
        print('-'*100)

    def delete_item(self,item):
        if self.head == None:
            return False
        elif self.head.data == item:
            curr = self.head.next
            prev = self.head
            while curr != self.head:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            self.head = self.head.next

        else:
            curr = self.head
            prev = curr
            while curr.next != self.head:
                if curr.data == item:
                    prev.next = curr.next
                prev = curr
                curr = curr.next
        return True

#c = circular_list()
#c.append(10)
#c.append(15)
#c.append(25)
#c.print_list()
#c.delete_item(10)

#c.print_list()
#c.append(10)
#c.print_list()

#print(c.head.data)
#print(c.head.next.data)
#print(c.head.next.next.data)
#print(c.head.next.next.next.data)


