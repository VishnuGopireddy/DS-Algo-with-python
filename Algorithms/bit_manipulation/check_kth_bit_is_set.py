# RBR Interview Prep
# Check kth bit is set or not
'''
we assume that index of LSB is 0 here k = 3
ex: 1001010
and 0001000 (to get this: 1 << k)
-------------
ans 0001000  ----> if set then sol > 0; else sol = 0
-------------
TIME: O(logn)
'''


def check_kth_bit(num, k):
    '''
    :param num: integer, number to test
    :param k: integer, position to test
    :return: 0 if not set
             1 if set
    '''
    num2 = 1 << k
    if num & num2 > 0:
        return 1
    else:
        return 0


print(check_kth_bit(89, 2))
