#입력, 출력이 없는 함수. 함수 내부에서 과정이 끝나는 것
def my_sum():
    #함수 정의
    num1, num2 = input("두 수를 입력하세요: ").split()
    print("num1+num2="+str(int(num1)+int(num2)))

print("입력(parameter), 출력(return)이 없는 함수 테스트")
my_sum()
