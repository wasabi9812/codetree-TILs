import sys

N = int(sys.stdin.readline())

q = str(N)
end = len(q)

def recur(n, i):
    if n == end:
        return 0
    m = int(q[i])
    return m * m + recur(n + 1, i + 1)

ans = recur(0, 0)
print(ans)