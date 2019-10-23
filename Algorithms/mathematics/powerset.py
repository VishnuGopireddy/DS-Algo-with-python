# https://www.geeksforgeeks.org/power-set/
'''
Power set P(S) of a set S is the set of all subsets of S.
For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.

If S has n elements in it then P(s) will have 2^n elements
'''


def powerset(set):
    set_size = len(set)
    power_set_size = 2 ** set_size
    for counter in range(0, power_set_size):
        for j in range(0, set_size):
            if (counter & (1 << j)) > 0:
                print(set[j], end='')
        print(' ')

set = ['a', 'b', 'c']
powerset(set)
