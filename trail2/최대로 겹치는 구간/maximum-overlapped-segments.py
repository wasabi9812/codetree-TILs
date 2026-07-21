n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
nlist = [0]*201
for i in range(n):
    a = segments[i][0] + 100
    b = segments[i][1] + 100
    for j in range(a,b):
        nlist[j]+=1

result = max(nlist)
print(result)