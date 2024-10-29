import sys

N = int(sys.stdin.readline())

def func(n):
    if n == N:
        return N
    
    return n+func(n+1)

print(func(0))