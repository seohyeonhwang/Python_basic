###2019.09.27###

##ex28
import random

randNum = random.sample(range(1,100),5) #1이상 100미만 
print(randNum)
randNum = random.sample(range(1,100),0) #0 넣으면 빈 리스트
print(randNum)
print(type(randNum))


randNum = random.random()
print(randNum)
print(type(randNum))
#random 함수는 시험에 안나온데, 과제에는 나온데

#ex29
randNum = random.uniform(0,5) #0이상 5이
print(randNum)
randNum = random.gauss(0,1)
print(randNum)
randNum = random.randint(1,100)  #rand.sample과 차이는 list vs int
print(randNum)

#주사위 게임 만들기
randNum1 = random.randint(1,6)
randNum2 = random.randint(1,6)
    #독립시행

randNum = random.sample(range(1,7),2)
    #절대 같은 수가 나오지 않는 주사위

##ex30
x = random.sample(range(0,10),5)
print(x)
sum = x[0]+x[1]+x[2]+x[3]+x[4] #원래 built in 함수라서 안되긴 하는데 변수로 취급
#Sum=sum(x) #이렇게 넣으면 이미 변수로 이용한 sum을 built in 함수로 써서 안됨
mean = sum/len(x)
print(mean)

##ex31
#내가 짠 코드
num = random.randint(0,10)
print(num)
hol_jak = num/2
if hol_jak%2 == 0:
    print("짝수")
else:
    print("홀수")

#교과서 코드
print(num%2 > 0)
print(num, end=' ')
print('is odd?', end=' ')
print(num%2>0)


##quiz
#1번
Num = random.sample(range(1,10),5)
print(Num)
Num.sort(reverse=True) #교수님은 Num.reverse() 쓰심
print(Num)

#2번
a = [1,2,3]
b = [4,5,6]
print(a+b) #틀림!!!!!!!!!!!!!!!!!!!!리스트에 추가해줌

#3번
print(a[2]) #아마 3
print(b[1]) #아마 5

c = [a,b]
print(c) #아마 [[1,2,3],[4,5,6]]
print(c[0][1]) #아마 2 틀림!!!!!!!!!!!

#4번 네
b = [4,5,6,7]
c = [a,b]
print(c)
#5번 [[0,1],[0,1],[0,3]] 아닐까 전체 리스트 인덱스, 0번 리스트 인덱스, 1번 리스트 인덱스
#a = -3 ~ 2
#b = -4 ~ 3
#c = -2 ~ 1
print(-int(len(c)) : int(len(c))-1)  ##프린트하려면??

