#https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
'''
GCD/HCF of two numbers
GCD of two numbers is the largest number that divides both of them.
An efficient solution is to use Euclidean algorithm which is the main algorithm used for this purpose.
The idea is, GCD of two numbers doesn’t change if smaller number is subtracted from a bigger number.
'''



def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a-b,b)
        else:
            return  gcd(a,b-a)

a = 36
b = 13
print('GCD of %d and %d is %d' % (a, b, gcd(a, b)))
