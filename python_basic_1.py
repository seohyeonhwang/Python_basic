'''
#2019.9.20
#example 17
print("분자 입력해")
numerator = int(input())
print("분모 입력해")
denominator=int(input())

#example19
print("소수로" + str(numerator/denominator) + "임")

print("몫은" + str(numerator//denominator) + "임")
print("나머지는" + str(numerator%denominator)+"임")

print("몫은"+ str(int(numerator/denominator))+"임")


#example20
print("다섯개의 수를 입력하시오, 단 정수형태여야 함 ")
print("a를 입력하시오")
a = int(input())
print("b를 입력하시오")
b = int(input())
print("c를 입력하시오")
c = int(input())
print("d를 입력하시오")
d = int(input())
print("e를 입력하시오")
e = int(input())

sum=a+b+c+d+e
print("모든 합은"+str(sum)+"임")
print("모든 평균은" +str(sum/5)+"임")

'''
#preview
print("100개의 숫자의 평균을 계산하는 계산기임")
print("수열로 이루어진 숫자를 계산하고자 하면 1을 랜덤한 숫자를 계산하고자 하면 2를 선택하시오")
choose = input()

if choose == 1:
    print("시작할 숫자를 입력하시오, 단 정수형태여야 함")
    start_num = int(input())
    print("공차를 입력하시오, 단 정수형태여야 함")
    add_num = int(input())
    summ = 0
    for i in range(99):
        start_num = start_num + i*add_num
        summ += start_num
        end
    print("100개 숫자의 합은" + str(int(summ))+"임")
    print("100개 숫자의 평균은" + str(summ/100)+"임")

if choose==2:
    print("안해")
'''
#quiz
r=4
l = 2*3.14*r
print(l)
s = 3.14*r**2
print(s)
v = 4/3 *3.14* r**3
print(format(v,'0.4f'))

x = 1.9
print(float(int(x)))
print(type(x))
print(int(float(str(x))))
print(type(x)) ##낚이지 말기!! x는 float임
    ##quiz 4번에 - 부호가 우선순위 2순위인거 잊지 말기(사진 찍어둠)
    ##숫자(int,float)끼리는 더할 수 있지만 str이 섞이면 사칙연산 안됨/ bool도 숫자임

x = 1
y = 2
y *= x +3
print(y)
#quiz 7번의 경우 operator 오른쪽에 있는 연산을 끝낸 후 operator를 돌린다. y = (x+3)*y
#quiz 8번의 경우 print(x/y) 는 float임!!!!!! 조심
