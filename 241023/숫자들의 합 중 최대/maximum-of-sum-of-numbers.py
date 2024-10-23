import sys

N, M = tuple(map(int,sys.stdin.readline().split()))

def digit_sum(n):
    if n<10:
        return n
    else:
        return digit_sum(n//10)+(n%10)


ans = 0

for i in range(N, M+1):
    ans = max(ans, digit_sum(i))

print(ans)