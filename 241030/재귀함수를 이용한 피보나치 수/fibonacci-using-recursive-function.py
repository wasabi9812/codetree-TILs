import sys

N = int(sys.stdin.readline())

def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return recur(n-1)+recur(n-2)

print(recur(N))