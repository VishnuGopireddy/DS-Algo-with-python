class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class single_linked:
    def __init__(self):
        self.head = None

    def append(self,item):
        '''
        Append item to the list at the last position
        :param item: item which has to be appended
        :return: None
        '''
        if self.head is None:
            self.head = Node(item)

        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = Node(item)



    def insert_begin(self,item):
        '''
        Inserts an element at the begining of the list
        :param item: item to be inserted
        :return: None
        '''
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
        '''
        Prints all the elements in the list
        :return: None
        '''
        curr = self.head
        while curr:
            print(curr.data,end=' ')
            curr = curr.next
        print()


    def delete_item(self,item,singly):
        '''
        Checks wheater a given element is present in the list or not
        and delete the element if it is present

        :param item: Item to be deleted
        :param singly: List on which the item has to be deleted
        :return: Updated list if the item is present else do nothing
        '''

        if singly.find_item(item):
            curr = self.head
            last = self.head
            if curr.data == item:
                self.head = curr.next
            else:
                while (curr.next and curr.data != item):
                    last = curr
                    curr = curr.next
                last.next = curr.next
        else:
            print("Entered element can't be deleted")

    def find_item(self,item):
        '''
        Check wheater given element is present in the list or not
        :param item: item which has to be check
        :return: True if the item is present else False
        '''
        curr = self.head
        while curr.next and curr.data != item:
            curr = curr.next
        if curr.data == item:
            return True
        else:
            return False


    def length(self):
        '''
        Length of the list
        :return: count of the list
        '''
        count = 0
        curr = self.head

        while(curr != None):
            curr = curr.next
            count = count + 1
        return count

    def print_reverse(self):
        '''
        Print a list in reversed order. List remains same
        :return: None
        '''
        curr = self.head
        l = []
        while curr:
            l.append(curr.data)
            curr = curr.next
        print(l[::-1])

    def reverse_list(self):
        '''
        Reverses a linked list
        :return:
        '''

        curr = self.head
        prev = None
        up = curr.next
        while(up):
            #print(curr.data)
            curr.next = prev
            prev = curr
            curr = up
            up = curr.next
        curr.next = prev
        self.head = curr

    def count_occurances(self,item,singly):
        '''
        Count number of times item occures in the list
        :param item: item of the list
        :return: number of times item occured in the list
        '''
        count = 0
        if singly.find_item(item):
            curr = self.head
            while(curr):
                if curr.data == item:
                    count = count + 1
                curr = curr.next

        return count

