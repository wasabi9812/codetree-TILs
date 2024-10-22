import sys, math

n, s = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)

minimal_length = float('inf')
sum_val = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and sum_val < s:
        j += 1
        sum_val += arr[j]

    # sum_val이 s 이상이면 minimal_length 갱신
    if sum_val >= s:
        minimal_length = min(minimal_length, j - i + 1)

    # 다음 구간으로 넘어가기 전에 현재 구간의 시작점 i를 제외
    sum_val -= arr[i]

if minimal_length == float('inf'):
    print(-1)
else:
    print(minimal_length)