#RBR Interv prep
#Find the longest increasing subsequence
'''
Example: [2,10,13,15,3,11,12]
longestincreasing subsequences are: [2,3,11,12], [2,10,13,15], [10,13,15]
Approach1:
    arr = [2,10,13,15,3,11,12]
    arr1 = [2,3,10,11,12,13,15] ==> sorted array
    Perform Longest common subsequence on arr, arr1
    TIME and Space = O(n^2)
Approach 2: Bruteforce
    Generate all possible subarrays (2^n).
    Check weather the elements in the subarray are in increasing order or not.
    TIME: O(2^n * n)
Approach 3: Dynamic Programing
    TIME: O(n^2)
    SPACE : O(n)
'''


def longest_increasing_subseq(arr):
    '''
    Returns longest increasing sub-sequence from a given array
    :param str: string
    :return: Integer, wit longest increasing sub-sequence
    '''


    n = len(arr)
    sol = [1 for i in range(n)]
    for i in range(n):
        print(sol)
        if i == 0:
            sol[0] = 1
        else:
            for j in range(0,i):
                max_sub = sol[i]
                if arr[i] > arr[j]:
                    temp = sol[j] + 1
                    if temp > max_sub:
                        sol[i] = temp
    return max(sol)



#arr = [2,10,13,15,3,11,12]
arr = [2,3,1,5,12,10,11]
print(longest_increasing_subseq(arr))

