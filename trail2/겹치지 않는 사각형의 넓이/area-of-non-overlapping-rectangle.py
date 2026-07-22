x1, y1, x2, y2 = [], [], [], []
for _ in range(3):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

offset = 1000

nlist =[[0]*2001 for _ in range(2001)]

for i in range(2):
    xa = x1[i]+offset
    xb = x2[i]+offset
    ya = y1[i]+offset
    yb = y2[i]+offset

    for j in range(ya,yb):
        for k in range(xa, xb):
            nlist[j][k]+=1

    xa = x1[2]+offset
    xb = x2[2]+offset
    ya = y1[2]+offset
    yb = y2[2]+offset

for i in range(ya,yb):
    for j in range(xa,xb):
        nlist[i][j] = 3

cnt =0

for i in range(2):
    xa = x1[i]+offset
    xb = x2[i]+offset
    ya = y1[i]+offset
    yb = y2[i]+offset

    for j in range(ya,yb):
        for k in range(xa, xb):
            if nlist[j][k] ==3:
                continue
            else:
                cnt+=1
            
print(cnt)