n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
rev = list(reversed(nums))

print(*nums)
print(*rev)