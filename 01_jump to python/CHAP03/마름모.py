# coding: cp949
while True: num=int(input("Ȧ���� �Է��ϼ���(0<-����): ")) point = 1 #��ǥ ù��d° empty=int(num/2) if num == 0 : break elif num % 2 == 0 : continue else:
        while point <= num:
            print(" "*empty+"*"*point)
            point=int(point+2)
            empty=int(empty-1)
