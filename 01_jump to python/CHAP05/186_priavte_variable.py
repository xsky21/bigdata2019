#-*-coding: utf-8 -*-#
class Service:
    secret="영구는 배꼽이 두 개다." #클래스가 가지는 고유의 공통속성
    name=""
    def __init__(self, name): #언더스코어 두개의 의미는 이 함수가 원래 파이썬에 있는 함수란 것을 의미한다
        self.name= name
    def sum(self, a, b):
        result = a+b
        print("%s님 %s+%s=%s입니다." % (self.name, a,b,result))

pey= Service("홍길동") #객체만이 가지는 고유의 초기값을 설정하고 싶을 때 생성자를 활용한다.
print(pey.secret)
