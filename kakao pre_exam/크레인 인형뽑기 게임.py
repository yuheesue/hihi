board =[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

basket=[]
answer = 0


#moves위치 인식후 해당자리 집게이동
for a in moves:
    for b in range(len(board[0])):
        if board[b][a-1] != 0:
            basket.append(board[b][a-1])
            board[b][a-1] = 0

            if len(basket)>1 and basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer +=2
            break

print(answer)