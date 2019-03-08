import pandas as pd
import numpy

data_frame = pd.read_csv("Zip_Stat.csv", index_col=None)

def My_Ascendant(key):#오름차순
    global data_frame
    k = list(data_frame[key].array)
    k.sort()
    print(" ".join(str(v) for v in k))

def My_Descendant(key):#내림차순
    global data_frame
    k = list(data_frame[key].array)
    k.sort(reverse=True)
    print(" ".join(str(v) for v in k))

def My_Standard_Deviation(key):
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return("표준편차(Standard Deviation) 공식: √분산\n표준편차: "+str(numpy.std(data_frame[key].array)))

def My_Variance(key):#분산
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return("분산(Variance) 공식: ∑(표본-평균)**2/표본수\n분산: "+str(numpy.var(data_frame[key].array)))

def My_Deviation(key):
    global data_frame
    average = data_frame[key].array.sum() / len(data_frame[key].array)
    print("편차(Deviation)공식: 표본값 - 평균")
    print("표본"+"\t"+"편차")
    for a in data_frame[key].array:
        print(str(a)+"\t"+str(a-average))

def My_Min(key):
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return ("최소값: " + str(min(data_frame[key].array)))

def My_Max(key):
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return("최대값: "+str(max(data_frame[key].array)))

def My_Average(key):
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return ("평균: " +str(data_frame[key].array.sum()/len(data_frame[key].array)))

def My_Sum(key):
    global data_frame
    for a in data_frame[key].array:
        print(a)
    return("총합: "+ str(data_frame[key].array.sum()))

def print_col(key):
    global data_frame
    k = data_frame[key].array
    for a in k:
        print(a)

def print_row(key):
    global data_frame
    key = int(key)-2
    b = data_frame.iloc[key, :]
    k = b.array
    print(" ".join(str(v) for v in k))

while True:
    print("0.종료\n1.행\n2.열\n3.총합\n4.평균\n5.최대값\n6.최소값\n7.편차\n8.분산\n9.표준편차\n10.오름차순 정렬\n11.내림차순 정렬")
    menu_pick = int(input("메뉴를 선택하세요: "))
    if menu_pick != 0 :
        key = input("Access Key를 입력하세요: ")
        if menu_pick == 1:
            print_row(key)
        elif menu_pick == 2:
            print_col(key)
        elif menu_pick == 3:
            print(My_Sum(key))
        elif menu_pick == 4:
            print(My_Average(key))
        elif menu_pick == 5:
            print(My_Max(key))
        elif menu_pick == 6:
            print(My_Min(key))
        elif menu_pick == 7:
            My_Deviation(key)
        elif menu_pick == 8:
            print(My_Variance(key))
        elif menu_pick == 9:
            print(My_Standard_Deviation(key))
        elif menu_pick == 10:
            My_Ascendant(key)
        elif menu_pick == 11:
            My_Descendant(key)
    elif menu_pick == 0:
        exit()