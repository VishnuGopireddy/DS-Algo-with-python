#https://www.geeksforgeeks.org/c-program-find-gcd-hcf-two-numbers/
'''
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
            return gcd(a,b-a)
