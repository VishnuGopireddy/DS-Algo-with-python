#code
#https://practice.geeksforgeeks.org/problems/ishaan-loves-chocolates/0
kases = int(input())

for kase in range(kases):
    n = int(input())
    tasty = list(map(int,input().split(' ')))
    print(min(tasty))
