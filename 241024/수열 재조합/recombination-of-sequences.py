import sys

N = int(sys.stdin.readline())
stack = []
last = 0
for i in range(1,N+1):
    m = int(sys.stdin.readline())
    if last<m:
        for j in range(1,m+1):
            stack.append(j)
            print("+")
        last = m
    if stack:
        top_value = stack[-1]
        if top_value == m:
            stack.pop()
            print("-")