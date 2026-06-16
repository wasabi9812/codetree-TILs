n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class history:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


result = []

for i in range(n):
    result.append(history(date[i], day[i], weather[i]))

result.sort(key=lambda x: x.date)
temp =[]
for i in range(len(result)):
    obj = result[i]
    if obj.weather == "Rain":
        temp.append(obj)
        break

obj = temp[0]
print(obj.date, obj.day, obj.weather)
