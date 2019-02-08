#입력이 있고 출력이 있는 함수
def my_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1+num2

a, b =input("두 수를 입력하세요: ").split()
a = int(a)
b = int(b)
print("num1+num2="+str(my_sum(a,b)))
