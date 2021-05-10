from math import*
def solution(enroll, referral, seller, amount):
    seller_new = []
    amount_new = []
    enroll_money = []
    answer =[]

    
        
    for n in range(len(seller)) :
        if seller_new.count(seller[n]) >0: #find -> count
            index1 = seller_new.index(seller[n])
            amount_new[index1] += amount[n]*100
        else:    
            seller_new.append(seller[n]) #seller_new[n] = seller[n]
            amount_new.append(amount[n]*100) #amount_new[n] = amount[n]




    for m in range(len(enroll)):
        if seller_new.count(enroll[m])==1:
            index2 = seller_new.index(enroll[m])
            enroll_money.append(amount_new[index2]) #enroll_money[m] = amount_new[index2]
            answer.append(enroll_money[m])
                #anaswer[m] = enroll_money[m]
        else:
            enroll_money.append(0)
            answer.append(enroll_money[m])


    
    for a in range(8):

        if enroll_money[a] != 0:
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
            
        
    return answer

q1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
q2 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
q3 = ["young", "john", "tod", "emily", "mary"]
q4 = [12, 4, 2, 5, 10]


print(solution(q1, q2, q3, q4))
