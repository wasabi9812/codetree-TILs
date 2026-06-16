user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class userspace:
    def __init__(self, id, level):
        self.id = id
        self.level = level

temp1 = userspace("codetree", 10)
temp2 = userspace(user2_id,user2_level)

print("user",temp1.id,"lv", temp1.level)
print("user",temp2.id,"lv", temp2.level)