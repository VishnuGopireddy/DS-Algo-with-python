#BINARY SEARCH
my_list = [1,4,8,9,12,16,19,25,29,35]

ele = 1
n = len(my_list)
def binarysearch(my_list,ele,low=0,high=n):
    if high >= low:
        mid = low + (high-1) // 2
        if my_list[mid] == ele:
            return mid
        elif ele < my_list[mid]:
            return binarysearch(my_list,ele,low=0,high=mid-1)
        else:


            return binarysearch(my_list, ele, low=mid+1, high=high)
    else:
        return False

mid = binarysearch(my_list,ele,0,n-1)
if mid:
    print(ele,'is found at position',mid)
else:
    print('Element fot found')