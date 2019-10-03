#FIND OUT ALL THE UPPER CASE LETTERS IN A STRING
st = 'I am Vishnu from HYD'

for i in st:
    if i.isupper():
        print(i)
    else:
        pass

def upper_case(st):
    if st:
        if st[0].isupper():
            print(st[0])
        return upper_case(st[1:])


print('-'*100)
upper_case(st)