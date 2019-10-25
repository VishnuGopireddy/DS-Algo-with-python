'''
Fibonacci series
0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55 +
'''

def fibonacci(n):
    f = [0 for i in range(n+2)]
    f[0], f[1] = 0, 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fibonacci(15))




