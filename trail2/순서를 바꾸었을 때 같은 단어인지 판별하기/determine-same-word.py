word1 = input()
word2 = input()

# Please write your code here.
temp1 = list(word1)
temp2 = list(word2)

d1 = {}
d2 = {}



for i in temp1:
    if i in d1:
        d1[i] +=1
    else:
        d1[i] = 0
for i in temp2:
    if i in d2:
        d2[i] +=1
    else:
        d2[i] = 0

if d1 == d2:
    print("Yes")
else:
    print("No")