#https://www.geeksforgeeks.org/count-number-of-bits-to-be-flipped-to-convert-a-to-b-set-2/
'''
Count number of bits to be flipped to convert A to B

Approach:
1. compute A ^ B
2. Calculate #set bits in A ^ B
'''

def bits_required_to_flip(a,b):
    xor = a ^ b
    return  bin(xor).count('1')

a = int(input('Enter A:'))
b = int(input('Enter B:'))
count = bits_required_to_flip(a,b)
print(count, 'bits required')