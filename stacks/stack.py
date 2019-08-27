
class Stacks():
    '''
    Basic operations with stack
    A stack is created with a list
    '''
    def __init__(self):
        '''
        Create a stack with an empty list
        '''
        self.items = []

    def push(self,item):
        '''
        Push an item into stack
        :param item: A item to push into stack
        :return: None
        '''
        self.items.append(item)

    def pop(self):
        '''
        pops an item
        :return: popped element
        '''
        return self.items.pop()

    def peek(self):
        '''
        Get the top most element from the stack
        :return: top most element from the stack
        '''
        return self.items[-1]

    def isempty(self):
        '''
        Check wheater a stack is empty or nor
        :return: True/ False
        '''
        return self.items == []
    def get_items(self):
        '''
        Get all the items in the stack
        :return: list of elements in a stack
        '''
        return self.items

s = Stacks()

s.push(1)
s.push(2)
s.push(3)
print(s.get_items())
print(s.isempty())
s.pop()
print(s.peek())
print(s.get_items())