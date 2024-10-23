import sys

s = []
data = list(map(str, sys.stdin.readline().strip()))  # 입력을 문자 하나하나로 받음

for char in data:
    if char == "(":
        s.append("(")  # 여는 괄호를 스택에 추가
    elif char == ")":
        if s:  # 스택에 여는 괄호가 있으면 pop
            s.pop()
        else:  # 스택이 비어 있는데 닫는 괄호가 나왔다면 잘못된 괄호
            print("No")
            exit()

# 모든 괄호가 짝이 맞는지 확인
if not s:
    print("Yes")
else:
    print("No")