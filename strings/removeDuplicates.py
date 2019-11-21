#remove duplicates from a given string
'''
Example: 'abbcccddddeeeee'
Output: 'abcde'

Approach 1:
1. create a new array to store output.
2. add new chars to the output after comparing with previously inserted values
Time: O(n^2)
Space: O(N)

Approach 2:
1. create a new array to store output and maintain a hash table to store occurances.
2. add new chars to the output after checking with hash table
Time: O(n)
Space: O(N) + O(k)   k = #symbols

Approach 3(inplace of approach 2):
Time: O(n)
Space: O(1) + O(k)
'''


def removeDuplicates(st):
    '''
    Remove duplicate characters from a given string (for simplicitywe consider only small case alphabets only)
    :param st: string
    :return: string after removing dplicates
    '''

    dict = {chr(i):0 for i in range(ord('a'), ord('z')+1)}
    out = ''
    for i in st:
        if dict[i] == 0:
            out = out + i
            dict[i] = 1
    return out

s = 'abbcccdddd'
print(removeDuplicates(s))
