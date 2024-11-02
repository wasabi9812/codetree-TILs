import sys

N = int(sys.stdin.readline())

def recur(n):
    if n ==1:
        return 2
    if n ==2:
        return 4
    a = recur(n-1)*recur(n-2)
    b = a%100
    return b

print(recur(N))