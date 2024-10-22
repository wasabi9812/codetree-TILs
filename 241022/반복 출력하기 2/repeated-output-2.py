import sys

N = int(sys.stdin.readline())

def recur(n):
    if n == 0:
        return
    recur(n - 1)
    print("HelloWorld")

recur(N)