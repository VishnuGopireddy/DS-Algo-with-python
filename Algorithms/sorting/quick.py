'''
Quick sort: DIVIDE and CONQURE
i,j at start and pivot at end

BEST CASE: O(nlogn)
AVG CASE: O(nlogn)
WORST CASE: O(n^2)
'''
arr = [7,2,1,6,8,5,3,4]
n = len(arr)

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = pivot,arr[i+1]

    return i + 1
quicksort(arr,0,n-1)
print(arr)