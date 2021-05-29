def solution(answers):

    p = 0
    n = 0
    correct = 0
    answer = []
    math1 = [1,2,3,4,5]
    math2 = [2,1,2,3,2,4,2,5]
    math3 = [3,3,1,1,2,2,4,4,5,5]

    while( p == len(answer)):
        
        math1[p] = p%5+1
        
        if p%2 == 0:
            math2[p] = 2
        elif p%8 == 1:
            math2[p] = 1
        elif p%8 == 3:
             math2[p] = 3
        elif p%8 == 5:
             math2[p] = 4
        elif p%8 == 7:
             math2[p] = 5 

        math3.append(math[p])       


            math2[p] =  p%8
            1,9,17
            4,12,8
        if


    return answer

    1,2,3,4,5,6,7,8,9,10
    0,5,10,