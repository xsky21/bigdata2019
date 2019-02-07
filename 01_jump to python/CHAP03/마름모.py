# coding: cp949
while True:
    num=int(input("홀수를 입력하세요(0<-종료): "))
    point = 1
    prt_point = "*"*point
    space = int((num-point)/2)
    prt_space = " "*space
    if num == 0 : break
    elif num % 2 == 0 : continue
    else:
        while point <= num:
            print("{0}{1}".format(prt_space,prt_point))
            point=point+2

