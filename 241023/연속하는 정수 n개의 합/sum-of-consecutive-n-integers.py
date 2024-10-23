import sys

N, M = map(int, sys.stdin.readline().split())
arr =[0] +list(map(int,sys.stdin.readline().split()))

val_sum = 0
result = 0
j =0
for i in range(1,N+1):
    while j<N and val_sum < M:
        j+=1
        val_sum+=arr[j]
    # 해당값이 M과같다면
    if val_sum == M:
        result +=1 
    # i가 움직이니 그거 빼줌
    val_sum -= arr[i]

print(result)