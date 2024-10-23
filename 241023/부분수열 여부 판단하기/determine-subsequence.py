import sys

def is_subsequence(A,B,n,m):
    i = 1
    for j in range(1, m+1):
        while i<=n and A[i] != B[j]:
            i += 1
        
        if i == n+1:
            return False
        else:
            i += 1
    return True

N, M = map(int,sys.stdin.readline().split())

A =[0]+list(map(int,sys.stdin.readline().split()))
B =[0]+list(map(int,sys.stdin.readline().split()))

if is_subsequence(A,B,N,M):
    print("Yes")
else:
    print("No")