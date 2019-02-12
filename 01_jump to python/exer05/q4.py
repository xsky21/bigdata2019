class Restaurant:
    number_served = 0
    todays_customer = 0
    def __init__(self,name,type):
        self.f = open("./고객서빙현황로그.txt","r")
        self.todays_customer = int(self.f.readline())
        self.f.close()
        self.resta_name = name
        self.resta_type = type
        self.f= open("./고객서빙현황로그.txt",'w')
    def describe_resta(self):
        print("저희 레스토랑 명칭은 \'"+self.resta_name+"\'이고 "+self.resta_type+"전문점 입니다.")
        openclose = input("레스토랑을 오픈하시겠습니까?(y/n) : ")
        if openclose == "y":pass
        else : exit()
    def open_resta(self):
        print("저희 "+self.resta_name+" 레스토랑 오픈했습니다.")
    def reset_number_served(self):
        self.number_served = 0
    def increment_number_served(self):
        self.number_served += int(number)
    def check_customer_number(self):
        print("지금까지 총 %d명 손님께서 오셨습니다." %(self.number_served))
    def __del__(self):
        print("이용해주셔서 감사합니다.")
        self.f.write(str(self.todays_customer + self.number_served))
        self.f.close()


name, type =input("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분 : )").split()
golmok = Restaurant(name, type)
golmok.describe_resta()
golmok.open_resta()
while True:
    number = input("어서오세요. 몇명이십니까?(초기화:0, 종료:-1, 누적고객 확인:p : ")
    if number  == "0":
        golmok.reset_number_served()
    elif number == "-1":
        print(name+" 레스토랑 문닫습니다.")
        exit()
    elif number == "p":
        golmok.check_customer_number()
    else :
        golmok.increment_number_served()

