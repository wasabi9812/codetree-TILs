n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

snum = len(t)
st = list(t)
temp = []
for i in range(n):
    if len(str[i])<snum:
        continue
    checksame = True
    for j in range(snum):
        if str[i][j] != st[j]:
            checksame = False
            break
    if checksame:
        temp.append(str[i])

temp.sort()

print(temp[k-1])