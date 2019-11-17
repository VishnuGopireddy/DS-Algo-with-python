#RBR Interview Prep-
#Find the longest subsequence in an array, such that elements in subsequence are consecutive
'''
Find the longest subsequence in an array, such that elements in subsequence are consecutive
Example: [10,4,3,11,13,5,6,12,7]
possible subsequence are: 1. [4,3,5,6,7] and [10,11,13,12]
return longest subsequence

Approach 1: (Sort)
1. Sort out the array
2. Find the length of the longest sub-sequence
Time: O(nlogn) + O(n)

Approach2: (Hash Table)
1. Crate hash table with all the elements in the array and key is true.
2. For a given number in the hash table Check for the series and return longest sequence.
TIme: O(n) + O(2n) + On()
Space:  O(n)
'''
#approach 2


def longest_sub_consecutive_sequence(arr,n):
    dict = {i: False for i in arr}
    processed = 0
    longest = 0
    subseq = []
    while processed < n:
        for i in range(n):
            if dict[i] == False:
               subseq.append(arr[i])

            else:
                pass


arr = [10, 4, 3, 11, 13, 5, 6, 12, 7]
n = len(arr)