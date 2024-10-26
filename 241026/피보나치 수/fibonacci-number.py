import sys

N = int(sys.stdin.readline())
def bottom_up(n):
    if n<1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[n])
bottom_up(N)