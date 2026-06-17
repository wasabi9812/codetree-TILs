n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

class students:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

result = []
for i in range(n):
    result.append(students(name[i],korean[i],english[i],math[i]))

result.sort(key=lambda x:(x.kor,x.eng,x.mat), reverse =True)

for i in range(n):
    print(result[i].name, result[i].kor, result[i].eng, result[i].mat)