import urllib.request
from bs4 import BeautifulSoup
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
# print(soup)
#print(soup.prettify)
tags = soup.findAll('div',attrs={'class':'tit3'})
print(tags)
up_down = soup.find('img',attrs={'src':'http://imgmovie.naver.net/2007.img/common.icon_na_1.gif'})

#과제 랭킹 웹페이지를 분석해서 csv 파일을 생성하시오 순위, 영화명, 변동폭 순