import sys

n, s = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)

minimal_length = float('inf')
sum_val = 0
j = 0
for i in range(1, n+1):
    while j+1 <= n and sum_val <s:
        sum_val += arr[j+1]
        j += 1

        if sum_val >= s:
            minimal_length = min(minimal_length, abs(j-i+1))

    sum_val -= arr[i]

print(minimal_length)