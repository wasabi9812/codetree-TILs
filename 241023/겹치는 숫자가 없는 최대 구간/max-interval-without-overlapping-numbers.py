import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.insert(0,0)
ans = 0
count_arr = [0,0,0,0]
j=0
for i in range(1,N+1):
    while j+1 <=N and count_arr[arr[j+1]] !=1:
        count_arr[arr[j+1]]+=1
        j+=1
    
    ans = max(ans, j-i+1)
    count_arr[arr[i]]-=1 #i가 증가할거니까
print(ans)