###2019년 11월 1일###

#ex57
family = ("fater", "mother", "sister","brother")
print(family[1])
##tuple은 내용이 바뀌지 않지만 index접근은 []으로

#ex58
profile = {'이름' : '서현', "나이":22, '소속': '이대'}
print(profile)
#print(profile[1])
#dict은 순서가 중요하지 않아서 index를 뽑아낼 수 없

dictionary = {'pi':3.141592, 'e':2.718281}

r = float(input('반지름:'))
print('원 둘레:' + str(2*dictionary['pi']*r))
print('원 넓이:' +str(dictionary['pi']*r*r))
#dict는 순서가 중요하지 않아서 insert 나 append가 없다 <- 순서도 없으니까
#dict는 key가 있으면 출력하고 없으면 추가함
#dict은 remove도 없다... del이 있다
profile['이름'] = '서현 황'
print(profile)
profile['직업'] = ' 학생'
print(profile)

#ex63
menu = ['coffee', 'latte', 'smoothie', 'tea']
price1 = {'smoothie': 4500, 'tea': 3000, 'coffee': 3500, 'latte': 4000}
price2 = {menu[0]: 3500, menu[1]: 4000, menu[2]: 4500, menu[3]: 3000}
print(price1 == price2)

##과제 안내
#메뉴와 가격이 변경가능 하다는 건 너맘대로 메뉴를 바꿔도 된다는 뜻이다.
