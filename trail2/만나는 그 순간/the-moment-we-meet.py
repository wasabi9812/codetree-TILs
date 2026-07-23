n , m = map(int,input().split())

nlista = [0]*1000000
nlistb = [0]*1000000

#a
ta = 1
for i in range(n):
    dir, t = tuple(input().split())
    for _ in range(int(t)):
        if dir  == 'R':
            temp = 1
        else:
            temp = -1
        nlista[ta] = nlista[ta-1] + temp
        ta+=1

#b
tb =1
for i in range(m):
    dir, t = tuple(input().split())
    for _ in range(int(t)):
        if dir  == 'R':
            temp = 1
        else:
            temp = -1
        nlistb[tb] = nlistb[tb-1] + temp
        tb+=1

result = -1
for i in range(1, ta):
    if nlista[i] == nlistb[i]:
        result = i
        break
print(result)