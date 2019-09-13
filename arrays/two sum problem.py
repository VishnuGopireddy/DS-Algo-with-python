# Given a sorted array find two indices of the elements that add up to the given number
# Under a constraint that no two elemets are repeating

#APPROACH 1: O(n^2) BruteForce - Try with all possible combinations

#APPROACH 2: O(n)

def two_sum(arr,len,s):
    start = 0
    end = len - 1
    while arr[start] + arr[end] != s and start < end:
        if arr[start] + arr[end] < s:
            start = start + 1
        else:
            end = end - 1

    if arr[start] + arr[end] == s:
        return start,end, arr[start] + arr[end]
    else:
        return None

arr = [-2,1,2,4,7,11]
len = 6
s = 16

print(two_sum(arr,len,s))