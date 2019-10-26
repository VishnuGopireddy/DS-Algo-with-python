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

        temp.prev = curr
        temp.next = curr.next
        curr.next.prev = temp
        curr.next = temp


    def find_item(self,item):
        curr = self.head
        while curr.next and curr.data != item:
            curr = curr.next
        if curr.data == item:
            return True
        else:
            return False

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
d.append(100)
d.insert_pos(50,5)
d.print_list()
