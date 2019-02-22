while True:
    number = input("숫자열을 입력해주세요 : ")
    for n in range(0,10):
        if number.count(str(n)) != 1:
            print("false")
            break
        else:
            if n == 9:
                print("True")