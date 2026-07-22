n = int(input())

point = []

nlist = [[0]*250 for _ in range(250)]

offset = 100

for i in range(n):
    a,b = map(int,input().split())
    a = a+offset
    b = b+offset
    for j in range(b,b+8):
        for k in range(a,a+8):
            nlist[j][k] =1

cnt =0
for i in range(250):
    for j in range(250):
        if nlist[i][j] ==1:
            cnt +=1
print(cnt)