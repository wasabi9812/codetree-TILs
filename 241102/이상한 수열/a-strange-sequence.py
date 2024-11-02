import sys

N = int(sys.stdin.readline())

def recur(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    n_nums = recur(n//3)+recur(n-1)
    return n_nums

print(recur(N))