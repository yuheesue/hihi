'''print(1+1)

print(2**3)
print(10%3)
print(5%2)
print(10//3)

print(10>3)
print(4>=7)
print(10<3)
print(5<=5)
print(3 == 3)
print(4 == 2)

print(not(1 != 3))
print((3>0)and(3<5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

print(2 + 3 * 4)
print((2 + 3) * 4)

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 2
print(number) 

print(abs(-5))
print(pow(4,2)) #4^2=16
print(max(5,12))#12
print(min(5,12))#5
print(round(3,14)) #3 반올림
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *

print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45 이하의 임의의 값 생성

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

from random import *

day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" , day ,"일로 선정되었습니다.")

sentence ='나는 소년입니다'
print(sentence)
sentence2="python is easy"
print(sentence2)
sentence3 ="""
im man
python is easy
"""
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])# 0 ~ 2 직전까지 (0,1)
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])

print("생년월일 : "+jumin[:6]) #처음부터 6 직전까지
print('뒤 7자리 : ' + jumin[7:]) #7부터 끝까지
print("뒤 7 자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python. lower())
print(python. upper())
print(python[0].isupper()) # 이 위치가 대문자인지 T,F
print(len(python)) # 길이수 변환
print(python.replace("Python","Java"))

index =python.index("n") #n이 몇번째 위치에 있는지
print(index)
index = python. index("n", index +1)
#뒤에는 start위치로 n 다음번부터 n을 찾아 두번째 n을 찾게됨
print(index)

print(python.find("Java")) 
#원하는 값 없을때 -1출력 후 계속 진행
#print(python.index("Java")) 
# 프로그램 중단

print(python.count("n"))
# n이 총 몇번 나오는지 


print("a"+"b")
print("a", "b")

#방법1
print("나는 %d살입니다." %20) #d는 정수
print("나는 %s을 좋아해요 " % " 파이썬") #문자열 string
print("Apple 은 %c로 시작해요" % "A") #문자 하나
# %s는 문자, 정수, 문자열 상관없이 다 허용

print("나는 %s 색과 %s 색을 좋아해요." %("파란", "빨간"))

#방법2
print("나는 {}살입니다.". format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
# 순번에 맞게 출력됨

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

##탈출문자
print("백문이 불여일견\n백견이 불여일타")

#\" \' : 문장 내에서 따옴표
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print('저는 \'나도코딩\'입니다.')

# \\ : 문장내에서 \
print("C:\\Users\\yhsue\\Desktop\\pythonworkspace>")

#\r : 커서를 맨 앞으로 이동
print("Red Apple \rPine")

#\b : 백스페이스 (한글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")



##Quiz

site = "http://facebook.com"
print(f"{site}")
print("rule1,2 : " +site[7:-4])

a = site[7:-4]
print(a)
print(a[ :3] )
print(len(a))
print(a.count("e"))

print(a[ :3] + str(len(a)) + str(a.count("e")) + "!")

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고 있는가?
#순서는 0부터 시작
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
#print(subway.pop())
#print(subway)

#print(subway.pop())
#print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)


#다양한 자료형 함께 사용가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)



###사전####

cabinet = {3:"유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))
#none대신 사용가능으로 표기
print("hi")
#대괄호로는 출력멈춤, cabinet.get은 none나오고 이어서출력

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])


#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

#key 들만 출력
print(cabinet.keys())


#value 들만 출력
print(cabinet.values())


#key,value 쌍으로 출력
print(cabinet.items())


#목욕탕 폐점
cabinet.clear()
print(cabinet)



###튜플###
#변경이 되지않는 목록을 사용할때,

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])


#menu.add는 불가능

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

###집합(set)###
#중복안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) #{1,2,3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java도 할 수 있거나 python 할 수  있는 개발자)
print(java | python)
print(java.union(python))

#차집합 ( java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊었어요
java.remove("김태호")
print(java)



###자료구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


###Quiz

from random import*
#user = range(1, 21) #1부터 20까지 숫자생성
#위의 코드를 쓰면 type이 range로 바뀌므로 
# list로 type을 바꾸기 위해user = list(users)를 이용해야함
lst =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
#print(lst)
print("치킨 당첨자 : ", sample(lst,1))
print("커피 당첨자 : ", sample(lst,3))
print(" --축하합니다--")
#이렇게하면 중복됨

#if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온이 어땨요?"))
if 30<= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0<= temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지마세요")


##for

print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")


for waiting_no in range(5): #0, 1, 2, 3, 4
    print("대기번호:{0}".format(waiting_no))

for waiting_no in range(1,6): #1, 2, 3, 4, 5
    print("대기번호:{0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))



##while
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer, index))
    index += 1

customer = "토르"
person = "Unknown"

while person != customer : 
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

print("맛있게드세요")



###continue 와 break
absent = [2, 5]  #결석
no_book = [7] #책을 깜빡함
for student in range(1, 11): #1~10
    if student in absent:
        continue #해당되지 않는것에 왔을때 다음것 이어서 반복
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0},책을 읽어봐".format(student))



##한줄 for 문

#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students) #8, 4, 10

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


##Quiz6=> 성공!
from random import*

client = 0
for customer in range(1,51):

    time = randrange(5,51)

    if 5 <= time <= 15:
         client += 1 
         print("[o] {0}번째 손님 (소요시간 : {1})".format(customer, time))

    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(customer, time))


print("총 탑승 승객 : {}".format(client))

##함수


def open_account(): #def 뒤 함수이름 괄호 콜론
    print("새로운 계좌가 생성되었습니다.")

open_account()


##전달값과 반환값
def open_account(): #def 뒤 함수이름 괄호 콜론
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은{0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):#저녁에 출금 수수료
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
#alance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은{1}원입니다.".\
    format(commission, balance))


##기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}."\
#         .format(name, age, main_lang))

# profile ("유재석", 20, "파이썬")
# profile ("김태호", 25, "자바")

#같은 학교, 학년, 반, 수업

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어{2}"\
        .format(name,age,main_lang))

profile("유재석")
profile("김태호")


##키워드값

def profile(name, age , main_lang ):
    print(name, age, main_lang)

profile(name="유재석", main_lang = "파이썬", age=20)
profile(main_lang = "자바", age=20, name="김태호")

##가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : \t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : \t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석",20,"python", "Java","C","C++", "C#","JavaScript")
profile("김태호",25, "Kotlin", "Swift")


##지역변수와 전역변수
gun = 10 

def checkpoint(soldiers): # 경계근무
    global gun #전역 공간에 있는 gun 사용 #전역변수 많이 쓰면 코드 복잡
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
#=>전역변수로 gun을 받은경우

def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    return gun
#=> 입력받고 return하여 gun을 사용한 경우

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))



##퀴즈
def std_weight(height, gender):
    if gender == "남자":
        weight = height**2* 0.01**2 * 22

    elif gender == "여자":
        weight = height **2* 0.01**2 * 21

    else:
        print("다시 입력해주세요")
        height = int(input("키가 어떻게 되시나요?"))
        gender = input ("성별이 무엇인가요?")
        weight = std_weight(height, gender)
    
    weight = round(weight, 2)

    return weight


height = int(input("키가 어떻게 되시나요?"))
gender = input ("성별이 무엇인가요?")
weight = std_weight(height, gender)
print("키{0}cm {1}의 표준 체중은 {2}kg입니다."\
        .format(height, gender, weight))


###표준 입출력
print("python", "Java",  sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("python", "Java", file=sys.stdout)#표준출력
print("python", "Java", file=sys.stderr)
#표준에러로 처리되는 부분에 의해 따로 로깅을 하여 따로 에러처리

#시험성적
scores ={"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")


#은행 대기순번표
#001, 002, 003,
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(4))

answer = input("아무 값이나 입력하세요 : ")
# 사용자 입력을 통해 값을 받게되면 항상 문자열형태 str.
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")


###다양한 출력포맷

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500)) #       500

#양수일땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) #      +500
print("{0: >+10}".format(-500)) #      -500

#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(-500)) #-500______

#3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000)) #100,000,000,000

#3자리 마다 콤마를 찍어주기, +,- 부호도 붙이기
print("{0:+,}".format(100000000000)) #+100,000,000,000
print("{0:+,}".format(-100000000000)) #-100,000,000,000

#3자리 마다 콤마를 찍어주기, +,- 부호도 붙이고, 자릿수 확보하기
#돈이 많으면 행복하니까 빈자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))

#소수점 출력
print("{0:f}".format(5/3))

#소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))



##파일 입출력
score_file = open("score.txt", "w", encoding="utf8") #w 쓰기용도
#endcoding utf8을 정의하지 않으면 한글이 이상한 문자로 정의될수 있으므로 무조건 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") 
#w쓰면 덮어쓰기 되므로 a로 덧붙여 쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #write는 줄바꿈 자동안됨
score_File.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", encoding = "utf8")
while True: #파일이 몇줄인지 모를때 반복문 사용
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines()#list 형태로 저장
for line in lines:
    print(line)
score_file.close()


###pickle
#프로그램상에서 사용하고 있는 데이터를 파일로 저장하는것
import pickle
profile_file = open("profile.pickle", "wb" )
#wb는 binary인데 pickle에서는 이를 사용해야함. 따로 encoding 필요없음
profile = {"이름" : "박명수", "나이":"30", "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb" )
profile = pickle.load(profile_file)
#file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#우리가 가지고 있는 데이터를 pickle이용해서 file에 저장하고 file에 있는 내용을 load를 통해 불러와서 변수에 저장하여 계속 이용할수있도록 도와주는 library


####with

import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
#     #close할 필요없이 자동 탈출

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())


#퀴즈
import pickle
for n in range(51):
    with open("{0}주차.txt".format(n),"w",encoding="utf8") as report_file:
       report_file.write("- {0} 주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : ".format(n))
    
    with open("{0}주차.txt".format(n),"r",encoding="utf8") as report_file:
        print(report_file.read())'''


