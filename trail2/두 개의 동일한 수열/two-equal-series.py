n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

answer = True

for i in range(len(A)):
    if A[i] != B[i]:
        answer = False
        break

if answer == True:
    print("Yes")
else:
    print("No")