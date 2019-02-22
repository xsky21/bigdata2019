def sum(a,b):
    return a+b

while True:
    error_num1 = 0
    error_num2 = 0
    try :
        num1, num2 = input("두 수를 입력하세요(종료 입력시 프로그램 종료): ").split(" ")
    except ValueError:
        print("프로그램을 종료합니다.")
        exit()
    else :
        try:
            num1 = int(num1)
        except ValueError:
            error_num1 = 1
            pass
        try:
            num2 = int(num2)
        except ValueError:
            error_num2 = 1
            pass
    if error_num1:#오류는 묶어서 처리
        print("1번째 입력이 [%s]입니다." % num1)
    if error_num2:
        print("2번째 입력이 [%s]입니다." % num2)
    if error_num1 ==0 and error_num2 ==0:
        print(sum(int(num1), int(num2)))

