n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.


class people:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

temp = []
for i in range(n):
    temp.append(people(name[i],height[i],weight[i]))

temp.sort(key = lambda x: x.height)

for i in range(n):
    print(temp[i].name, temp[i].height, temp[i].weight)
    