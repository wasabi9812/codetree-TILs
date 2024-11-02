import sys

data = list(map(str ,sys.stdin.readline().strip()))

for i in range(len(data)-1):
    for j in range(len(data)-1,i,-1):
        if data[j-1]>data[j]:
            data[j-1],data[j] = data[j], data[j-1]

for i in range(len(data)):
    print(data[i],end ='')