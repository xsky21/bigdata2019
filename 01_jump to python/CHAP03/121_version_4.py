# coding: cp949

age_st=input("나이를 입력하세요.: ")
age=int(age_st)
fee=0
rate=""
if 0 <= age <=3:
    fee = 0
    rate = "유아"
elif 4<= age <=13:
    fee = 2000
    rate = "어린이"
elif 14<= age <=18:
    fee = 3000
    rate = "청소년"
elif 19<= age <=65:
    fee = 5000
    rate = "성인"
else
    fee = 0
    rate = "노인"

print("귀하의 등급은 %s등급이며 요금은 %d원 입니다." %(rate, fee))
if rate == "유아" or rate == "노인"
    print("티켓을 발급합니다.")
    exit()


