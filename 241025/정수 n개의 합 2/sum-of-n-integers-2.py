import sys

N, M = map(int, sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))

prefix_list = [0] * (len(data) + 1) 
prefix_sum = 0
for i in range(len(data)):
    prefix_sum = prefix_sum + data[i]
    prefix_list[i] = prefix_sum

max_val = -float('inf')  # 최댓값 초기화

# 길이가 M인 모든 구간 합 중 최댓값 찾기
for i in range(len(data) - M + 1):
    # 구간 합 계산 (i부터 i+M-1까지의 합)
    wanted_val = prefix_list[i + M] - prefix_list[i]
    if wanted_val > max_val:
        max_val = wanted_val

print(max_val)