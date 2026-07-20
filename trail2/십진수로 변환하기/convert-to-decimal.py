binary = input()

# Please write your code here.

ba = list(binary)

num = 0
power = 0

for i in range(len(ba) - 1, -1, -1):
    num += int(ba[i]) * (2 ** power)
    power += 1

print(num)