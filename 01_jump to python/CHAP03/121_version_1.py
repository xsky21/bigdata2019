# coding: cp949

age=input("나이를 입력하세요.: ")
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
print("요금은 %s원 입니다." %str(fee))
