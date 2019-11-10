#RBR Inter Prep
#Given an array eith even and odd number seperate all even and odd numbers
'''
Example: [12,15,10,8,7,10,18,5,4,3,12,16]
Ans : [3, 15, 5, 7, 8, 10, 18, 10, 4, 12, 12, 16]
Approach:
Take left and right pointer. do swappings

TIME: O(N)
'''



def seperate_even_odd(arr):
    n = len(arr) - 1
    l, r = 0, n
    while l <= r:
        if arr[l] % 2 == 1:
            l = l + 1
        if arr[r] % 2 == 0:
            r = r - 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l = l + 1
            r = r - 1
    return arr



arr = [12,15,10,8,7,10,18,5,4,3,12,16]
print(seperate_even_odd(arr))
