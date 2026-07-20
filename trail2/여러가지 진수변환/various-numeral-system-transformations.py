N, B = map(int, input().split())

result = []

while N > 0:
    result.append(N % B)
    N //= B

for i in range(len(result) - 1, -1, -1):
    print(result[i], end="")