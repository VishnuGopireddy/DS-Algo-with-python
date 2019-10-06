'''
INSERTION SORT
'''
arr = [170, 45, 75, 90, 802, 24, 2, 66]

n = len(arr)

def insertion(arr,n):
    for i in range(1,n):
        j = i - 1
        while arr[i] < arr[j] and j >= 0:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j = j - 1
        arr[i],arr[j] = arr[j],arr[i]

insertion(arr)
print(arr)