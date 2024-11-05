import sys

N = int(sys.stdin.readline())
data1 = list(map(int,sys.stdin.readline().split()))
data2 = list(map(int,sys.stdin.readline().split()))

data1.sort()
data2.sort()

is_same =True

for i in range(N):
    if data1[i] != data2[i]:
        is_same = False

if is_same:
    print("Yes")
else:
    print("No")