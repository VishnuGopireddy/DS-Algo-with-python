'''
count sort: Count the coccurances in a list, and convert occurances list to form a original list.

BEST CASE: O(n+k)
AVG CASE: O(n+k)
WORST CASE: O(n+k)
SPCAE : O(n+k)

Example: consider array in range (0,9)
'''


def counting(arr,low,high):
    '''
    Perform counting sort on the given array.
    :param arr: integers
    :param low: least number
    :param high: higher number
    :return: sorted array
    '''
    sort = []
    count = [0 for i in range(low,high+1)]
    for i in arr:
        count[i] = count[i] + 1


    j = 0
    for i in range(len(count)):
        while count[i] > 0:
            sort.append(i)
            count[i] -= 1
    return sort


arr = [1, 4, 1, 2, 7, 5, 2]
low = 0
high = 9

print(counting(arr, low, high))