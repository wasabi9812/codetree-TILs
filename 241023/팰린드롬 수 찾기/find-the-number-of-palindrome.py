import sys

N, M = map(int,sys.stdin.readline().split())

palnum = 0

def is_palindrome(n):
    n = str(n)
    nlen = len(n)
    for i in range(nlen//2):
        if n[i] != n[nlen-i-1]:
            return False
    return True

for i in range(N,M+1):
    if is_palindrome(i) == True:
        palnum+=1

print(palnum)