# coding: cp949

age_st=input("나이를 입력하세요.: ")
age=int(age_st)
fee=0
rate=""
if 0 <= age <=3:
    fee = 0
    rate = "유아"
    print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
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
else:
    print("다시 입력하세요")
