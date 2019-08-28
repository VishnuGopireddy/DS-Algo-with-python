class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class single_linked:
    def __init__(self):
        self.head = None

    def append(self,item):
        if self.head is None:
            self.head = Node(item)

        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = Node(item)

    def insert_begin(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def insert_pos(self,item,pos):
        '''
        Insert at any arbitary position
        :param item: Item to insert
        :param pos: starts from 1 ie., begining
        :return: None
        '''

        temp = Node(item)
        i = 2
        curr = self.head
        while i<pos and curr.next != None:
            curr = curr.next
            i = i + 1
        temp.next = curr.next

        curr.next = temp

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


s = single_linked()
s.append(2)
s.append(3)
s.append(10)
s.append(100)
s.insert_begin(1)
#s.print_list()
s.insert_pos(50,5)
s.print_list()