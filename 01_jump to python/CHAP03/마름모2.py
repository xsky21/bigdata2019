# coding: cp949
while True:
    num=int(input("홀수를 입력하세요(0<-종료): "))
    point = 1
    empty=int(num/2)
    if num == 0 : break
    elif num % 2 == 0 : continue
    else:
        while point <= num:
            print(" "*empty+"*"*point)
            point=int(point+2)
            empty=int(empty-1)
        point=int(point-2)
        empty=int(empty+1)
        while point > 0 :
            point=int(point-2)
            empty=int(empty+1)
            print(" "*empty+"*"*point)

