import urllib.request
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
tags = soup.find_all("a", href=re.compile('/movie/bi/mi/basic')) #영화 이름 찾기
m = re.compile('title="([\w:,]+)">')
k = m.findall(str(tags)) #findall은 그냥 바로 group지정된걸 가져오나? k는 영화 이름 리스트
up_down = soup.find_all('td', attrs={'class':'range ac'})#순위 변동 태그 찾기
m = re.compile('>(\d)<')
p = m.findall(str(up_down)) #p는 순위 변동 리스트
index = soup.find_all('img',attrs={'width':'14'}) #순위 찾기
m = re.compile('alt="([\d]{2})"')
r = m.findall(str(index)) #r은 순위 리스트
up_down_k = soup.find_all("img",attrs={'class':'arrow'}) #순위 상승 여부
m = re.compile('alt="([\w]{2})"')
t = m.findall(str(up_down_k)) #순위 상승 여부 리스트
movie_list = []
for a in range(45):
    movie_list.append(r[a] + "\t" + k[a] + "\t" + t[a] + "\t" +p[a])

print(movie_list)




