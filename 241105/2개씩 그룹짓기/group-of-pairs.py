import sys

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

def sortnum(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1, i , -1):
            if arr[j-1]>arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

sortnum(data)
if N ==1:
    print(data[1])
else:
    sum_val = 0
    for i in range(N):
        sum_val+=data[N-i]

    print(sum_val)