import sys

a,b,c =map(int,sys.stdin.readline().split())
M = a*b*c
def f(m):
    if m<10:
        return m
    return f(m//10)+(m%10)

print(f(M))