product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class pro:
    def __init__(self, name, code):
        self.name = name
        self.code = code

obj1 = pro("codetree",50)
obj2 = pro(product_name, product_code)

print("product",obj1.code,"is",obj1.name)
print("product",obj2.code,"is",obj2.name)