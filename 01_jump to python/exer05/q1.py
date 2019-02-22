#-*- coding: utf-8 -*-"
class Restaurant:
    def __init__(self,name,type):
        self.resta_name = name
        self.resta_type = type
    def describe_resta(self):
        print("저희 레스토랑 명칭은 \'"+self.resta_name+"\'이고 "+self.resta_type+"전문점 입니다.")
    def open_resta(self):
        print("저희 "+self.resta_name+" 레스토랑 오픈했습니다. 어서오세요")

name, type =input("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분): ").split()
chinese = Restaurant(name, type)
chinese.describe_resta()
chinese.open_resta()
