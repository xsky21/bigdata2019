#입력이 있고 출력이 없는 함수
def my_sum(num1, num2):
    num1=num1+1000
    num2=num2+1000
    print("num1+num2="+str(num1+num2))
num1, num2 =input("두 수를 입력하세요: ").split()
num1 = int(num1)
num2 = int(num2)
my_sum(num1,num2)
#my_sum()
