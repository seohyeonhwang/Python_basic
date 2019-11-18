###2019.11.08####

#g29
def f(x):
    y = 2* x +1
x = 2
z = f(x)
print(z)
    ##none 출

#pg31
def addition(a, b):
    c= a +b
    return c
y = addition(1,3)
print(y)

def addition(a, b):
    c= a +b
    print(c)
y = addition(1,3)
print(y)
    ##none 출력

#pg38
def add_mul(a,b):
    add_result=a+b
    mul_result=a*b
    return add_result
    return mul_result
    ## 첫 리턴을 만나면 함수가 끝남!!!!! 다음 리턴은 안보고 넘어기기 때문에 7나옴
a=2
b=5
x=add_mul(a,b)
print(x)

def add_mul(a,b):
    add_result=a+b
    mul_result=a*b
    return add_result, mul_result
a=2
b=5
x=add_mul(a,b)
add, mul = add_mul(a,b)
print(x)    ##두개를 리턴하는 함수를 한번에 받으면 (튜플)로 나옴~!!!!! not 리스트!
print(add)
print(mul)

##pg39
##함수 내 변수는 지역변수! 쓰는 이유는 함수 안과 밖의 변수를 구분하기 위해서/데이터만 전달
#ex70 맨 왼쪽애랑 중간 애랑 완전히 똑같다. 헷갈nono
#ex70 맨 오른쪽 애는 x라는 변수를 전역변수로 이용하는 
