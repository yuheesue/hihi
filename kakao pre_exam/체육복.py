n = 5
lost = [1,3,5]
reserve = [1,2,3,4,5]


answer = 0
student = []

for a in range(n+1):    #모든학생 1로 세팅
    student.append(1)

for b in lost:  #체육복 잃어버린 학생 0으로 세팅
    student[b] = 0

for e in range(len(lost)):  #잃어버린 학생과 여벌학생 같을때 2로세팅
    for f in range(len(reserve)):
        if e == f:
            student[e] = 2

for c in reserve:
    if c == 1 or student[c] !=2 or student[c-1] == 1  :    #맨앞사람, 앞사람 잃어버리지 X
        if c != n and student[c+1] == 0:    #맨뒷사람X, 뒷사람 잃어버리지 O
            student[c+1] = 2    #뒷사람에게 2

for d in reserve:
    if d == n or student[d] !=2 or student[d+1] == 1 :    #맨뒷사람O, 뒷사람 잃어버리지 X
        if student[d-1] == 0:    #맨앞사람, 앞사람 잃어버리지 X
            student[d-1] = 2    #앞사람에게 2

for g in reserve:
    if student[g-1] == 0 and student[g+1] == 0: 
        student[g-1] = 2

    
answer = n - student.count(0)

print(answer)
print(student)


