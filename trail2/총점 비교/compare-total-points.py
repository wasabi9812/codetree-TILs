n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class students:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 =s1
        self.s2 =s2
        self.s3 =s3

temp = []

for i in range(n):
    temp.append(students(name[i],score1[i],score2[i],score3[i]))

temp.sort(key = lambda x: x.s1 + x.s2 + x.s3)

for i in range(n):
    print(temp[i].name, temp[i].s1, temp[i].s2,temp[i].s3)