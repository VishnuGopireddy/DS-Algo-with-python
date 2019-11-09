#https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0/?ref=self
'''
There are given N ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.
'''

def min_cost_ropes(ropes,n):
    cost = 0
    while n > 1:
        r1 = min(ropes)
        ropes.remove(r1)
        r2 = min(ropes)
        ropes.remove(r2)
        ropes.append(r1 + r2)
        cost = cost + r1 + r2
        n = n -1
    return cost


kases = int(input())
for kase in range(kases):
    n = int(input())
    ropes = list(map(int,input().split()))
    print(min_cost_ropes(ropes,n))