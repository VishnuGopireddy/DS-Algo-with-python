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
    ugly = [1]
    i2, i3, i5 = 0
    next_2 = 2
    next_3 = 3
    next_5 = 5
    #current = [ugly[i] * 2, ugly[i] * 3, ugly[i] * 5]
    for i in range(1, kth):
        ugly.append(min(next_2, next_3, next_5))
        if ugly[i] == next_2:
            next_2 = next_2 *
        if min(x, y, z) is y:
            ugly.append(y)
            j = j + 1
        if min(x, y, z) is z:
            ugly.append(z)
            k = k + 1
        z = z + 1
    print(ugly)
    return ugly[-1]


print(get_kthugly(50))