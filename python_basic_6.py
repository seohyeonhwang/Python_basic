#####2019.10.18#####
##ex53

i=0
while i!=100:
    print(i)
    i+= 1

i=0
while i<100:
    print(i)
    i+=1
    ##100사이니까 100은 포함 안함 그래서 101 말고 100 써야
    
##ex54##
i = 0
while i<100:
    if i%2==1:
        print(i)
    i+=1
#또는, 아래가 훨씬 연산 횟수가 적다
j = 0
while j <100:
    print(i)
    i+=2

##ex55##
busket = []
while item != "end":
    print("주문할 아이템을 써요")
    item = input()
    busket.append(item)
    if item == "end":
        break
print("끝")
###이건 안돌아가는 거 알지? item이 미리 정의가 안된 애니까

while 1:
    order = input("주문할 아이템을 써요")
    if order == "end":
        break
    else:
        orderbusket.append(order)
print(orderbusket)

##ex56##
import random
print("컴퓨터가 정한 랜덤 숫자가 있습니다.")
computer = random.randint(1,50)
print(computer)
i=1
while i<8:
    print("당신이 부른 숫자는")
    user = int(input(str(i)+"번째에"))
    i+=1
    if user < computer:
        print("up")
    elif user > computer:
        print("down")
    else:
        print("대박... 맞춤. 컴이 먹음")
        break
print("끝까지 못마셨네, 나머지 마셔라")

###코드는 모두 봐야 3까지는
###4리스트는 나오니 공부하셈 4 모듈 안봐도 되는데 공부하셈
###모듈 다 줌
###if for while은 다 나옴
###유형1 코드를 주면 돌렸을 때 뭐나오냐
###유형2 코드 에러가 왜 에러인지 위치
###유형3 예제처럼 코드 작성하게 하는

###기출문제: family =[ mother,father,sister,brother,me]
###주어진 list family를 가지고 다음의 결과과 출력되는 코드를 작성
'''
다음 결과
me
brother
sister
father
mother
'''
family =['mother','father','sister','brother', 'me']

for i in range(5):
    print(family[4-i])
for i in range(5):
    print(family[-i-1])

for i in range(-1,-6,-1):
    print(family[i])
