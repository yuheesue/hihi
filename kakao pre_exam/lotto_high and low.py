#clear 21.05.08
def solution(lottos, win_nums):
    
    i = 0
    for n in range(6):
        if lottos[n] in win_nums:
            i += 1

    if lottos.count(0) == 0 and i == 0: #아무것도 안맞고, 아무것도 지워지지 않은 경우 예외처리
        i += 1

    high = 7 - (lottos.count(0)+i)

    if i == 0:  #아무것도 안맞고, 다 지워졌을때의 예외처리
        i += 1
    
    low = 7 - i

    answer = [ high , low ]

    return answer

a = [1, 2, 5, 6, 7, 8]
b = [20, 9, 3, 45, 4, 35]
print(solution(a,b))