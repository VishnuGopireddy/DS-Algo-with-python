#RBR Interview Prep
#Find Max sum sub-array
'''
Ex: [10, -5, -3, 4, 2, 12, -8, -12, 19]

Max sum is 20([10, -5, -3, 4, 2, 12])

Kadan's Algo:(Assumption atleast one element is positive in the array)
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far

Time Complexity: O(n)
'''


def kadane(arr):
    n = len(arr)
    index, max_sum, curr_sum = -1, 0, 0
    for i in range(n):
        curr_sum = curr_sum + arr[i]
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
            index = i

    curr_sum = 0
    print(max_sum, index)
    for start in range(index, -1, -1):
        curr_sum = curr_sum + arr[start]
        if curr_sum == max_sum:
            if start == index:
                return arr[index:index+1]
            return arr[start:index]


arr = [-10, -5, -3, -4, -2, 12, -8, -12, -19]
print(kadane(arr))