#count number of setbits
'''
https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
'''
def count_set_bits(n)
    '''
    :param n: integer 
    :return: count as integer
    '''
    return bin(n).count('1')

n = input('enter a number')
count = count_set_bits(n)
print(count)