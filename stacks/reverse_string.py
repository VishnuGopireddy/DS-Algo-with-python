'''
Perform reversing of a string using stack
'''

from stacks import stack
s = stack.Stacks()

string = input("Enter a string to reverse")
print(string)
for i in string:
    s.push(i)

while s.isempty() != True:
    print(s.pop(),end='')