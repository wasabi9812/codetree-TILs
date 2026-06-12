import sys
N = int(sys.stdin.readline())

temp = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(len(temp)-1,-1,-1):
    if temp[i]%2 ==0:
        result.append(temp[i])

print(*result)

