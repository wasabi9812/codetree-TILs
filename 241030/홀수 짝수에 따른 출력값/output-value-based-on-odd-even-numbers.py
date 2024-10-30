import sys

N = int(sys.stdin.readline())

def odd(n):
    if n==1:
        return 1
    return n+odd(n-2)

def even(n):
    if n==2:
        return 2
    return n+even(n-2)

if N%2==0:
    print(even(N))
else:
    print(odd(N))