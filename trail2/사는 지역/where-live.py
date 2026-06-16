n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.


class spot:
    def __init__(self,name,add,reg):
        self.name = name
        self.add = add
        self.reg = reg


result = []

for i in range(n):
    result.append(spot(name[i],street_address[i],region[i]))

result.sort(key=lambda x: x.name, reverse=True)
obj1 = result[0]

print("name", obj1.name)
print("addr", obj1.add)
print("city", obj1.reg)