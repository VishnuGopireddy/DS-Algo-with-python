#Find given number is even or odd using bit manipulation
'''
Approach: For any odd number least significant bit is always set to 1.

Ex:
    9 --> 1001
    15 --> 1111
'''
def isodd(n):
    return 1 if bin(n)[-1] == '1' else 0

n = int(input('enter a number'))
print(isodd(n))
