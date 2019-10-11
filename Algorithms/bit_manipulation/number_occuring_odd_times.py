#https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times
'''
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3
'''

def odd_ocuurance(arr):
    res = 0
    for i in arr:
        res = res ^ i
    return res
arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(odd_ocuurance(arr))


