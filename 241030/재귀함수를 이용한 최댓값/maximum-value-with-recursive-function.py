import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
max_val = 0

def f(m,i,d):
    if i == len(d)-1:
        if d[i] >=m:
            m = d[i]
            return m
        else:
            return m
    if d[i] >=m:
        m = d[i]
    return f(m,i+1,d)

print(f(0,0,data))