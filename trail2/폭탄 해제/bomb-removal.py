unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

obj = bomb(unlock_code,wire_color,seconds)

print("code :",obj.code)
print("color :",obj.color)
print("second :",obj.sec)