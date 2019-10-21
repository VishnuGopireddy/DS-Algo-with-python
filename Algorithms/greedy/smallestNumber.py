#https://practice.geeksforgeeks.org/problems/smallest-number/0
'''
The task is to find the smallest number with given sum of digits as s and number of digits as d.

Expected Time Complexity: O(d)

This can be solved using greedy algorithm
'''
kases = 3
nums = [[9,2],[20,3],[63,3]]


for i in nums:
    tot_sum = i[0]
    digits = i[1]
    if tot_sum > digits * 9:
        # sum exceeds
        print('-1')
    else:
        dig = []
        while digits > 0:
            digits = digits - 1
            rem = tot_sum - (digits * 9)
            if rem <= 0:
                dig.append(1)
                tot_sum = tot_sum - 1
            else:
                dig.append(rem)
                tot_sum = tot_sum - rem
        print(dig)