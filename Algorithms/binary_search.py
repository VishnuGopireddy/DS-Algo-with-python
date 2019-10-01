#BINARY SEARCH

my_list = [1,4,8,9,12,16,19,25,29,35]

ele = 25
n = len(my_list)
def binarysearch(my_list,ele,low=0,high=n):
    mid = (low + high) // 2
    if low < high:
        if my_list[mid] == ele:
            return mid
        elif ele < my_list[mid]:
            return binarysearch(my_list,ele,low=0,high=mid)
        else:
            return binarysearch(my_list, ele, low=mid, high=high)
    else:
        return False
if binarysearch(my_list,ele,0,n):
    print(ele,'is found at position',mid)
else:
    print('Element fot found')