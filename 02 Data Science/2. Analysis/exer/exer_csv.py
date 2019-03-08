import csv
import sys
import math
def My_Descendant(key):#내림차순
    num_list = []
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = int(data[b][a])
        num_list.append(u)
    num_list.sort(reverse=True)
    for c in num_list:
        print(c)
def My_Ascendant(key):#오름차순
    num_list = []
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = int(data[b][a])
        num_list.append(u)
    num_list.sort()
    for c in num_list:
        print(c)
def My_Standard_Deviation(key):# 표준편차
    My_Variance = 0
    My_Deviation = 0
    My_Average = 0
    total_Deviation = 0
    total = 0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        total += int(u)
    My_Average = total / len(data)
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        total_Deviation += (int(u) - My_Average) * (int(u) - My_Average)
        result = math.sqrt(total_Deviation)
        return ("표준편차(Standard Deviation) 공식 : √분산\n"+"표준편차: "+ str(result))

def My_Variance(key):#분산
    My_Variance=0
    My_Deviation = 0
    My_Average = 0
    total_Deviation = 0
    total = 0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        total += int(u)
    My_Average = total / len(data)
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        total_Deviation += (int(u) - My_Average)*(int(u) - My_Average)
    return ("분산(Variance) 공식: Σ(표본-평균)**2/표본수\n" + str(total_Deviation/len(data)))

def My_Deviation(key):
    My_Deviation=0
    My_Average = 0
    total = 0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        total += int(u)
    My_Average = total / len(data)
    print("표본"+"\t"+"편차")
    for b in range(1, len(data)):
        u = data[b][a] # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u+"\t"+str(My_Average-int(u)))

def My_Min(key):
    My_Min = 0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        if int(u) < My_Min:
            My_Min = int(u)
        else: pass
    return ("최소값 :"+str(My_Min))

def My_Max(key):
    My_Max=0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        if int(u) > My_Max:
            My_Max = int(u)
        else: pass
    return ("최대값 :"+str(My_Max))

def My_Average(key):
    My_Average=0
    total = 0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1, len(data)):
        u = data[b][a]  # 왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        total += int(u)
    My_Average = total/len(data)
    return ("평균값: " + My_Average)

def My_Sum(key): # 총합
    total=0
    for a in range(len(data[0])):  # 열
        if data[0][a] == key:
            break
    for b in range(1,len(data)):
        u = data[b][a] #왜 이걸 두번 쓰면 아웃 오브 레인지가 뜨지?
        print(u)
        total += int(u)
    return("총합: " + total)

def print_col(key):
    for a in range(len(data[0])): #열
        if data[0][a] == key:
            break
    for b in range(1,len(data)):
        print((data[b][a]))

def print_row(key): #행
    print(" ".join(data[key-1]))

with open('Zip_Stat.csv',newline='') as infile:
    data=list(csv.reader(infile)) #data는 리스트 안에 리스트가 들어가 있는 형태

while True:
    print("0.종료\n1.행\n2.열\n3.총합\n4.평균\n5.최대값\n6.최소값\n7.편차\n8.분산\n9.표준편차\n10.오름차순 정렬\n11.내림차순 정렬")
    menu_pick = int(input("메뉴를 선택하세요: "))
    if menu_pick == 0 :
        exit()
    elif menu_pick == 1:
        key = int(input("Access Key를 입력하세요: "))
        print_row(key)
    elif menu_pick == 2:
        key = input("Access Key를 입력하세요: ")
        print_col(key)
    elif menu_pick == 3:
        key = input("Access Key를 입력하세요: ")
        print(My_Sum(key))
    elif menu_pick == 4:
        key = input("Access Key를 입력하세요: ")
        print(My_Average(key))
    elif menu_pick == 5:
        key = input("Access Key를 입력하세요: ")
        print(My_Max(key))
    elif menu_pick == 6:
        key = input("Access Key를 입력하세요: ")
        print(My_Min(key))
    elif menu_pick == 7:
        key = input("Access Key를 입력하세요: ")
        My_Deviation(key)
    elif menu_pick == 8:
        key = input("Acces Key를 입력하세요: ")
        print(My_Variance(key))
    elif menu_pick == 9:
        key = input("Acces Key를 입력하세요: ")
        print(My_Standard_Deviation(key))
    elif menu_pick == 10:
        key = input("Acces Key를 입력하세요: ")
        My_Ascendant(key)
    elif menu_pick == 11:
        key = input("Acces Key를 입력하세요: ")
        My_Descendant(key)
    elif menu_pick == 2:
        pass
