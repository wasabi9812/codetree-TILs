import sys

s = []

cur = 0

data = list(map(str,sys.stdin.readline().split()))

for i in range(len(data)):
    if data[i] == "(":
        cur += 1
    else:
        cur -= 1

if cur ==0:
    print("Yes")
else:
    print("No")