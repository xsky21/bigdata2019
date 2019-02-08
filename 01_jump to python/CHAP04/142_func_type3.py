#입력이 없고 출력이 있는 함수
def my_sum():
    num1, num2 =input("두 수를 입력하세요: ").split()
    num1 = int(num1)
    num2 = int(num2)
    return num1+num2

result=my_sum()

print("num1+num2="+str(result))
#my_sum()
