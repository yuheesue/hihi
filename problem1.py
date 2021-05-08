s = "one2three4zero"

def solution(s):

    if s.find("one"):
        s = s.replace("one","1")
        

    if s.find("two"):
        s = s.replace("two","2")

    if s.find("three"):
        s = s.replace("three","3")

    if s.find("four"):
        s = s.replace("four","4")

    if s.find("five"):
        s = s.replace("five","5")

    if s.find("six"):
        s = s.replace("six","6")

    if s.find("seven"):
        s = s.replace("seven","7")

    if s.find("eight"):
        s = s.replace("eight","8")

    if s.find("nine"):
        s = s.replace("nine","9")

    if s.find("zero"):
        s = s.replace("zero","0")


    answer = s
    return answer

    print(solution)