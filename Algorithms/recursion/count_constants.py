#COUNT CONSTANTS in a string
#we consider ' ' also as a consonent

#recursion

st = 'welcome words'

def count_cons(st):
    if st:
        if st[0] not in 'aeiou':
            return 1 + count_cons(st[1:])
        else:
            return 0 + count_cons(st[1:])
    else:
        return 0

print(count_cons(st))