import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

data.sort()

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

temp =data[0]

for i in range(N):
    temp = lcm(data[i],temp)

print(int(temp))