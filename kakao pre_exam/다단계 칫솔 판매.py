def solution(enroll, referral, seller, amount):
    count =[]
    help = 0
    enroll_plus = []  #중복파트 뒤에 붙이기 위함
    referral_plus = []  #중복파트 뒤에 붙이기 위함
    answer_plus = []  #중복파트 뒤에 붙이기 위함
    referral_fo = []    #중복되는 것도 그냥 enroll순으로 다 나열해놓은것, append를 쓰므로,
    answer_fo = []  #answer전 중복되는 것도 그냥 enroll순으로 다 나열해놓은것
    answer =[]  #중복되는 값 합해놓은, 중복 없는.

    for m in range(len(enroll)):
        count.append(seller.count(enroll[m]))
        
        if int(count[m]) > 1:
            index = seller.index(enroll[m])
            for i in range(count[m]-1):
                index = seller.index(enroll[m], index+1)
                answer_plus.append(amount[index]*100)
                referral_plus.append(referral[m])
                enroll_plus.append(enroll[m])

        elif count[m] == 0:
            answer_fo.append(0)
            referral_fo.append(referral[m])
        
        else:
            index = seller.index(enroll[m])
            answer_fo.append(amount[index]*100)
            referral_fo.append(referral[m])


    enroll.extend(enroll_plus)
    referral_fo.extend(referral_plus)
    answer_fo.extend(answer_plus)

    print(enroll)
    print(referral)
    print(seller)
    print(referral_fo)

    for a in range(7):
        if answer_fo[a] != 0 :  #0이 아닐때
            if a<8:   
                interest = int(answer_fo[a] * 0.1)

                if interest >=1:  #이자율
                    answer_fo[a] -= interest   #이자율 뺀 금액

                while(interest>=1):    
                    if referral_fo[a] != "-": #b변수를 이용하기 위해 
                        b = enroll.index(referral_fo[a]) #referral을 enroll로 옮기기 위한 위치찾기
                        '''print(seller[b])
                        print(referral_fo[a])
                        print(enroll[b])
                        print(answer_fo[b])'''

                        if interest*0.1 >=1:
                            answer_fo[b] += (interest - int(interest*0.1))
                            interest = int(interest *0.1)
                            a = b
                        else:
                            answer_fo[b] += interest                          
                            break

                    else:
                        break

            elif a>8:  
                interest = int(answer_fo[a] * 0.1)

                if interest >=1:  #이자율
                    answer_fo[a] -= interest   #이자율 뺀 금액
                    w = enroll.index(enroll[a])
                    answer_fo[w] += answer_fo[a] 

                while(interest>=1):    
                    if referral_fo[a] != "-": #b변수를 이용하기 위해 
                        b = enroll.index(referral_fo[a]) #referral을 enroll로 옮기기 위한 위치찾기

                        if interest*0.1 >=1:
                            answer_fo[b] += (interest - int(interest*0.1))
                            interest = int(interest *0.1)
                            a = b
                        else:
                            answer_fo[b] += interest
                            break

                    else:
                        break


        else:
            continue
            
    return answer_fo

q1 = ["john", "mary", "edward", "sam",    "emily", "jaimie", "tod",     "young"]
q2 = ["-"   , "-"   , "mary"  , "edward", "mary",   "mary",  "jaimie", "edward"]
q3 = ["young", "john", "tod", "emily", "mary"]
q4 = [12, 4, 2, 5, 10]


print(solution(q1, q2, q3, q4))

# seller를 enroll 순서로 재 배열
# 이자율에서 seller 배열에 맞는 referral를 하나 더 생성..(?) or seller count>1일때 처음 index에 referral로 이어지도록 변환
# 두개의 for문을 하나로 합치기