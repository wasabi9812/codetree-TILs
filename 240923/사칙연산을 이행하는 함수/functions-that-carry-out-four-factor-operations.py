import sys

# 입력을 받아서 분리
x, a, y = sys.stdin.readline().split()
x = int(x)
y = int(y)

# 함수 정의를 위로 이동
def su(x, y):
    r = x + y
    return r

def minus(x, y):
    r = x - y
    return r

def multi(x, y):
    r = x * y
    return r

def div(x, y):
    r = x // y
    return r

# 연산 수행
if a == "+":
    result = su(x, y)
    print(f"{x} {a} {y} = {result}")
elif a == "-":
    result = minus(x, y)
    print(f"{x} {a} {y} = {result}")
elif a == "*":
    result = multi(x, y)
    print(f"{x} {a} {y} = {result}")
else:
    result = div(x, y)
    print(f"{x} {a} {y} = {result}")