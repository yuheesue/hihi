def solution(answers):

    p = 0
    i = 0
    answer = []
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]

    while( p+5 == len(answer)):
        
        math1.append(math1[p])
        math2.append(math2[p])
        math3.append(math3[p])       

    return answer

    1,2,3,4,5,6,7,8,9,10
    0,5,10,