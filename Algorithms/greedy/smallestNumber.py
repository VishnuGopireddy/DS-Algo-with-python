#https://practice.geeksforgeeks.org/problems/smallest-number/0

kases = 3
nums = [[9,2],[20,3],[63,3]]

for i in nums:
    sum = i[0]
    digits = i[1]
    if sum > digits * 9:
        # sum exceeds
        print('-1')
    else:
        dig = [0 for i in range(digits)]
        print(dig)