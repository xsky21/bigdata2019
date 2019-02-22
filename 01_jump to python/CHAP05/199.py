#-*-coding: utf-8 -*-#
class HousePark():
    __lastname__ = "박" #프라이빗의 의미
    full_name = ""
    def set_name(self,name):
        self.fullname = self.__last_name__ + name
    def trabel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))

pey = HousePark()
pes = HousePark()
print(pey.__lastname__)
print(pes.__lastname__)
