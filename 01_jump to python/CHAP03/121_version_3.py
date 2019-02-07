# coding: cp949

age_st=input("나이를 입력하세요.: ")
age=int(age_st)
fee=0
rate=""
if 0 <= age <=3:
    fee = 0
    rate = "유아"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
    print("티켓을 발급합니다.")
    exit()
    
elif 4<= age <=13:
    fee = 2000
    rate = "어린이"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
elif 14<= age <=18:
    fee = 3000
    rate = "청소년"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
elif 19<= age <=66:
    fee = 5000
    rate = "성인"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
elif age >= 66:
    fee = 0
    rate = "노인"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
    print("티켓을 발급합니다.")
    exit()

pay_st=input("요금을 입력하세요.: ")
pay=int(pay_st)
charge=0
if pay==fee:
    print("감사합니다. 티켓을 발행합니다.")
elif pay>fee:
   charge = pay - fee
   print("감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다." % charge)
else:
    charge = fee - pay
    print("%d원이 모자랍니다. 입력하신 %d원을 반환합니다." %(charge,pay))
# modify1

