#https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
'''
Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n. While i divides n, print i and divide n by i. After i fails to divide n, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps. So print n if it is greater than 2.
'''

def primefactors(num):
    '''
    :param num: int
    :return: list of prime factor
    '''
    from math import  sqrt, ceil
    primes = []
    n = num
    while num > 1:
        for i in range(2, ceil(sqrt(n))+1, 1):
            if num % i == 0:
                num = num // i
                primes.append(i)
                break
    return primes


print(primefactors(125))
