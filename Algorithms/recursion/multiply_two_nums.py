'''
x = 5
y = 3
(5,3)
5 + (5,2)
5 + (5,1)
5 + (5,0)
'''
x = 5
y = 3
def multiply(x,y):
    if y == 0:
        return 0
    else:
        return 5 + multiply(5,y-1)

print(multiply(x,y))