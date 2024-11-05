import sys

N,M = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))

def sortnum(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1,i,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]

sortnum(data)

print(data[M-1])