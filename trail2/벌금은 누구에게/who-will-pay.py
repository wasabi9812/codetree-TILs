N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
nlist = [0]*(N+100)
ans = -1
for i in range(M):
    temp = student[i]
    nlist[temp]+=1
    if nlist[temp] == K:
        ans = temp
        break
print(ans)