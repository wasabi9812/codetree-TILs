n, k, p, t = map(int,input().split())

info = []

for i in range(t):
    a,b,c = map(int,input().split())
    info.append([a,b-1,c-1])
#a =time from b to c
info.sort()


devlist = [0]*n
conlist = [0]*n
conlist[p-1] = 1

for time, start, end in info:
    # 이번 악수 전에 이미 감염돼 있었는지 저장
    start_infected = conlist[start]
    end_infected = conlist[end]

    if start_infected and devlist[start] < k:
        devlist[start] += 1
        conlist[end] = 1

    if end_infected and devlist[end] < k:
        devlist[end] += 1
        conlist[start] = 1

print(''.join(map(str, conlist)))
