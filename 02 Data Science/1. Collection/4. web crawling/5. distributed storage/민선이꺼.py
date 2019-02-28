import urllib.request
from bs4 import BeautifulSoup
import re
import os

dir_num=1
dir_count=1
dir_name = './naver_ranking1'
file_name = '/movie1'
file_num='1'
html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html,'html.parser')
soup = str(soup)
tags_list = ['순위,영화명,변동폭']
p=re.compile(r'title="(.+)">\1</a>\n</div>\n</td>\n.+\n.+\n<td class="ac">.+alt="([a-z]+)".+\n<td class=.+(\d+)')
match_list = p.findall(soup)

def search_file_list(dir_name):
    try:
        file_list = os.listdir(dir_name) #listdir 경로 밑에 있는 파일들을 리스트로 리턴한다
        return len(file_list) #경로 밑에 파일들 그니까 파이썬 파일들이 몇개 있는지 리턴한다.
    except Exception:
        pass #해당 경로가 존재하지 않으면 패스
def search_dir_list(dir_name):
    global dir_num
    global dir_count
    dir_name = './naver_ranking%d' %dir_num #dir_name 은 디렉토리 이름
    if not os.path.isdir(dir_name): #하위에 이름이 같은 폴더가 없다면 만들고
        os.mkdir(dir_name)
        return dir_count,dir_name #dir count = 1, dir_name ~~1
    else:
        file_len = search_file_list(dir_name)
        if file_len<3:
            return dir_count,dir_name
        else:
            dir_num+=1
            dir_count+=1
            dir_count,dir_name = search_dir_list(dir_name)
            return dir_count,dir_name


for index in range(len(match_list)):
    if match_list[index][0].find(',')!=-1:
        title = '"'+match_list[index][0]+'"'
    else:
        title = match_list[index][0]
    if match_list[index][1]=='up':
        change = '+'+match_list[index][2]
    elif match_list[index][1]=='down':
        change = '-'+match_list[index][2]
    else:
        change = match_list[index][2]
    tags_list.append(str(index + 1) + ',' + title + ',' + change)

dir_count,dir_name = search_dir_list(dir_name) #값을 한 번에 두개 받기
file_len = search_file_list(dir_name)
file_name = '/movie%d'%((file_len+1)+(dir_count-1)*3)

f = open('%s%s.csv'%(dir_name,file_name),'w')
f.write('\n'.join(tags_list))
f.close()