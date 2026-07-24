n, m = map(int, input().split())

nlista = [0] * 2000000
nlistb = [0] * 2000000

pa = 1
for i in range(n):
    t, dir = input().split()
    t = int(t)

    for _ in range(t):
        if dir == 'R':
            temp = 1
        else:
            temp = -1

        nlista[pa] = nlista[pa - 1] + temp
        pa += 1


pb = 1
for i in range(m):
    t, dir = input().split()
    t = int(t)

    for _ in range(t):
        if dir == 'R':
            temp = 1
        else:
            temp = -1

        nlistb[pb] = nlistb[pb - 1] + temp
        pb += 1


cnt = 0

ltime = max(pa,pb)

for i in range(pa, ltime):
    nlista[i] = nlista[i-1]
for i in range(pb, ltime):
    nlistb[i] = nlistb[i-1]
    
for i in range(ltime):
    if nlista[i] == nlistb[i]:
        if nlista[i - 1] == nlistb[i - 1]:
            continue
        cnt += 1

print(cnt)