#-*-coding: utf-8 -*-#
class HousePark:
    __last_name__ = "박" #프라이빗의 의미
    full_name = ""
    def __int__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))

class HouseKim(HousePark):
    pass

kitty = HouseKim("만복")
kitty.travel("제주도")

