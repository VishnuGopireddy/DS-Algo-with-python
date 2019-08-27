'''
Perform reversing of a string using stack
'''

from stacks import stack
s = stack.Stacks()
string = 'vishnu'

for i in string:
    s.push(i)

print(s.get_items())
