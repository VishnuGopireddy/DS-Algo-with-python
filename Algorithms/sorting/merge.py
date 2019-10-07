'''
soves with divide and conquer.

BEST CASE: O(nlogn)
AVG CASE: O(nlogn)
WORST CASE: O(nlogn)

SPACE : O(n)

'''

arr = [5, 6, 1, 7, 0, 4, 12, 10, 9]
n = len(arr)
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergesort(left_arr)
        mergesort(right_arr)

        i, j, k = 0, 0, 0

        l1, l2 = len(left_arr), len(right_arr)
        while i < l1 and j < l2:
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1
        while i < l1:
            arr[k] = left_arr[i]
            i = i + 1
            k = k + 1
        while j < l2:
            arr[k] = right_arr[j]
            j = j + 1
            k = k +1

mergesort(arr)
print(arr)