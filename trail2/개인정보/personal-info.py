n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class man:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

temp = []

for i in range(5):
    temp.append(man(name[i], height[i], weight[i]))
temp2= temp[:]
temp.sort(key=lambda x: x.name)
temp2.sort(key=lambda x: x.height,reverse=True)

print("name")
for i in range(5):
    print(temp[i].name,temp[i].height, temp[i].weight)
print()
print("height")
for i in range(5):
    print(temp2[i].name,temp2[i].height, temp2[i].weight)