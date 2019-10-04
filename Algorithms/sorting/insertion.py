'''
INSERTION SORT: Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Worst case: O(n^2)
Best case: O(n)
'''

arr = [5, 6, 1, 7, 0, 4, 12, 10, 9]

n = len(arr)

def insersion(arr):
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while key < arr[j]  and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

insersion(arr)
print(arr)