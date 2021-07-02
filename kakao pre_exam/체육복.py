n = 5
lost = [2,4]
reserve = [3]


answer = 0
student = []
for a in range(n+1):    #모든학생 1로 세팅
    student.append(1)

for b in lost:  #체육복 잃어버린 학생 0으로 세팅
    student[b] = 0

for e in lost:  #잃어버린 학생과 여벌학생 같을때 2로세팅
    for f in reserve:
        if e == f:
            student[f] = 2

for c in reserve: #뒷사람에게 주기위함
    if student[c] != 2 :
        if c == 1 or student[c-1] != 0  :    #맨앞사람, 앞사람 잃어버리지 X
            if c != n and student[c+1] == 0:    #맨뒷사람X, 뒷사람 잃어버 O
                student[c+1] = 2    #뒷사람에게 2


for d in reserve:
    if student[d] != 2 :    #앞사람에게 주기위함
        if d == n  or student[d+1] == (1 or 2) :    #맨뒷사람O, 뒷사람 잃어버리지 X
            if student[d-1] == 0:    #맨앞사람, 앞사람 잃어버 o
                student[d-1] = 2    #앞사람에게 2
        elif d == n or student[d+1] == 0 :  #앞뒤로 다 잃어버린 경우.
                student[d-1] = 2

answer = n - student.count(0)
print(answer)
print(student)

