n = int(input())
arr = list(map(int, input().split()))

arrtemp = []
result = []

for i in range(n):
    arrtemp.append(arr[i])

    if i % 2 == 0:
        arrtemp.sort()
        result.append(arrtemp[len(arrtemp)//2])

print(*result)

