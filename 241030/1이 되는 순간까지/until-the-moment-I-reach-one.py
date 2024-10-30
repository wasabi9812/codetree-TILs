import sys

N = int(sys.stdin.readline())
cnt = 0
def recur(n):
    global cnt
    if n == 1:
        return
    if n %2 ==0:
        n=n//2
        cnt+=1
    else:
        n=n//3
        cnt+=1
    return recur(n)

recur(N)
print(cnt)