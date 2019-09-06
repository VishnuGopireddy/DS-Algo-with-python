#josephus problem
from circular_list import circular

c = circular.circular_list()
n = 7
k = 3

for i in range(1,n+1):
    c.append(i)

c.print_list()
