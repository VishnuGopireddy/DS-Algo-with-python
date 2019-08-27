# Check for balanced paranthesis using stack

'''
Ex:
1. {{}[]()[[]]} ----> Balanced
2. [[[[{{{}}}]]]][ --> Not Balanced
'''


from stacks.stack import Stacks

s = Stacks()

def is_match(p1,p2):
    if p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '(' and p2 == ')':
        return True
    else:
        return False

def bal_paranthesis(exp):
    for i in exp:
        if i in '{[(':
            s.push(i)
        elif i in '])}':
            if is_match(s.pop(),i) != True:
                return False
        else:
            pass

    if s.isempty():
        return True
    else:
        return False

#expression = input("Enter an Expression")
exp = '{[[()]]}'
print(exp)
print(bal_paranthesis(exp))



