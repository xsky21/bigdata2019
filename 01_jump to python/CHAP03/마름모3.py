# coding: cp949
while True:
    num=int(input("홀수를 입력하세요(0<-종료): "))
    empty=int(num/2)
    if num == 0 : break
    elif num % 2 == 0 : continue
    else:
        print(" "+"-"*num+" ")
        for emp in range(empty,-1):
            point=num-2*emp
            print("|"+" "*emp+"*"*point+" "*emp+"|")
        for empt in range(1,empty+1):
            point=num-2*emp
            pyrint("|"+" "*empt+"*"*point+" "*empt+"|")

        print(" "+"-"*num+" ")
