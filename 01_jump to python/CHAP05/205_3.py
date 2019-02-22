#-*-coding: utf-8 -*-#
class HousePark:
    __last_name__ = "박" #프라이빗의 의미
    full_name = ""
    def __init__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))

class HouseKim(HousePark):
    __last_name__= "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가다"%(self.full_name, where, day))

kitty = HouseKim("만복")
print(kitty.__last_name__)
kitty.travel("제주도",3)

