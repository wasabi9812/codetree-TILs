import sys

N = int(sys.stdin.readline())
cnt = 0
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    sumnum = 0
    for i in range(len(temp)):
        sumnum += temp[i]
    if sumnum // len(temp)>= 60:
        print("pass")
        cnt +=1
    else:
        print("fail")


print(cnt)