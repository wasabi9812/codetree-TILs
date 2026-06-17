n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
class Num:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx

arr = []

for i in range(n):
    arr.append(Num(sequence[i], i))

arr.sort(key=lambda x: x.value)

result = [0] * n

for i in range(n):
    original_idx = arr[i].idx
    result[original_idx] = i + 1

print(*result)