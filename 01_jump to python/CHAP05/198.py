#-*-coding: utf-8 -*-#
class HousePark():
    __last_name__ = "박" #프라이빗의 의미
    full_name = ""
    def set_name(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))

pey = HousePark()
pey.set_name("응용")
pey.travel("부산")
print(pey.__last_name__)
