def solution(board, moves):
    basket=[]
    answer = 0
    w = 0
    b = 0

    #moves위치 인식후 해당자리 집게이동
    for a in range(1):
        doll = moves[a]-1
        #print(doll)
        colum = [ i [doll] for i in board]
        #print(colum)

    #인형 구별
        for b in colum:

            if colum[b] != 0:
                basket.append(colum[b]) 
                colum[b] = 0
                print("b!:",b)
                print("c_b!:" , colum[b])
                print("!c" , colum)
                print("basket:",basket)
                break

            elif colum[b] == 0:
                print("b:",b)
                print("c_b:" , colum[b])
                continue

        if basket[-1:] == basket[-2:-1]:
            basket.pop()
            basket.pop()
            answer +=2

    return answer

board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
