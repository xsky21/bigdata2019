import urllib.request
from bs4 import BeautifulSoup
import os
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags = soup.find_all("div", attrs = {'class' : "tit3"}) #영화 이름 찾기
up_down = soup.find_all('td', attrs={'class':'range ac'})#순위가 얼마나 바뀌었나
index = soup.find_all('img',width="14", height="13") #순위 찾기
up_down_image = soup.find_all("img", attrs = {'class':'arrow'}) #순위 상승 여부
movie_list = []
up_down_arrow =""
for b in range(49):
    if up_down_image[b].get("alt") == "na":
        up_down_arrow = " "
    elif up_down_image[b].get("alt") == "up":
        up_down_arrow = "+"
    elif up_down_image[b].get("alt") == "down":
        up_down_arrow = "-"
    movie_list.append(index[b].get("alt") + '\t' + (tags[b].a).text + "\t" + up_down_arrow + up_down[b].text)
movie_list = "\n".join(movie_list)
storage_number =1
file_path= "./distributed_storage_%d" % storage_number
file_number=1
file_name_number = 1
file_name= "/movie_%d.csv" % file_number
total_path = file_path + file_name
while True:
    crwaling = input("파일 생성할까요(y/n): ")
    if crwaling == "y":
     try :
         file = open(total_path,'w')
         file.write(movie_list)
         file.close()
     except Exception:#폴더가 없는 경우
         os.mkdir(file_path)
         file = open(total_path, 'w')
         file.write(movie_list)
         file.close()
     file_number += 1
     if file_number == 4:
            file_number = 1
            storage_number +=1
    elif crwaling == "n":
        exit()

