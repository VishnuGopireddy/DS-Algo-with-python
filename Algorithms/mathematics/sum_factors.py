#https://www.geeksforgeeks.org/sum-of-factors-of-a-number-using-prime-factorization/
'''
Sum of Factors of a Number using Prime Factorization
Given a number N. The task is to find the sum of all factors of the given number N.
Ex:
Input : N = 12
Output : 28
All factors of 12 are: 1,2,3,4,6,12
'''



def primefactors(num):
    '''
    :param num: int
    :return: list of prime factor
    '''
    from math import sqrt, ceil
    primes = []
    n = num
    while num > 1:
        for i in range(2, ceil(sqrt(n))+1, 1):
            if num % i == 0:
                num = num // i
                primes.append(i)
                break
    return primes

def sum_primefactors(num):
    '''
    :param num: num
    :return:  sum of factors
    '''
    prime_factors = primefactors(num)
    counts = {i:prime_factors.count(i) for i in prime_factors}
    tot_sum = 1
    print(counts)
    for i in counts.keys():
        t = 1
        for j in range(1,counts[i]+1):
            print(i,j)
            t = t + (i**j)
        tot_sum = t * tot_sum
    print(tot_sum)

sum_primefactors(1100)