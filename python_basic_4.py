####2019.10.04####

'''
#ex37

import random

option = ['가위','바위','보']

index = random.randint(0,2)
    ##random.sample(range(0,3),1) but 얘는 리스트로 반환됨
    ##random.sample(options, 1)
    
computer = option[index]
    ##sample 함수 쓸거면 option[index[0]]으로 써야
    ##두번째 sample쓸거면 computer = index[0]
    
print("컴퓨터는"+computer+"를 선택함")

#ex37
print("가위 바위 보 중에서 선택하세요")
player = input()

if player != "가위" and player != "바위" and player != "보": ##or 아니지 잘못했지
    print("이상한 거 치지 마라")
    exit() #exit이 없으면 다음 뭘 입력함도 나

print("사용자는 " + player +"를 입력함")

#ex37
if player==computer:
    print("비겼습니다")
elif computer == '가위' and player == '보':
    print('졌습니다.')
elif computer == '가위' and player == '바위':
    print('이겼습니다.')
elif computer == '바위' and player == '보':
    print('이겼습니다.')
elif computer == '바위' and player == '가위':
    print('졌습니다.')
elif computer == '보' and player == '가위':
    print('이겼습니다.')
elif computer == '보' and player == '바위':
    print('졌습니다.')


#ex38
import random
X = random.sample(range(0,100),3)  ##random.randint((0,100),3) 안됨 왜? randint는 int하나임
print(X)

if X[0]>=X[1] and X[0]>=X[2]:
    print(X[0])
if X[1]>=X[0] and X[1]>=X[2]: #elif 도 오케이
    print(X[1])
if X[2]>=X[0] and X[2]>=X[0]: #elif 도 else 도 오케이
    print(X[2])
    ##같은 경우는 제외하는 이유가 1)어차피 1번 if에서 다 같으니까 X[0]로나옴
    ## 2) sample은 중복허용을 안해서

print(max(X))

#quiz1
import random
six1 = random.randint(1,6) #randint는 하나뽑아주고 a<=num<=b
six2 = random.randint(1,6)

if six1 == six2:
    print("한 번 더!")
else:
    print(str(six1+six2)+"만큼 이동합니다")
'''
#quiz2
print("정수를 입력하세요")
num=int(input())
if num % 10 >= 5:
    sumnum = num + (10 - (num%10))
    print(sumnum)
else:
    sumnum = num - num%10
    print(sumnum)
