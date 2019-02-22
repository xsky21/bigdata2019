#-*-coding: utf-8 -*-#
class HousePark():
    __lastname__ = "박" #프라이빗의 의미
    def __int__(self, name):
        self.full_name = self.__last_name__ + name
    def trabel(self,where):
        print("%s, %s 여행을 가다"%(self.full_name, where))

pey = HousePark("응용")
print(pey.__lastname__)

