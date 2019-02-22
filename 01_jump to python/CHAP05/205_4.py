#-*-coding: utf-8 -*-#
class HousePark:
    __last_name__ = "박" #프라이빗의 의미
    full_name = ""
    def __init__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))
    def love(self,other):
        print("%s, %s와 사랑에 빠졌다."%(self.full_name, other.full_name))
    def __add__(self, other):
        print("%s, %s와 결혼했네" %(self.full_name, other.full_name))

class HouseKim(HousePark):
    __last_name__= "김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가다"%(self.full_name, where, day))

pey = HousePark("응용")
juliet = HouseKim("주리")
pey.travel("대구")
juliet.travel("대구", 3)
pey.love(juliet)
pey+juliet

