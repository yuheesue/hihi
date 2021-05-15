def solution(enroll, referral, seller, amount):
    answer_fo = []
    answer =[]

    for m in range(len(enroll)):
        if seller.count(enroll[m])==1:
            index = seller.index(enroll[m])
            answer.append(amount[index]*100)
            answer_fo.append(amount[index]*100)
            
        elif seller.count(enroll[m])>1:
            index = seller.index(enroll[m])
            answer[m].append(amount[index]*100)
            answer_fo.append(amount[index]*100)


            for i in range(seller.count(enroll[m])-1):
                index = seller.index(enroll[m], index+1)
                answer[m] += amount[index]*100
                answer_fo.append(amount[index]*100)

        else:
            answer.append(0)

    for a in range(len(answer)):

        if answer[a] != 0:
            interest = int(answer[a] * 0.1)
            if interest >=1:  #이자율
                answer[a] -= interest   #이자율 뺀 금액

            while(interest>=1):    
                if referral[a] != "-": #b변수를 이용하기 위해 
                    b = enroll.index(referral[a]) #referral을 enroll로 옮기기 위한 위치찾기
                    if interest*0.1 >=1:
                        answer[b] += (interest - int(interest*0.1))
                        interest = int(interest *0.1)
                        a = b
                    else:
                        answer[b] += interest
                        break

                else:
                    break
                    
        else:
            continue
            
        print(enroll)
    return answer

q1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
q2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
q3 = ["young", "john", "tod", "emily", "mary", "mary", "mary","mary", "null" ]
q4 = [12, 4, 2, 5, 10, 10, 10, 10, 0 ]


print(solution(q1, q2, q3, q4))

# seller를 enroll 순서로 재 배열
# 이자율에서 seller 배열에 맞는 referral를 하나 더 생성..(?) or seller count>1일때 처음 index에 referral로 이어지도록 변환
# 두개의 for문을 하나로 합치기