#RBR interview prep
#set kth bit of a number
'''
we assume that index of LSB is 0 here k = 3
ex: 1001010
and 1110111 (to get this: complement of (1 << k))
-------------
ans 1000010  ----> return
-------------
TIME: O(log n)
'''





def clear_kth_bit(num, k):
    '''
    :param num: integer, number to test
    :param k: integer, position to test
    :return: integer, with kth bit clear
    '''
    return (num & ~(1 << (k - 1)))


print(clear_kth_bit(32,2))
