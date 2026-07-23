n = int(input())

nlist = []
for i in range(n):
    a =int(input())
    nlist.append(a)

result = 0
cnt = 0
for i in range(n):
    if i >=1 and nlist[i] == nlist[i-1]:
        cnt +=1
    else:
        cnt = 1
    result = max(result, cnt)
print(result)