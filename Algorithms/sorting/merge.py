arr = [5, 6, 1, 7, 0, 4, 12, 10, 9]
n = len(arr)
def mergesort(arr,low=0,high=n):
    if low < high
        mid = (low + high) // 2
        mergesort(low, mid)
        mergesort(mid, high)

def merge(arr1,arr2):
    i, j = 0, 0
    new_arr = []
    l1,l2 = len(arr1), len(arr2)
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i = i + 1
        else:
            new_arr.append(arr2[j])
            j = j + 1
    while i < l1:
        new_arr.append(arr1[i])
        i = i + 1
    while j < l2:
        new_arr.append(arr2[j])
        j = j + 1
    return new_arr

print(merge(arr1,arr2))