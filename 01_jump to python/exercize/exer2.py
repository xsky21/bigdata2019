#-*-coding: utf-8 -*-#
print("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다.")
print("1. 주문")
print("2. 종료")
enter = int(input("입력: "))
foodreserve = []

def input_gredient(a):
    foodreserve.append(a)

def make_sandwiches():
    print("샌드위치를 만들겠습니다.")
    for a in foodreserve:
        print(a+"추가합니다.")
    print(".\n.\n.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")
    exit()


if enter == 1:
    while True:
        food= input("안녕하세요. 원하시는 재료를 입력하세요. : ")
        if food == "종료":
            make_sandwiches()
        else :
            input_gredient(food)
else : exit()