'''###9-1클래스
#스타크래프트 예시
#마린 : 공격 유닛, 군인. 총을 쏠 수 잇음
name = "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

#탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반모드 / 시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력{1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35

print("{}유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력{1}\n".format(tank2_hp,tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

class Unit:
    def __init__(self, name, hp, damage):
        #__init__ 파이썬에서 쓰이는 생성자. 객체가 만들어질때 자동호출
        self.name =name #멤버변수,class내의 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marinel = Unit("마린", 40, 5) #객체, class로 부터 만들어지는 것
marine2 = Unit("마린",40, 5)
tank = Unit("탱크", 150, 35)
#marine3 = Unit("마린")
#marine3 = Unit("마린", 40) 
# #unit함수에서 정의된 self를 제외한 개수만큼 똑같이 보내주어야 객체를 만들수 있음

#레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
#멤버 변수를 class외부에서 사용 가능

#마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것(빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True #외부에서 변수 추가 할당
#class외부에서 내가 원하는 변수 확장 가능, 확장한 객체에만 적용됨
if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

###9-4 메소드
#일반 유닛
class Unit:
    def __init__(self, name, hp, damage):
        #__init__ 파이썬에서 쓰이는 생성자. 객체가 만들어질때 자동호출
        self.name =name #멤버변수,class내의 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


class AttackUnit:
    def __init__(self, name, hp, damage):
    #__init__ 파이썬에서 쓰이는 생성자. 객체가 만들어질때 자동호출
        self.name =name #멤버변수,class내의 정의된 변수
        self.hp = hp
        self.damage = damage

#공격 유닛/ self는 자기자신을 의미
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
            .format(self.name, location, self.damage))
            #self 붙어있는건 위에 정의된것,  안붙어 있는건 전달받은 값
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))


#파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

#공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

###상속
#메딕 : 의무병
class Unit:
    def __init__(self, name, hp):
        self.name =name 
        self.hp = hp

class AttackUnit(Unit): #일반 유닛을 중복되는 이름과 hp를 상속받아서 만들어지는것.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage


#드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 불가

class Unit:
    def __init__(self, name, hp):
        self.name =name 
        self.hp = hp

class AttackUnit(Unit): #일반 유닛을 중복되는 이름과 hp를 상속받아서 만들어지는것.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

#공격 유닛/ self는 자기자신을 의미
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력 {2}]"\
            .format(self.name, location, self.damage))
            #self 붙어있는건 위에 정의된것,  안붙어 있는건 전달받은 값
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

#날수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_Speed):
        self.flying_speed =flying_Speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"\
            .format(name, location, self.flying_speed))

    
#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init(name, hp, 0)
        #super와 Unit으로 사용되는건 똑같지만 super에서는 뒤에 ()를 붙이고, self를 안쓰는 차이가 있음
        self.location = location

###간단하게 class 와 상속에 대해 
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
#다중 상속시 super를 이용하면 맨처음에 사용되는 class만 호출됨.
        Unit.__init__(self)
        Flyable.__init__(self)    
#두개를 다 호출하기 위해서는 각자 따로 init함수로 호출해줘야함

#드랍쉽
dropship = FlyableUnit()


##퀴즈8

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
            .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

print("총 3대의 매물이 있습니다.")
h1 = House("강남", "아파트", "매매", "10억", "2010년")
h1.show_detail()
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h2.show_detail()
h3 = House("송파", "빌라", "월세", "500/50", "2000년")
h3.show_detail()

###10-1 예외처리

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 :")))
    nums.append(int(input("두번째 숫자를 입력하세요 :")))
    #nums.append(nums[0] / nums[1])
    print("{0} / {1} = {2}".format(nums[0],nums[1],nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)


##10-2에러 발생시키기 

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 :"))
    num2 = int(input("두번째 숫자를 입력하세요 :"))
    if num1>= 10 or num2 >=10:
        raise ValueError
    print("{0} / {1} = {2}.".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


##10-3 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 :"))
    num2 = int(input("두번째 숫자를 입력하세요 :"))
    if num1>= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}.".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: #오류가 나거나 정상적으로 작동해도 정상적으로 종료
    print("계산기를 이용해주셔서 감사합니다.")'''


####퀴즈9
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):

    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        
        elif order > 0 and order < chicken:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order
        
        elif order == chicken:
            raise SoldOutError("")
        
        else:
            raise ValueError
        
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
