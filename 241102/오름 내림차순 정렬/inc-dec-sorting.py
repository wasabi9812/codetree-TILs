import sys

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

for i in range(N-1):
    for j in range(N-1, i, -1):
        if data[j-1]>data[j]:
            data[j-1], data[j] = data[j], data[j-1]

for i in range(N):
    print(data[i], end=' ')
print()
for i in range(N-1,-1,-1):
    print(data[i], end=' ')