n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
nlist = [0] * 2001
offset = 1000
wwr = offset

for i in range(n):
    distance = x[i]
    d = dir[i]

    if d == 'R':
        for j in range(wwr, wwr + distance):
            nlist[j] += 1

        wwr += distance

    else:
        for j in range(wwr - distance, wwr):
            nlist[j] += 1

        wwr -= distance

answer = 0

for count in nlist:
    if count >= 2:
        answer += 1

print(answer)