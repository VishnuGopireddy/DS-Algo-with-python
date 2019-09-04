# Sum of two linked lists
# Ex:
#   126
# + 987
# -------
#   1113
#---------
# For simplicity we assume length of both lists are equal and sum of lists in reverse order
from singly_linked.singly import single_linked

def sum_list(l1,l2):
    l1 = l1.head
    l2 = l2.head
    s = single_linked()
    carry = 0
    while l1.next and l2.next:

        x = l1.data + l2.data + carry
        if x < 10:
            s.append(x)
            carry = 0

        else:
            s.append(x % 10)
            carry = 1
        l1 = l1.next
        l2 = l2.next

    s.append(a.data+b.data+carry)
    return s

l1 = single_linked()
l2 = single_linked()

l1.append(6)
l1.append(2)
l1.append(1)
l2.append(7)
l2.append(8)
l2.append(9)
l1.print_reverse()
l2.print_reverse()
s = sum_list(l1,l2)
s.print_reverse()