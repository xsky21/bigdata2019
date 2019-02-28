import urllib.request
from bs4 import BeautifulSoup
import os

movie_list = "1"
storage_number = 1
file_number=1
def file_save():
    with open(total_path(), 'w') as file :
        file.write(movie_list)
    exit()
def file_path():
    return "./distributed_storage_"+str(storage_number)
def file_name():
    return "/movie_" + str(file_number) + ".csv"
def total_path():
    return file_path()+file_name()

while True:
    try :
        os.mkdir(file_path()) #distributed_storage_1 이라는 폴더를 만든다
    except FileExistsError: #폴더가 이미 있으면 에러가 뜬다. #에러가 떳을때 해당 폴더가 꽉 차있는지 아닌지 확인한다
        if len(os.listdir(file_path())) == 1 : #해당 폴더에 파일이 하나 있을 때
            file_number= 2
            print(total_path())
            file_save()
        elif len(os.listdir(file_path())) == 2: #해당 폴더에 파일이 두개 있을 때
            file_number= 3
            file_save()
        elif len(os.listdir(file_path())) == 3:
            #해당 폴더에 세 개 있을 때, 디렉토리 이름을 바꾸고 다시 루프를 돌린다.
            #다시 루프를 돌린다
            storage_number +=1
            continue
    else:
        file_save()


