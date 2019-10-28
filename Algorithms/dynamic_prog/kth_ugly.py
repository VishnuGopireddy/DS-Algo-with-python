#RBR Interview Prep
#Find kth ugly number
'''
Ugly number: A ugly number is a number which contain primes factors as 2,3,5
Ex: 1,2,3,4,5,6,8,9,10,12,15 ..............

Approach 1: Brute Force

Approach 2: Dynamic Programming

if x is an ugly number then next number is always min(x*2, x*3, x*5)
'''
def get_kthugly(kth):
    '''
    :param k: integer
    :return: kth ugly number
    '''
    ugly = [0] * kth
    i2, i3, i5 = 0, 0, 0
    ugly[0] = 1
    next_2, next_3, next_5 = 2, 3, 5
    for i in range(1, kth):
        ugly[i] = min(next_2, next_3, next_5)
        if ugly[i] == next_2:
            i2 = i2 + 1
            next_2 = ugly[i2] * 2
        if ugly[i] == next_3:
            i3 = i3 + 1
            next_3 = ugly[i3] * 3
        if ugly[i] == next_5:
            i5 = i5 + 1
            next_5 = ugly[i5] * 5

    print(ugly)
    return ugly[-1]


print(get_kthugly(50))