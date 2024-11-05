import sys

N = int(sys.stdin.readline())

def strsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1,i,-1):
            if arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            

data = []
for i in range(N):
    data.append(sys.stdin.readline().strip())

strsort(data)
for i in range(len(data)):
    print(data[i])