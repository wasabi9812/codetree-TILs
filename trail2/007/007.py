secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class temp:
    def __init__(self, sc, mp, t):
        self.sc = sc
        self.mp = mp
        self.t = t


obj = temp(secret_code, meeting_point, time)

print("secret code :",obj.sc)
print("meeting point :" ,obj.mp)
print("time :",obj.t)