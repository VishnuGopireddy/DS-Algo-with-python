#https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
'''
LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.
An efficient solution is based on below formula for LCM of two numbers ‘a’ and ‘b’.

   a x b = LCM(a, b) * GCD (a, b)

   LCM(a, b) = (a x b) / GCD(a, b)
'''


def gcd(a,b):
    '''
    :param a: int
    :param b: int
    :return: GCD of a and b
    '''
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
def lcm(a,b):
    '''
    :param a: int
    :param b: int
    :return: lcm of a and b
    '''
    return (a*b)/gcd(a,b)

a = 15
b = 30
print('LCM of %d and %d is %d'%(a,b,lcm(a,b)))