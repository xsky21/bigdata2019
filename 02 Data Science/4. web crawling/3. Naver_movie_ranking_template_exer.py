import urllib.request
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags = soup.find_all("a", href=re.compile('/movie/bi/mi/basic')) #영화 이름 찾기
up_down = soup.find_all('td', attrs={'class':'range ac'})#순위 변동 태그 찾기
index = soup.find_all('img',attrs={'width':'14'}) #순위 찾기
up_down_k = soup.find_all("img",attrs={'class':'arrow'}) #순위 상승 여부
movie_list = []
up_down_arrow =""
for a in range(49):
    if up_down_k[a].get("alt") == "na":
        up_down_arrow = " "
    elif up_down_k[a].get("alt") == "up":
        up_down_arrow = "+"
    elif up_down_k[a].get("alt") == "down":
        up_down_arrow = "-"
    movie_list.append(index[a].get("alt") + '\t' + tags[a].get("title") + "\t" + up_down_arrow + up_down[a].text)
print("\n".join(movie_list))
movie_list = "\n".join(movie_list)
with open("movie.csv",'w') as file:
    file.write(movie_list)

