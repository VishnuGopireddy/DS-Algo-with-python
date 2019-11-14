#https://www.geeksforgeeks.org/find-the-missing-number/
'''
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list.
One of the integers is missing in the list. Write an efficient code to find the missing integer.

This can be solved by XOR operation and sum approach.
Using XOR:
1) XOR all the array elements, let the result of XOR be X1.
2) XOR all numbers from 1 to n, let XOR be X2.
3) XOR of X1 and X2 gives the missing number.
'''

def get_missing(arr):
    n = len(arr)
    x1, x2 = 1, arr[0]
    for i in range(1,n):
        x2 = x2 ^ arr[i]

    for i in range(2,n+2):
        x1 = x1 ^ (i)

    return x1 ^ x2

arr = [1, 2, 4, 6, 3, 7, 8]
print(get_missing(arr))

