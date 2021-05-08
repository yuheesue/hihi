def solution(s):

        if s.find("one"):
            a1 = s.replace("one","1")
        else:
            a1 = s

        if s.find("two"):
            a2 = a1.replace("two","2")
        else:
            a2 = a1

        if s.find("three"):
            a3 = a2.replace("three","3")
        else:
            a3 = a2
        
        if s.find("four"):
            a4 = a3.replace("four","4")
        else:
            a4 = a3
        
        if s.find("five"):
            a5 = a4.replace("five","5")
        else:
            a5 = a4

        if s.find("six"):
            a6 = a5.replace("six","6")
        else:
            a6 = a5
        
        if s.find("seven"):
            a7 = a6.replace("seven","7")
        else:
            a7 = a6

        if s.find("eight"):
            a8 = a7.replace("eight","8")
        else:
            a8 = a7

        if s.find("nine"):
            a9 = a8.replace("nine","9")
        else:
            a9 = a8

        if s.find("zero"):
            answer = a9.replace("zero","0")
        else:
            answer = a9
        
        print(answer)
        return answer  

solution("one2three4zero")