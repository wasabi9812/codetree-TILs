import sys

N = int(sys.stdin.readline().strip())

# 필요한 초기값만 설정
dp = [0] * (N + 5)
dp[2], dp[3] = 1, 1

def climb(n):
    # 4번째 계단부터 n번째 계단까지 dp 배열 채우기
    for i in range(4, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 3])%10007
    return dp[n]

print(climb(N))