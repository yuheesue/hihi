def solution(enroll, referral, seller, amount):
    count =[]
    help = 0
    enroll_plus = []  #중복파트 뒤에 붙이기 위함
    referral_plus = []  #중복파트 뒤에 붙이기 위함
    answer_plus = []  #중복파트 뒤에 붙이기 위함
    answer =[]  #중복되는 값 합해놓은, 중복 없는.

    for m in range(len(enroll)):
        count.append(seller.count(enroll[m]))
        
        if int(count[m]) > 1:
            index = seller.index(enroll[m])
            answer.append(amount[index]*100)
            for i in range(count[m]-1):
                index = seller.index(enroll[m], index+1)
                answer_plus.append(amount[index]*100)
                referral_plus.append(referral[m])
                enroll_plus.append(enroll[m])

        elif count[m] == 0:
            answer.append(0)
        
        else:
            index = seller.index(enroll[m])
            answer.append(amount[index]*100)


    enroll.extend(enroll_plus)
    referral.extend(referral_plus)
    answer.extend(answer_plus)


    for a in range(len(enroll)):
        if answer[a] != 0 :  #0이 아닐때
            if a<8:   
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

            elif a>7:  
                interest = int(answer[a] * 0.1)

                if interest >=1:  #이자율
                    answer[a] -= interest   #이자율 뺀 금액
                    w = enroll.index(enroll[a])
                    answer[w] += answer[a]
 

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

    del answer[8:]
    return answer

q1 = ["john", "mary", "edward", "sam",    "emily", "jaimie", "tod",     "young"]
q2 = ["-"   , "-"   , "mary"  , "edward", "mary",   "mary",  "jaimie", "edward"]
q3 = ["young", "john","sam", "-", "young"]
q4 = [12, 12, 0, 0, 5 ]


print(solution(q1, q2, q3, q4))

# seller를 enroll 순서로 재 배열
# 이자율에서 seller 배열에 맞는 referral를 하나 더 생성..(?) or seller count>1일때 처음 index에 referral로 이어지도록 변환
# 두개의 for문을 하나로 합치기