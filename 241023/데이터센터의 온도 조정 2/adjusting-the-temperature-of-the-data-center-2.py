import sys

N,C,G,H = map(int,sys.stdin.readline().split())
templist = []
for i in range(N):
    templist.append(list(map(int,sys.stdin.readline().split())))

max_temp = 0



for i in range(len(templist)):
    if max_temp<templist[i][1]:
        max_temp = templist[i][1]

def tempfunc(m,ta,tb):
    if m<ta:
        return C
    elif ta<= m <=tb:
        return G
    else:
        return H

for i in range(max_temp+1):
    tempsum = 0
    for j in range(len(templist)):
        ta, tb = templist[j][0], templist[j][1]
        tempsum += tempfunc(i,ta,tb)
    if tempsum>max_temp:
        max_temp = tempsum

print(max_temp)