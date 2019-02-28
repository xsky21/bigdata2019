import urllib.request
from bs4 import BeautifulSoup
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
print("\n".join(movie_list))
movie_list = "\n".join(movie_list)
with open("movie.csv",'w') as file:
    file.write(movie_list)

