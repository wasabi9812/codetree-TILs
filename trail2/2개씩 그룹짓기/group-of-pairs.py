n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

temp = []
nums.sort()
for i in range(n):
    sumnum = nums[i] + nums[2*n-i-1]
    temp.append(sumnum)

print(max(temp))