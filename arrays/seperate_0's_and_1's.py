# RBR Interview PREP
# Seperate 0's and 1's in an array
'''
Given a binary array(only 0's and 1's seperate all zero's and ones's in an array
Example: 1001110
Sol: 0001111

Approach 1: (Count sort)
count all 1's and 0's then add all zeros in the front and 1's at the end.
TIME: O(n)

Approach 2:
Take left pointer and right pointer do swapping
TIME: O(N)
'''

arr = [1, 0, 0, 1, 1, 0, 1, 1, 0]
n = len(arr) - 1
l, r = 0, n
while l <= r:
    if arr[l] == 0:
        l = l + 1
    if arr[r] == 1:
        r = r - 1
    else:
        arr[l], arr[r] = arr[r], arr[l]
        l = l + 1
        r = r - 1
print(arr)