# coding: cp949

age=input("���̸� �Է��ϼ���.: ")
fee=0
if 0 <= int(age) <=3:
    fee = 0
elif 4<= int(age) <=13:
    fee = 2000
elif 14<= int(age) <=18:
    fee = 3000
elif 19<= int(age) <=66:
    fee = 5000
elif int(age) >= 66:
    fee = 0
print("����� %s�� �Դϴ�." %str(fee))
