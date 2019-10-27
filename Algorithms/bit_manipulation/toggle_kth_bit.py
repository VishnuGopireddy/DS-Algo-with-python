#RBR interview prep
#toggle kth bit of a number
'''
we assume that index of LSB is 0 here k = 3
ex: 1000010
xor 0001000 (to get this: 1 << k)
-------------
ans 1001010  ----> return
-------------
TIME: O(log n)
'''


def toggle_kth_bit(num, k):
    '''
    :param num: integer, number to test
    :param k: integer, position to test
    :return: integer, with kth bit set
    '''
    num2 = 1 << k
    return num ^ num2


print(toggle_kth_bit(89, 2))