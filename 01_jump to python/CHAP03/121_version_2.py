# coding: cp949

age_st=input("���̸� �Է��ϼ���.: ")
age=int(age_st)
fee=0
rate=""
if 0 <= age <=3:
    fee = 0
    rate = "����"
    print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
elif 4<= age <=13:
    fee = 2000
    rate = "���"
    print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
elif 14<= age <=18:
    fee = 3000
    rate = "û�ҳ�"
    print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
elif 19<= age <=66:
    fee = 5000
    rate = "����"
    print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
elif age >= 66:
    fee = 0
    rate = "����"
    print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
else:
    print("�ٽ� �Է��ϼ���")
