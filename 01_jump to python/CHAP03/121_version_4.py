# coding: cp949

age_st=input("���̸� �Է��ϼ���.: ")
age=int(age_st)
fee=0
rate=""
if 0 <= age <=3:
    fee = 0
    rate = "����"
elif 4<= age <=13:
    fee = 2000
    rate = "���"
elif 14<= age <=18:
    fee = 3000
    rate = "û�ҳ�"
elif 19<= age <=65:
    fee = 5000
    rate = "����"
else
    fee = 0
    rate = "����"

print("������ ����� %s����̸� ����� %d�� �Դϴ�." %(rate, fee))
if rate == "����" or rate == "����"
    print("Ƽ���� �߱��մϴ�.")
    exit()


