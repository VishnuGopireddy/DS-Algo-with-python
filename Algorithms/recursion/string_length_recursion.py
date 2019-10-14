#calculate lenth of the string
st = 'Welcome to the world'
#predefined function
print(len(st))
#Iterative
count = 0
for i in st:
    count +=1
print(count)

#recursive





def word_count(st):
    if st:
        return 1 + word_count(st[1:])
    else:
        return 0

print(word_count(st))