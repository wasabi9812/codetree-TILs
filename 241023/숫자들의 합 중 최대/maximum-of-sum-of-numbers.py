import sys

N, M = map(int,sys.stdin.readline().split())

d1= list(str(N))
d2= list(str(M))
valsum1 =0
valsum2 =0
for i in range(len(d1)):
    valsum1 += int(d1[i])

for i in range(len(d2)):
    valsum2 += int(d2[i])

if valsum1>valsum2:
    print (valsum1)
elif valsum1<valsum2:
    print (valsum2)