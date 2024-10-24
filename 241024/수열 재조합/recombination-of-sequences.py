import sys

N = int(sys.stdin.readline())
stack = []
last = 0
output = []
possible = True

for i in range(N):
    m = int(sys.stdin.readline())
    
    # 스택에 더 큰 값 추가
    if last < m:
        for j in range(last + 1, m + 1):
            stack.append(j)
            output.append("+")
        last = m
    
    # 스택 최상단이 m과 같다면 pop
    if stack:
        top_value = stack[-1]
        if top_value == m:
            stack.pop()
            output.append("-")
        else:
            # 스택의 최상단 값이 현재 필요한 값과 다르다면 수열을 만들 수 없음
            possible = False
            break

if possible:
    for op in output:
        print(op)
else:
    print("NO")