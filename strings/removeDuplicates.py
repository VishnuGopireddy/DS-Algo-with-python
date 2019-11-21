#remove duplicates from a given string
'''
Example: 'abbcccddddeeeee'
Output: 'abcde'

Approach 1:
1. create a new array to store output.
2. add new chars to yhe output after comparing with previously inserted values

Time: O(n^2)
Space: O(N)

Approach 2:
1. create a new array to store output and maintain a hash table to store occurances.
2. add new chars to the output after comparing with previously inserted values

Time: O(n^2)
Space: O(N)


'''