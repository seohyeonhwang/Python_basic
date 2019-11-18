####2019.11.06####

#함수를 쓰는 이유: 빨라짐 코드를 추가로 작성하지 않아도됨 / 여러번 사용가
#함수에서 함수 밖으로 데이터를 전달하기 위한 수단이 바로 return의 개념입니다.

##ex64
def HelloWorld():
    print("hello world")

##ex64
def SayHello(name):
    print('Hello ' + name)
a = SayHello('임성수')
print(a)  ##이거하면 none임 return한 값이 없으므로

def f(x):
    y = 2 * x + 1
x = 2
z = f(x)  ##동일한 원리로 return값이 없어서 none
