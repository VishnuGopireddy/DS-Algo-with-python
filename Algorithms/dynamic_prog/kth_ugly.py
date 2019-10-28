#RBR Interview Prep
#Find kth ugly number
'''
Ugly number: A ugly number is a number which contain primes factors as 2,3,5
Ex: 1,2,3,4,5,6,8,9,10,12,15 ..............

Approach 1: Brute Force

Approach 2: Dynamic Programming

if x is an ugly number then next number is always min(x*2, x*3, x*5)
'''
def get_kthugly(k):
    '''
    :param k: integer
    :return: kth ugly number
    '''
