# Problem:
# Count number of zeros in a factorial of large number

# Sol:
#       Take all the multiplications in an array.
# Ex:
#   6! = [7,2,0]

def get_array(num):
    """
    :param num:
    :return:
    """
    arr = []
    while num >0:
        arr.append(num % 10)
        num = num //10
    return arr

def multiply(arr,num):
    carry = 0
    p = []
    for i in arr:
        prod = (i * num) + carry
        carry = prod//10
        p.append(prod%10)
    if carry > 9:
        while carry >= 1:
            p.append(carry % 10)
            carry = carry // 10
    else:
        p.append(carry)

    return p

num = int(input("Enter a number"))
arr = get_array(num)

while num > 1:
    num = num - 1
    arr = multiply(arr,num)

res = arr[::-1]
res = map(str,res)
s = ''.join(res).lstrip('0')
print(s.count('0'))