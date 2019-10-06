'''
count sort:

Example: consider array in range (0,9)
'''

arr = [1, 4, 1, 2, 7, 5, 2]
low = 0
high = 9
count = [0 for i in range(low,high+1)]

for i in arr:
    count[i] = count[i] + 1
print(count)

print(sort)