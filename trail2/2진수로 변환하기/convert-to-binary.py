n = int(input())

# Please write your code here.
nums = []
while True:
    if n<2:
        nums.append(n) 
        break
    nums.append(n%2)
    n = n//2

for i in range(len(nums)-1, -1, -1):
    print(nums[i], end="")
