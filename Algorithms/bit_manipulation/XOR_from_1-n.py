#calculate XOR from 1 to n
'''
https://www.geeksforgeeks.org/calculate-xor-1-n/
NAIVE: O(n)

but can be done in O(1)

case 1: If n % 4 == 0 then return n
case 2: If n % 4 == 1 then return 1
case 3: If n % 4 == 2 then return n + 1
case 4: If n % 4 == 3 then return 0
'''