import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
sums = 0
for i in range(N):
    sums += abs(nums[i])

print(sums)