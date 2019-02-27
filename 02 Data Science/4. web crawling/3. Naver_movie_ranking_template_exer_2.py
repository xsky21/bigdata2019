import urllib.request
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
re_name = re.compile('href="/movie/bi/mi/basic.nhn[?]code=[0-9]{5,6}" title="(.+)"') #영화제목
re_name_2 = re_name.findall(str(soup))
re_ranking = re.compile('''alt="([0-9]+)" width="14" height="13"''')#영화 순위
re_renking_2 = re_name.findall(str(soup))
re_up_down = re.compile('''([0-9])</td>\n''')
re_up_down_2 = re_up_down.findall(str(soup))#순위 변동
re_arrow = re.compile('''" height="10" class="arrow"''')
re_arrow_2 = re_arrow.findall(str(soup))
print(len(re_arrow_2))

