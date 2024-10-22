import sys

N = int(sys.stdin.readline())

def recur(n):
    if(n == 0):
        print(" ")
        return
    print(n, end=' ')
    recur(n-1)
    print(n, end=' ')

recur(N)