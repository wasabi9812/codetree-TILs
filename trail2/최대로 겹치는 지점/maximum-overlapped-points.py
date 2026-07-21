n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

nlist = [0]*201

for i in range(n):
    a = segments[i][0]
    b = segments[i][1]
    for j in range(a,b+1):
        nlist[j]+=1

print(max(nlist))