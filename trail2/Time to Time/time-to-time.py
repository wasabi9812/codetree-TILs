ah, bm, ch, dm = map(int, input().split())

# Please write your code here.
et = 0
while True:
    if ah == ch and bm == dm:
        break
    et+=1
    bm+=1

    if bm==60:
        ah+=1
        bm=0

print(et)