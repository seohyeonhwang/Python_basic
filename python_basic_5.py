####2019.10.11####
'''
##review
print(False and False)
print(False and True)
print(True and False)
print(True and True)
#False는 0 True는 1 and는 곱셈이라고 생각
print() #enter 됨
print(False or False)
print(False or True)
print(True or False)
print(True or True)
#or은 덧셈이라고 생각
if True and False or True: #True
    print('3')
if True and True or False: #True
    print('4')
if False or False and True: #False
    print('5')
#and >>> or 우선순위

##ex_39##
for i in range(10): #10개가 나옴!
    print(i)
range(0,10,1) #0부터 10까지 1씩 증가
for i in range(0,10,3):
    print(i)

#ex40
x= []
for i in range(10):
    num=int(input('X[' + str(i) +']='))
    x.append(num)
print(x)

#ex41
sum = 0
for i in range(10):
    sum += x[i]
print(sum/10)

#ex42
family = ["mother","father","sister","brother","me"]
for i in range(len(family)):
    print(family[i])
for element in family:
    print(element)

#ex43
x =[12,45,45,98,5,2,6,3]
for i in range(len(x)):
    print(x[i])

#ex44
score = [12 ,40,45,98,67,46,33,20,15,4]
for element in score:
    if element >= 70:
        print("합격")
    elif element>=50 and element<70:
        print("재시")
    else:
        print("불합격")

#ex45
for i in range(4):
    print('i =' + str(i))
    for j in range(10):
        print("j=" + str(j))
    #중첩 for 문

#ex46
for i in range(1,10):
    print("<<구구단"+str(i)+"단>>")
    for j in range(1,10):
        print(str(i) + "X"+ str(j)+"="+str(i * j))
    print()

#quiz 1
a = 'hello world'
for i in range(len(a)):
    print(a[i])

#quiz 2
import random
x = []
sum1 = 0
sum2 = 0
for i in range(100):
    val = random.randint(0,1)  ##이거 random.sample(range(0,2),100)안되는 이유는 sample은 중복허용 불가
    x.append(val)
for element in x:
    if element == 1:
        sum1 += 1
    else:
        sum2 += 1
print("1은" + str(sum1)+"번 나옴")
print("0은" + str(sum2)+"번 나옴")
if sum1>sum2:
    print("1이 더 많음")
elif sum1<sum2:
    print("0이 더 많음")
else:
    print("같게 나옴")

#quiz 3
import random
x = random.sample(range(0,100),30)
print(x)
breakval = 0
print("0~99 사이를 입력하세요")
user = int(input())
for i in range(len(x)):
    if x[i] == user:
        breakval = 1
        print("성공")
        
if breakval == 0:
        print("실패")

#quiz 4
Max= 0
for i in range(len(x)):
    if x[i]>Max:
        Max = x[i]
print(Max)

#quiz 5
print("브루마불을 시작합니다. 주사위 두개는 컴퓨터가 자동으로 굴려줍니다")
breakval = 0
while range(2):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print(num1,num2)
    if num1==num2:
        print("탈출")
        break
    else:
        breakval += 1

    if breakval == 3:
        print("3회 이내 탈출 못했으므로 종료합니다")
        break
'''
