n, m = map(int,input().split())

nlista = [0]*1000001
nlistb = [0]*1000001

pointa = 1
for i in range(n):
    v , t = map(int,input().split())
    for _ in range(t):
        nlista[pointa] = nlista[pointa-1]+v
        pointa+=1

pointb = 1
for i in range(m):
    v , t = map(int,input().split())
    for _ in range(t):
        nlistb[pointb] = nlistb[pointb-1]+v
        pointb+=1

leader = 0
ans = 0
for i in range(pointa):
    if nlista[i] > nlistb[i]:
        if leader ==2:
            ans+=1
        leader =1

    elif nlista[i] < nlistb[i]:
        if leader ==1:
            ans+=1
        leader=2

print(ans)
