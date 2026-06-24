m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
day_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

timepass = 1

while True:
    if m2 ==m1 and d2 ==d1:
        break
    
    timepass +=1
    d1+=1

    if d1 > day_month[m1]:
        if m1 ==12:
            m1 = 1
            d1 = 1
        else:
            m1+= 1
            d1 = 1

print(timepass)