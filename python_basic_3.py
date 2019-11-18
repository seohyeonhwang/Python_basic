####2018.10.2 LECT 5 본인이 생각하시기에 제일 중요하다고,,,ㅋㅋ####
'''
##review_quiz
title = '문제해결과SW프로그래밍'
print(title[0] + title[2] + title[7])
print(title[0],title[2],title[7])

title1 = '문제'
title2 = '해결과'
title3 = 'SW'
title4 = '프로그래밍'
print(title1[0]+title2[0]+title4[0])

print('정수를 입력하세요')
number = int(input())
print(number)
number = int(input('정수를 입력하세요\n'))#한줄로 엮을 수 있어 #input은 string
print(number)

##ex32
if number % 2 == 0:
    print("x는 짝수입니다")
else: ##x % 2 == 1 인거 밖에 없을 때만 else씀
    print("x는 홀수입니다")
    #부등호 먼저!! 다음에 =!!!

##ex33 
if number >0 :
    print("x는 양수입니다")
else :
    if number <0 :
        print("x는 음수입니다")
    else:
        print("x는 0입니다")

##ex34
if number >0 :
    print("x는 양수입니다")
elif number <0 :
    print("x는 음수입니다")
else:
    print("x는 0입니다")
        #else는 꼭 없어도 됨. 대신 else는 2개 이상은 안됨

##ex35 - 1, 2 
age = int(input("나이를 입력하세요"))

if age < 0 :  ##문제 !! 입력값을 다르게 입력했을 때
    print("잘못입력하셨어요")
elif age >= 0 and age < 10:
    print("0대네요")
elif age >= 10 and age < 20 : ## &&, & 아니고 and 로 써야함!!
    print("10대네요")
elif age >= 20 and age < 30 :
    print("20대네요")
elif age >= 30 and age < 40 :
    print("30대네요")
else : ##else 뒤에는 아무것도 안와야 해요!!!
    print("40대 이상이네요")
'''
##ex35 - 3
age = int(input('나이 입력:'))
if age < 0:
    print('잘못 입력했습니다.')
elif age < 10:
    print('0대 입니다.')
elif age < 20:
    print('20대 입니다.')
else:
    print('20대 이상입니다.')
    ##이런식으로 필터링 해도 괜찮음

##ex36
age = int(input('나이 입력:'))
if age >= 20 and age < 30 :
    print("20대입니다")
else :
    print("20대 아닙니다")

##교수님 ver #이건 좀 이상한데 아닙니다가 두번나
if age < 20 :
    print("20대 아닙니다")
elif age <= 30:
    print("20대 입니다")
else :
    print("20대 아닙니다")    
