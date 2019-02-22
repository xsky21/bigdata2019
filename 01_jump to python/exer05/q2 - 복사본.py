#-*- coding: utf-8 -*-"
class Restaurant:
    def inform_resta(self):
        name, type =input("레스토랑 이름과 요리 종류를 선택하세요(공백으로 구분 : )").split()
        self.resta_name = name
        self.resta_type = type
    def describe_resta(self):
        print("저희 레스토랑 명칭은 \'"+self.resta_name+"\'이고 "+self.resta_type+"전문점 입니다.")
    def open_resta(self):
        print("저희 "+self.resta_name+" 레스토랑 오픈했습니다. 어서오세요")
    def __del__(self):
        print(self.resta_name+" 레스토랑 문 닫습니다.")

restaurant_list=[]
for index in range(3):
    restaurant_list.append(Restaurant())
    restaurant_list[index].inform_resta()
    restaurant_list[index].describe_resta()
    restaurant_list[index].open_resta()

print("저녁 10시가 되었습니다.")
