'''def solution(s):
    
    while(True):
        if s.find("one"):
                answer = s.replace("one","1")
                
        if s.find("two"):    
                answer = s.replace("two","2")
            
        if s.find("three"):
                answer = s.replace("three","3")
            
        if s.find("four"):
                answer = s.replace("four","4")
                
        if s.find("five"):
                answer = s.replace("five","5")
            
        if s.find("six"):
                answer = s.replace("six","6")
                
        if s.find("seven"):
                answer = s.replace("seven","7")
                
        if s.find("eight"):
                answer = s.replace("eight","8")
                
        if s.find("nine"):
                answer = s.replace("nine","9")
                
        if s.find("zero"):
                answer = s.replace("zero","0")


    
    return answer

print(solution("one2three4zero"))'''


'''def solution(s):
    
    while(True):
        if s.find("one"):
            answer = s.replace("one","1")
        el
            
        elif s.find("two"):    
            answer = s.replace("two","2")
        
        elif s.find("three"):
            answer = s.replace("three","3")
        
        elif s.find("four"):
            answer = s.replace("four","4")
            
        elif s.find("five"):
            answer = s.replace("five","5")
        
        elif s.find("six"):
            answer = s.replace("six","6")
            
        elif s.find("seven"):
            answer = s.replace("seven","7")
            
        elif s.find("eight"):
            answer = s.replace("eight","8")
            
        elif s.find("nine"):
            answer = s.replace("nine","9")
            
        elif s.find("zero"):
            answer = s.replace("zero","0")
        
        else:
            break

    
    return answer'''

def solution(s):

    if s.find("one" or "two" or "three" or "four" or "five" or "six" or "seven" or "eight" or "nine" or "zero"):
        if s.find("one"):
            a1 = s.replace("one","1")
        else:
            a1 = s
        a2 = a1.replace("two","2")
        a3 = a2.replace("three","3")
        a4 = a3.replace("four","4")
        a5 = a4.replace("five","5")
        a6 = a5.replace("six","6")
        a7 = a6.replace("seven","7")
        a8 = a7.replace("eight","8")
        a9 = a8.replace("nine","9")
        answer = a9.replace("zero","0")
        
        print(a9)
        return answer   

solution("one2three4zero")