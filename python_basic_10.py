##2019.11.15
'''
#quiz 4
def swap(a,b):
    return b,a
a=1
b=2
a,b=swap(a,b)
print(a,b)

#quiz 5
##list는 return을 안해도 되는 함수 중 예외!!
def listReverse(x):
#    for i in range(len(x)):
#       temp=x[len(x)-1-i]
#       x[len(x)-1-i]=x[i]
#       x[i]=temp
#이거 다시 원래대로 나온 이유는? 바뀌고 다시 바뀌어서
    for i in range(int(len(x)/2)):
        temp=x[len(x)-1-i]
        x[len(x)-1-i]=x[i]
        x[i]=temp
List=[1,2,3,4,5]
listReverse(List)
print(List)

#quiz 6
def function(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    return a #대신에 else return a 해도 됨
print(function(1,3)) #3
print(function(3,1)) #3
print(function(1,1)) #1

#quiz 7
def GCD(x,y):
    gcd=0
    for i in range(1,min(x,y)+1): #min하면 안된다. 1 더해야 포함된다.
        if x%i==0 and y%i==0:
            gcd=i
    return gcd

a = GCD(5,13)
print(a)
'''
#quiz 1
def range_sum(start, stop):
    result = 0 
    for i in range(start,stop):
        result += i
    return result

rel = range_sum(3,6)
print(rel)
'''
##재귀함수
#ex 76
def plusOne(x,n):
    if x<n:
        print(x)
        plusOne(x+1,n)

plusOne(1,10)
print(plusOne(1,10)) #여기 맨 마지막에 none나오는 이유는///?

#ex 77
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print(factorial(5))

'''
