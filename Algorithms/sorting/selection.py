'''
selection sort:
'''

arr = [5, 6, 1, 7, 0, 4, 12, 10, 9]
n = len(arr)

def selection(arr,n):
    for i in range(0,n):
        min = i
        for j in range(i,n):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]


selection(arr,n)
print(arr)