#RBR Interview Prep
#Print all the possible permutations of a given string
'''
This problem can be solved using Backtacking
Example: BAT :
combinations are [ABT, ATB, BTA, BAT, TAB, TBA] = n!
Time Complexity = O(n (n!))
Space: O(n)
'''

name = 'vishnu'

def permutations(s):
    n = len(s)

    if n == 0:
        return []
    if n == 1:
        return[s]
    l = []

    for i in range(n):
        m = s[i]
        rem_list = s[:i] + s[i+1:]
        for p in permutations(rem_list):
            l.append([m] + p)
    return l

for p in permutations(name):
    print(p)
