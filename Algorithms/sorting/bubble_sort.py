# BUBBLE SORT
'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
'''

arr = [5, 6, 1, 7, 0, 4, 12, 10, 9]
n = len(arr)


# PASS
def bubble_search(arr,n):
    for j in range(n):
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
        if swapped == False:
            return arr

print(bubble_search(arr,n))