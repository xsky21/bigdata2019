#입력이 있고 출력이 없는 함수
def my_sum(num1, num2):
    print("num1+num2="+str(int(num1)+int(num2)))

num1, num2 = input("두 수를 입력하세요: ").split()
my_sum(num1,num2)
#my_sum()
