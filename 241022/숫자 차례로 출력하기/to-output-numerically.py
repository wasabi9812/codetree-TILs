import sys

N = int(sys.stdin.readline())

def recur1(n):
    if(n == 0):
        print(" ")
        return
    print(n, end=' ')
    recur(n-1)

def recur2(n):
    if(n == 0):
        print(" ")
        return
    recur(n-1)
    print(n, end=' ')

recur1(N)
print()
recur2(N)