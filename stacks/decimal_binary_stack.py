#Convert decimal number into a binary number using stack


from stacks.stack import Stacks

num = int(input("Enter a number to convert into binary:"))

s = Stacks()

#divide number with 2 and append the remainder to the stack till the num becomes zero

while num > 0:
    s.push(num % 2)
    num = num //2

print("Binary of",num,"is",end='-->')
print(s.get_items())

