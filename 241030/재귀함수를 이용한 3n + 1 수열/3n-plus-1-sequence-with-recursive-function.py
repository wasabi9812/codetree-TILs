import sys

N = int(sys.stdin.readline())

def f(n,c):
    if n==1:
        return c
    if n%2==0:
        return f(n//2,c+1)
    else:
        return f(3*n+1,c+1)

print(f(N,0))