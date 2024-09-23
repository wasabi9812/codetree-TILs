import sys

binarycode = sys.stdin.readline().strip()
sums = 0
for i in range(len(binarycode)):
    if int(binarycode[i])==1:
        sums+=2**(len(binarycode)-1-i)
    else:
        continue

print(sums)