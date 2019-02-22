class Calculator: # 사용자 정의 클래스
    def __init__(self): #init은 클래스 생성자(constructor) 객체 생성시 최초로 수행되는 함수
        self.result = 0 #class 멤버 변수

    def adder(self,num): #멤버 함수(member function)
        print("%d값을 입력 받았습니다." %num)
        self.result += num + 100 #멤버 변수로 등록은 가능하나 가독성을 떨어진다.
        return self.result

cal1=Calculator()
cal2=Calculator()
cal3=Calculator()
cal4=Calculator()

print(cal1.adder(3))
print(cal2.adder(4))
print(cal3.adder(3))
print(cal4.adder(7))
