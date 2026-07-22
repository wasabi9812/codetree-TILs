n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

offset = 100

point = 0

nlist= [[0]*201 for _ in range(201)]


for i in range(n):
    xa =x1[i]
    xb =x2[i]
    ya =y1[i]
    yb =y2[i]
    for j in range(xa,xb):
        for k in range(ya,yb):
            nlist[j][k] +=1

cnt = 0
for j in range(201):
    for k in range(201):
        if nlist[j][k] > 0:
            cnt+=1

print(cnt)