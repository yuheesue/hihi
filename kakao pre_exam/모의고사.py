def solution(answers):

    p = 0
    i = 0
    a = 0
    b = 0
    c = 0
    answer = []
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]

    while p+5 < len(answers):
        
        math1.append(math1[p])
        math2.append(math2[p])
        math3.append(math3[p])
        p += 1       

    for i in range(len(answers)):

        if math1[i] == answers[i]:
            a += 1

        if math2[i] == answers[i]:
            b += 1

        if math3[i] == answers[i]:
            c += 1
    
    if max(a,b,c) == a:
        answer.append(1)
    if max(a,b,c) == b:
        answer.append(2)
    if max(a,b,c) == c:
        answer.append(3)

    return answer
    
answers = [1,3,2,4,2]
print(solution(answers))
