import sys
matrix = []
for i in range(2):
    N = list(map(int, sys.stdin.readline().split()))
    matrix.append(N)

firstresult = []

for i in range(2):
    temp1 = 0
    for j in range(4):
        temp1 += matrix[i][j]

    firstresult.append(temp1/4)

secondresult = []

for i in range(4):
    temp2 = 0
    for j in range(2):
        temp2 += matrix[j][i]
    secondresult.append(temp2/2)

allresult = []
temp3 = 0

for i in range(2):
    for j in range(4):
        temp3 +=matrix[i][j]

allresult.append(temp3/8)

print(*[f"{x:.1f}" for x in firstresult])
print(*[f"{x:.1f}" for x in secondresult])
print(*[f"{x:.1f}" for x in allresult])